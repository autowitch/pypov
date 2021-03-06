from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_013_info():
    return Metadata("Pit with bridge", "e13",
            description="Pit with bridge",
            block_type="edge",
            bottom=-50, top=20,
            size="5x10",
            repeatable=True,
            fully_connected=False,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['pit', 'bridge'])

def edge_5x10_013(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
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
                Box(( -27.50001, 10,      -20.00001), (27.50001, 21,  -15.00001)),

                Box(( -15, -45, -10), (15, 21, 10)),
                wall_texture_1
            ),
        ),
        Union(
            Box((-15, 8, -1), (15, 10, 1)),
            wall_texture_1
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph
