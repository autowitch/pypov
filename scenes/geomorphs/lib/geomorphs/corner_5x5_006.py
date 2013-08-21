
from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object
from pypov.pov import Union, Difference
from lib.metadata import Metadata

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import wall_texture_1, cross_hatch_2


def corner_5x5_006_info():
    return Metadata("Basic four entrance room", "f2",
            description="Basic four entrance room", block_type="normal",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def corner_5x5_006(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Union(
                Box((-2.5, 10, -2.5), (  5, 21, -26)),
                Box(( 5, 10, -2.5), (-26, 21,   2.5)),

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
