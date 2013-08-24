from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_008_info():
    return Metadata("Pit passage", "e8",
            description="Complex of rooms around a passage with a deep pit",
            block_type="edge",
            bottom=0, top=20,
            size="5x10",
            repeatable=False,
            fully_connected=True,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['pit', 'bridges', 'complex'])

def edge_5x10_008(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Union(
                five_by_ten_edge(),
                Box((-50, 0, -25), (50, -50, 25)),
                cross_hatch_texture,
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001,  -12), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002,  2.50001), (  27.5, 21, -26)),
                Box((  -51, 10,  -2.5), (51, 21,   2.5)),
                Box((  -20, 10.0001,  -6), (20, 21,   6)),
                Box((  -20, 8,  -6), (20, -45.0001,   6)),
                Box((  -16, -45,  -5.9999), (-8, 21,   5.9999)),
                Box((  16, -45,  -5.9999), (8, 21,   5.9999)),
                Box((  4, -45,  -5.9999), (-4, 21,   5.9999)),

                Box((  4, 11, 0), (8, 16, 8)),
                Box((  -2, 12, 8), (14, 21, 22)),
                Box((  -4, 12, 10), (-18, 21, 22)),
                Box(( -5, 13, 14), (-1, 17, 18)),

                Box((  -4, 11, 0), (-8, 16, -8)),
                Box((  2, 12, -8), (-14, 21, -22)),

                Box((27, 10, 5), (46, 21, 15)),
                Box((27, 10, 14.9999), (32, 21, 23)),
                Box((34, 10, 14.9999), (39, 21, 23)),
                Box((41, 10, 14.9999), (46, 21, 23)),
                Box((34, 10, 5.0001), (39, 21, 2.49999)),

                Box((-18, 10, -9), (-40, 21, -20)),
                Box((-42, 15, -15), (-45, 21, 0)),
                Box((-42.001, 12.5, -15), (-39, 21, -12)),
                wall_texture_1
            ),
        ),
        Cylinder((-24, 10, -14.5), (-24, 21, -14.5), 1.5, wall_texture_1),
        Cylinder((-34, 10, -14.5), (-34, 21, -14.5), 1.5, wall_texture_1),
        translate=translate,
        rotate=rotate
    )
    return geomorph
