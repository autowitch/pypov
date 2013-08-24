from pypov.pov import Texture, Pigment, Cylinder
from pypov.pov import Finish, Box, Cone, Object
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def full_5x5_005_info():
    return Metadata("Basic diamond shaped room with round side rooms", "f5",
            description="Basic diamond shaped room with round side rooms",
            block_type="full",
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
            keywords=['diamond', 'angle', 'room', 'round', 'circular', 'basic', 'multiple rooms', 'side chambers'])

def full_5x5_005(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Box((-2.5, 10, 26), (  2.5, 21, -26)),
            Box((26, 10, -2.5), (-26, 21,   2.5)),
            Union(
                Box((-10, 10.0001, -10), (10, 21, 10)),
                Cylinder((-19, 10, 0), (-19, 21, 0), 7),
                Cylinder((19, 10, 0), (19, 21, 0), 7),
                Cylinder((0, 10, 19), (0, 21, 19), 7),
                Cylinder((0, 10, -19), (0, 21, -19), 7),
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
