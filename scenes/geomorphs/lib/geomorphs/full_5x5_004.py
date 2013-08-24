from pypov.pov import Texture, Pigment, Cylinder
from pypov.pov import Finish, Box, Cone, Object
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def full_5x5_004_info():
    return Metadata("Basic oval room", "f4",
            description="Basic oval room",
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
            keywords=['round', 'oval', 'rooms', 'basic'])

def full_5x5_004(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Box((-2.5, 10, 26), (  2.5, 21, -26)),
            Box((26, 10, -2.5), (-26, 21,   2.5)),
            Cylinder((0, 10.0001, 0), (0, 21, 0), 12, scale=(1.5, 1, 1)),
            wall_texture_1
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
