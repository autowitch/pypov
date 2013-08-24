from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_012_info():
    return Metadata("Bridges", "e12",
            description="Large deep pit with bridges over it",
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
            keywords=['pit', 'bridges'])

def edge_5x10_012(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
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
                Box(( -22.5, 10.0001, -10), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002, -10), (  27.5, 21, -26)),
                Box(( -51,   10,       -2.5), (51,   21,   2.5)),
                Box(( -27.5, 10,      -10.0), (27.5, 21,  -5.0)),
                Box(( -15, -45, -15), (15, 21, 15)),
                wall_texture_1
            ),
        ),
        Union(
            Box((-15, 8, -1), (15, 10, 1)),
            Box((-15, 8, -8.5), (15, 10, -6.5)),
            wall_texture_1
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph
