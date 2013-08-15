#!/usr/bin/env python

import os
import sys
# Assumes that a symlink to the pov modules is in the lib dir

import argparse
from pypov.pov import File, Settings, POV, parse_args

def main():

    """docstring for main"""

    parser = argparse.ArgumentParser(description='Geomorphed based dungeon generator',
            prefix_chars='+-')
    parser.add_argument('-D', '--detail-level',
                        type=int,
                        default=10,
                        dest='detail_level',
                        help='Set the level of detail fo the scene')
    args = parse_args(parser)

    pov_file = File("dungeon.pov")
    pov_file.include("colors.inc")
    pov_file.include("stones.inc")
    pov_file.include("metals.inc")

    settings = Settings()
    renderer = POV()
    renderer.render(pov_file, settings)

if __name__ == '__main__':
    main()
