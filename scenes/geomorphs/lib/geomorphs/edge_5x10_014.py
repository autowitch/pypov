from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_014_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def edge_5x10_014(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
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
                Box((  22.5, 10.0002, 2.5), (  27.5, 21, -26)),
                Box(( -51,   10,       -2.5), (22.50001,   21,   2.5)),
                Box(( 30,   10,       -2.5), (51,   21,   2.5)),
                Box(( -27.5, 10,      -20.0), (2.5, 21,  -15.0)),
                Box((-2.5, 10, -15.0001), (2.5, 21, -9.9999)),
                Box((-2.5, 10, 15.0001), (2.5, 21, 9.9999)),
                Box((-2.5, 10, 15), (35, 21, 20)),
                Box((30, 10, 15.0001), (35, 21, 2.4999)),

                Box(( -15, -45, -10), (15, 21, 10)),
                wall_texture_1
            ),
        ),
        Union(
            Difference(
                Cylinder((0, 0, -1), (0, 0, 1), 20, "scale <1, 0.5, 1> translate <0, 10, 0>"),
                Cylinder((0, 0, -2), (0, 0, 2), 18, "scale <1, 0.5, 1> translate <0, 10, 0>"),
                Box((-21, 10, -2), (21, -40, 2)),
            ),
            Box((-1, 10, -10), (1, 8, 10)),
            wall_texture_1
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph
