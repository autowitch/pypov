from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object
from pypov.pov import Union, Difference

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1

from lib.metadata import Metadata

def corner_5x5_004_info():
    return Metadata("Corner room with pit", "c4",
            description="Two passages open up into a room that is filled with a 100' deep stepped pit.",
            block_type="corner",
            bottom=-100, top=20, size="5x5",
            repeatable=False, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)


def corner_5x5_004(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Union(
                five_by_five_corner(),
                Difference(
                    Union(
                        Box((-20,  -50, -20), (20, 0, 20)),
                        Box((-15,  -95, -15), (15, 0, 15)),
                        Box((-25, -100, -25), (25, -79.99999, 25)),
                    ),
                    Box((-21, -80, 0), (0, 0, 21)),
                ),
                cross_hatch_texture),
            Union(
                Box(( -2.5,  10,  -5), (  2.5, 21, -26)),
                Box((  5,  10.00002,  -2.5), (-26, 21,   2.5)),
                Box((-20,  10.00001, -20), ( 20, 21,  20)),
                Box((-19,   0,  -19), ( 19, 21,  19)),
                Box((-18,  -10, -18), ( 18, 21,  18)),
                Box((-17,  -20, -17), ( 17, 21,  17)),
                Box((-16,  -30, -16), ( 16, 21,  16)),
                Box((-15,  -40, -15), ( 15, 21,  15)),
                Box((-14,  -50, -14), ( 14, 21,  14)),
                Box((-13,  -60, -13), ( 13, 21,  13)),
                Box((-12,  -70, -12), ( 12, 21,  12)),
                Box((-11,  -80.0001, -11), ( 11, 21,  11)),
                Box((-10,  -90, -10), ( 10, 21,  10)),

                Box((-10, -90.0001, 13), (10, -79, 24)),
                Box((-5, -90.0002, 0), (-9, -79.00001, 15)),
                Box((-13, -90.0001, 4), (-23, -79, 24)),
                Box((-9, -90.0003, 22), (-14, -79, 18)),
            )
        ),
        wall_texture_1,
        translate=translate,
        rotate=rotate
    )
    return geomorph
