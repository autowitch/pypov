from pypov.pov import Texture, Pigment
from pypov.pov import Union, Difference, Object, Box

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def full_5x5_003_info():
    return Metadata("Basic stepped room", "f3",
            description="Basic stepped room",
            block_type="full",
            bottom=0, top=20,
            size="5x5",
            repeatable=True,
            fully_connected=True,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['basic', 'simple', 'room'])

def full_5x5_003(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Union(
                Box((-2.5, 10, 26), (    2.5, 21, -26), wall_texture_1),
                Box((26,   10.00002, -2.5), (-26,   21,   2.5), wall_texture_1),
                Box((-14, 10.00001, -14), ( 14, 21,  14)),

                Box((-20, 10.00002, -8), ( -11, 21,  8)),
                Box(( 20, 10.00003, -8), (  11, 21,  8)),
                Box(( -8, 10.00003, -20), (  8, 21, -11)),
                Box(( -8, 10.00003,  20), (  8, 21,  11)),
                wall_texture_1
            )
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
