from pypov.pov import Texture, Pigment, Cylinder
from pypov.pov import Finish, Box, Cone, Object
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def corner_5x5_014_info():
    return Metadata("Basic diamond shaped room with side rooms", "c14",
            description="Basic diamond shaped room with side rooms",
            block_type="corner",
            bottom=0, top=20,
            size="5x5",
            repeatable=True,
            fully_connected=True,
            dead_ends=False,
            entrance=False,
            has_rooms=False,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['diamond', 'angle', 'room', 'basic', 'multiple rooms', 'side chambers'])

def corner_5x5_014(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Box((-2.5, 10, -2.49999), (  2.5, 21, -26)),
            Box(( 2.5, 10, -2.5), (-26, 21,   2.5)),
            Union(
                Box((-10, 10.0001, -10), (10, 21, 10)),
                Box((-12, 10.0001, -7), (-22, 21, 7)),
                Box((12, 10.0001, -7), (22, 21, 7)),
                Box((-7, 10.0001, 12), (7, 21, 22)),
                Box((-7, 10.0001, -12), (7, 21, -22)),
                Box((-13, 10.00002, -2), (13, 18, 2)),
                Box((-2, 10.00003, -13), (2, 18, 13)),
                rotate=(0, 45, 0),
            ),
            wall_texture_1
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
