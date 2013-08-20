#!/usr/bin/env python

import os
import sys
# Assumes that a symlink to the pov modules is in the lib dir

import argparse
from pypov.pov import File, Settings, POV, parse_args, Camera
from lib.environment import general, ground
from lib.textures import cross_hatch, cross_hatch_2, cross_hatch_3


def main():
    """docstring for main"""
    parser = argparse.ArgumentParser(description='Render a single geomorph',
            prefix_chars='+-')
    parser.add_argument('-D', '--detail-level',
                        type=int,
                        default=10,
                        dest='detail_level',
                        help='Set the level of detail fo the scene')
    parser.add_argument('-g', '--geomorph',
                        type=str,
                        default='gm01',
                        dest='geomorph',
                        help='Select the geomorph to renger')
    parser.add_argument('--list',
                        default=None,
                        action='store_true',
                        dest='list_geomorphs',
                        help='List all geomorphs')
    parser.add_argument('--info', default=None,
                        action='store_true',
                        dest='info',
                        help='Display information about a specific geomorph')
    parser.add_argument('--earth-texture', default=None,
                        type=str,
                        choices=['checker', 'glass', 'clear'],
                        dest='earth_texture',
                        help='Set the texture the geomorph is rendered inside')
    parser.add_argument('--ground-offset',
                        default=0,
                        type=int,
                        dest='ground_offset',
                        help='Set the offset to the ground plane')

    parser.add_argument('-R', '--rotate',
                        nargs=3,
                        type=float,
                        default=None,
                        dest='rotation',
                        metavar=('X', 'Y', 'Z'),
                        help='Set camera location')
    args = parse_args(parser)

    if args.list_geomorphs:
        path = os.path.realpath(__file__)
        path = "%s/lib/geomorphs" % path[:path.rfind('/')]
        print "geomorphs found in %s:" % path
        # How silly can we make this?
        geomorphs = \
                '\n'.join(
                    sorted(
                        map(lambda x : x[:x.rfind('.')],
                            filter(
                                lambda x : x.endswith('.py') and \
                                           not x.startswith('_'),
                                os.listdir(path)
                            )
                        )
                    )
                )
        print geomorphs
        sys.exit(0)

    geomorph_module = None
    try:
        geomorph_module = __import__('lib.geomorphs.%s' % args.geomorph)
        #print dir(geomorph_module)
        #print geomorph_module.__dict__
        module = getattr(geomorph_module.geomorphs, args.geomorph)
        function = getattr(module, args.geomorph)
    except ImportError, e:
        print 'geomorph %s was not found. Use the --list option to see what' \
            'geomorphs are available\n' % (args.geomorph)
        print e
        sys.exit(0)

    if args.info:
        # print "calling %s_info" % args.geomorph
        info_function = getattr(module, '%s_info' % args.geomorph)
        data = info_function()
        for x in sorted(data.__dict__):
            print "%s: %s" % (x, data.__dict__[x])
        sys.exit(0)

    earth_texture = cross_hatch_2
    if args.earth_texture:
        textures = {'glass':cross_hatch_3,
                'checker':cross_hatch,
                'clear':cross_hatch_2,
        }
        earth_texture = textures[args.earth_texture]

    rotation = (0, 0, 0)
    if args.rotation:
        rotation = args.rotation

    pov_file = File("geomorph-test.pov")
    pov_file.include("colors.inc")
    pov_file.include("stones.inc")
    pov_file.include("metals.inc")
    pov_file.include("functions.inc")
    general(pov_file)
    ground(pov_file, offset=args.ground_offset)
    camera = Camera(
        location = (-150, 250, -60),
        look_at = (0, 25, 0)
    )
    camera.write(pov_file)

    function(rotate=rotation, translate=(0, 0, 0),
            detail_level=args.detail_level,
            cross_hatch_texture=earth_texture).write(pov_file)

    settings = Settings()
    renderer = POV()
    renderer.render(pov_file, settings)


if __name__ == '__main__':
    main()
