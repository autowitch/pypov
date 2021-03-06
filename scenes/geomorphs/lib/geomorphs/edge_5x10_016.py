from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_016_info():
    return Metadata("Pit with side rooms", "e16",
            description="Pit with two side rooms and connected bridges",
            block_type="edge",
            bottom=-50, top=20,
            size="5x10",
            repeatable=True,
            fully_connected=True,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['pit', 'bridge', 'bridges', 'side chambers'])

def edge_5x10_016(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge()),
                Box((-50, 0, -25), (50, -50, 25)),
                cross_hatch_texture,
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001, -15.0001), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002, -15.0001), (  27.5, 21, -26)),
                Box(( -51,   10,       -2.5), (51,   21,   2.5)),
                Box(( -27.50001, 10,      -20.0), (27.500001, 21,  -15.0)),

                Box(( -15, -45, -10), (15, 21, 10)),

                Box((-12, 10, 12), (12, 21, 23)),
                Box((-2.5, 10, 9.9999), (2.5, 18, 12.00001)),

                Box((-12, 10.00001, -12), (12, 21, -23)),
                Box((-2.5, 10.00001, -9.9999), (2.5, 18, -12.00001)),
                wall_texture_1
            ),
        ),
        Union(
            Box((-15, 8, -1), (15, 10, 1)),
            Box((-1, 8, 1), (1, 10, 10)),
            Box((-1, 8, -1), (1, 10, -10)),
            wall_texture_1
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph
