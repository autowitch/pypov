#!/usr/bin/env python

import os
import sys
import re
# Assumes that a symlink to the pov modules is in the lib dir

import argparse
from pypov.pov import File, Settings, POV, parse_args

class Dungeon(object):
    """docstring for Dungeon"""
    def __init__(self):
        super(Dungeon, self).__init__()


    def find_geomorphs(self):
        path = os.path.realpath(__file__)
        path = "%s/lib/geomorphs" % path[:path.rfind('/')]
        print "geomorphs found in %s:" % path
        # How silly can we make this?
        geomorphs = sorted(
                        map(lambda x : x[:x.rfind('.')],
                            filter(
                                lambda x : x.endswith('.py') and \
                                           not x.startswith('_'),
                                os.listdir(path)
                            )
                        )
                    )
        print "Found geomorph modules:\n%s" %  geomorphs
        return geomorphs

    def load_geomorph_modules(self, geomorphs):
        modules = []
        count = 0
        fail_count = 0
        incomplete_count = 0

        for x in geomorphs:
            geomorph_module = None
            try:
                geomorph_module = __import__('lib.geomorphs.%s' % x)
                module = getattr(geomorph_module.geomorphs, x)
                geomorph_function = getattr(module, x)
                geomorph_info = getattr(module, '%s_info' % x)()

                if 'INCOMPLETE' in geomorph_info.keywords:
                    print "WARNING: %s is incomplete!" % x
                    incomplete_count += 1
                    continue

                geomorph = (x, geomorph_function, geomorph_info)
                modules.append(geomorph)

                print "Loaded: %s (%s): %s" % (x, geomorph_info.shortcode, \
                        geomorph_info.name)
                count += 1
            except ImportError, e:
                print 'ERROR: geomorph %s could not be loaded' % (x)
                print e
                fail_count += 1
            except AttributeError, e:
                print 'ERROR: geomorph %s has missing functions' % (x)
                print e
                fail_count += 1

        print "%d total geomorphs loaded" % count
        print "%d are incomplete and were skipped" % incomplete_count
        print "%d had problems and could not be loaded" % fail_count
        return modules

    def audit_geomorph(self, name, metadata):
        rc = True

        if metadata.block_type not in ['dead end', 'corner', 'pipe', 'edge', 'full']:
            print "WARNING: %s has invalid block type: %s" % metadata.block_type
            rc = False

        if metadata.size not in ['5x5', '5x10', '10x10', '10x20', '20x20']:
            print "WARNING: %s has invalid size: %s" % metadata.size
            rc = False

        if metadata.block_type in ['dead end', 'corner', 'pipe'] and \
                metadata.size != '5x5':
            print "WARNING: %s is %s and has a type of %s (1)" % (name, metadata.size, \
                    metadata.block_type)
            rc = False

        if metadata.block_type == 'edge' and metadata.size not in ['5x5', '5x10']:
            print "WARNING: %s is %s and has a type of %s (2)" % (name, metadata.size, \
                    metadata.block_type)
            rc = False

        if 'corner' in name and metadata.block_type is not 'corner':
            print "WARNING: Block %s has 'corner' in name, but block type is %s" % \
                    (name, metadata.block_type)
            rc = False
        if 'edge' in name and metadata.block_type is not 'edge':
            print "WARNING: Block %s has 'edge' in name, but block type is %s" % \
                    (name, metadata.block_type)
            rc = False
        if 'full' in name and metadata.block_type is not 'full':
            print "WARNING: Block %s has 'full' in name, but block type is %s" % \
                    (name, metadata.block_type)
            rc = False
        if 'dead_end' in name and metadata.block_type is not 'dead end':
            print "WARNING: Block %s has 'dead_end' in name, but block type is %s" % \
                    (name, metadata.block_type)
            rc = False
        if 'pipe' in name and metadata.block_type is not 'pipe':
            print "WARNING: Block %s has 'pipe' in name, but block type is %s" % \
                    (name, metadata.block_type)
            rc = False

        if '5x5' in name and metadata.size is not '5x5':
            print "WARNING: Block %s has '5x5' in name, but block size is %s" % \
                    (name, metadata.size)
            rc = False
        if '5x10' in name and metadata.size is not '5x10':
            print "WARNING: Block %s has '5x10' in name, but block size is %s" % \
                    (name, metadata.size)
            rc = False
        if '10x10' in name and metadata.size is not '10x10':
            print "WARNING: Block %s has '10x10' in name, but block size is %s" % \
                    (name, metadata.size)
            rc = False
        if '10x20' in name and metadata.size is not '10x20':
            print "WARNING: Block %s has '10x20' in name, but block size is %s" % \
                    (name, metadata.size)
            rc = False
        if '20x20' in name and metadata.size is not '20x20':
            print "WARNING: Block %s has '20x20' in name, but block size is %s" % \
                    (name, metadata.size)
            rc = False

        if not re.match("^(corner|dead_end|edge|full|pipe)_(entrance_)?(5x5|5x10|10x10|10x20|20x20)_[0-9]+(-.*$)?", name):
            print "WARNING: %s name is in wrong format" % name
            print '         it should match "^(corner|dead_end|edge|full|pipe)_(entrance_)?(5x5|5x10|10x10|10x20|20x20)_[0-9]+(-.*$)?"'
            rc = False

        if 'entrance' in name and not metadata.entrance:
            print "WARNING: Block has 'entrance' in name, but block type is not an entrance" % name
            rc = False


        return rc


    def arrange_geomorphs(self, geomorphs):
        arranged = {
            '5x5':{'dead end':[], 'corner':[], 'pipe':[], 'edge':[], 'full':[]},
            '5x10':{'edge':[], 'full':[]},
            '10x10':{'full':[]},
            '10x20':{'full':[]},
            '20x20':{'full':[]}
        }
        short_codes = {}
        audit_fail_count = 0

        for (name, geomorph, metadata) in geomorphs:
            if not self.audit_geomorph(name, metadata):
                audit_fail_count += 1

            if not metadata.shortcode in short_codes:
                short_codes[metadata.shortcode] = (geomorph, metadata)
            else:
                print "WARNING: %s shortcode duplicated in %s" % \
                        (metadata.shortcode, name)

            if metadata.size == '5x5':
                if metadata.block_type == 'full':
                    arranged['5x5']['full'].append((name, geomorph, metadata))
                elif metadata.block_type == 'edge':
                    arranged['5x5']['edge'].append((name, geomorph, metadata))
                elif metadata.block_type == 'corner':
                    arranged['5x5']['corner'].append((name, geomorph, metadata))
                elif metadata.block_type == 'pipe':
                    arranged['5x5']['pipe'].append((name, geomorph, metadata))
                elif metadata.block_type == 'dead_end':
                    arranged['5x5']['dead_end'].append((name, geomorph, metadata))
                else:
                    print "ERROR: %s attemted to insert block type %s into 5x5" % \
                            (name, metadata.block_type)

            elif metadata.size == '5x10':
                if metadata.block_type == 'full':
                    arranged['5x10']['full'].append((name, geomorph, metadata))
                elif metadata.block_type == 'edge':
                    arranged['5x10']['edge'].append((name, geomorph, metadata))
                else:
                    print "ERROR: %s attemted to insert block type %s into 5x10" % \
                            (name, metadata.block_type)

            elif metadata.size == '10x10':
                if metadata.block_type == 'full':
                    arranged['10x10']['full'].append((name, geomorph, metadata))
                else:
                    print "ERROR: %s attemted to insert block type %s into 10x10 full" % \
                            (name, metadata.block_type)

            elif metadata.size == '10x20':
                if metadata.block_type == 'full':
                    arranged['10x20']['full'].append((name, geomorph, metadata))
                else:
                    print "ERROR: %s attemted to insert block type %s into 10x20 full" % \
                            (name, metadata.block_type)

            elif metadata.size == '20x20':
                if metadata.block_type == 'full':
                    arranged['20x20']['full'].append((name, geomorph, metadata))
                else:
                    print "ERROR: %s Attemted to insert block type %s into 20x20 full" % \
                            (name, metadata.block_type)

            else:
                print "ERROR: %s - unrecognized block size: %s" % (name, metadata.size)


        print "%d geomorphs have potential problems" % audit_fail_count

        return arranged, short_codes



    #def foo(self):

        #geomorph_module = None
        #try:
            #geomorph_module = __import__('lib.geomorphs.%s' % args.geomorph)
            ##print dir(geomorph_module)
            ##print geomorph_module.__dict__
            #module = getattr(geomorph_module.geomorphs, args.geomorph)
            #function = getattr(module, args.geomorph)
        #except ImportError, e:
            #print 'geomorph %s was not found. Use the --list option to see what' \
                #'geomorphs are available\n' % (args.geomorph)
            #print e
            #sys.exit(0)

        #if args.info:
            ## print "calling %s_info" % args.geomorph
            #info_function = getattr(module, '%s_info' % args.geomorph)
            #data = info_function()
            #for x in sorted(data.__dict__):
                #print "%s: %s" % (x, data.__dict__[x])
            #sys.exit(0)

        #earth_texture = cross_hatch_2
        #if args.earth_texture:
            #textures = {'glass':cross_hatch_3,
                    #'checker':cross_hatch,
                    #'clear':cross_hatch_2,
            #}
            #earth_texture = textures[args.earth_texture]

        #rotation = (0, 0, 0)
        #if args.rotation:
            #rotation = args.rotation

        #pov_file = File("geomorph-test.pov")
        #pov_file.include("colors.inc")
        #pov_file.include("stones.inc")
        #pov_file.include("metals.inc")
        #pov_file.include("functions.inc")
        #pov_file.include("shapes.inc")
        #pov_file.include("textures.inc")
        #general(pov_file)
        #ground(pov_file, offset=args.ground_offset)
        #camera = Camera(
            #location = (-150, 250, -60),
            #look_at = (0, 25, 0)
        #)
        #camera.write(pov_file)

        #function(rotate=rotation, translate=(0, 0, 0),
                #detail_level=args.detail_level,
                #cross_hatch_texture=earth_texture).write(pov_file)

        #settings = Settings()
        #renderer = POV()
        #renderer.render(pov_file, settings)


def main():

    """docstring for main"""

    parser = argparse.ArgumentParser(description='Geomorphed based dungeon generator',
            prefix_chars='+-')
    parser.add_argument('-D', '--detail-level',
                        type=int,
                        default=10,
                        dest='detail_level',
                        help='Set the level of detail fo the scene')
    parser.add_argument('--earth-texture', default=None,
                        type=str,
                        choices=['checker', 'glass', 'clear'],
                        dest='earth_texture',
                        help='Set the texture the geomorph is rendered inside')
    parser.add_argument('-R', '--rotate',
                        nargs=3,
                        type=float,
                        default=None,
                        dest='rotation',
                        metavar=('X', 'Y', 'Z'),
                        help='Set camera location')
    args = parse_args(parser)

    d = Dungeon()
    geomorphs = d.load_geomorph_modules(d.find_geomorphs())
    d.arrange_geomorphs(geomorphs)
    #pov_file = File("dungeon.pov")
    #pov_file.include("colors.inc")
    #pov_file.include("stones.inc")
    #pov_file.include("metals.inc")


    #settings = Settings()
    #renderer = POV()
    #renderer.render(pov_file, settings)

if __name__ == '__main__':
    main()
