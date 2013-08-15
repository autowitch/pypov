#!/usr/bin/env python

import os
import sys
# Assumes that a symlink to the pov modules is in the lib dir

import argparse
from pypov.pov import File, Settings, POV, parse_args, Camera
from lib.environment import general, ground


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

    pov_file = File("geomorph-test.pov")
    pov_file.include("colors.inc")
    pov_file.include("stones.inc")
    pov_file.include("metals.inc")
    general(pov_file)
    ground(pov_file)
    camera = Camera(
        location = (-150, 250, -25),
        look_at = (0, 25, 0)
    )
    camera.write(pov_file)

    geomorph_module = None
    try:
        geomorph_module = __import__('lib.geomorphs.%s' % args.geomorph)
        print dir(geomorph_module)
        print geomorph_module.__dict__
        module = getattr(geomorph_module.geomorphs, args.geomorph)
        function = getattr(module, args.geomorph)
    except ImportError, e:
        print 'geomorph %s was not found. Use the --list option to see what' \
            'geomorphs are available\n' % (args.geomorph)
        print e
        sys.exit(0)



    function(rotate=(0, 0, 0), translate=(0, 0, 0),
            detail_level=args.detail_level).write(pov_file)

    settings = Settings()
    renderer = POV()
    renderer.render(pov_file, settings)


if __name__ == '__main__':
    main()
