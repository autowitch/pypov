#!/usr/bin/env python

import os
import sys
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

        for x in geomorphs:
            geomorph_module = None
            try:
                geomorph_module = __import__('lib.geomorphs.%s' % x)
                module = getattr(geomorph_module.geomorphs, x)
                geomorph_function = getattr(module, x)
                info_function = getattr(module, '%s_info' % x)
                modules.append((geomorph_function, info_function()))
                print "Loaded: %s" % x
            except ImportError, e:
                print 'ERROR: geomorph %s could not be loaded' % (x)
                print e
            except AttributeError, e:
                print 'ERROR: geomorph %s has missing functions' % (x)
                print e
        return modules

    def arrange_geomorphs(self, geomorphs):
        arranged = {
            '5x5':{'dead_end':[], 'corner':[], 'pipe':[], 'edge':[], 'full':[]},
            '5x10':{'edge':[], 'full':[]},
            '10x10':{'full':[]},
            '10x20':{'full':[]},
            '20x20':{'full':[]}
        }

        for (geomorph, metadata) in geomorphs:
            print metadata.__dict__

        return arranged



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
