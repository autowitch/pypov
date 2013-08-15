from lib.base import TenXTen

from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone
from pypov.pov import Union, Difference

from pypov.common import grey, white
from lib.base import five_by_five_corner, red


def corner_5x5_004(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            five_by_five_corner,
            Union(
                Box(( -5, 35,  -5), (  5, 51, -26)),
                Box((  5, 35,  -5), (-26, 51,   5)),
                Box((-20, 35.00001, -20), ( 20, 51,  20)),
                Box((-19, 25, -19), ( 19, 51,  19)),
                Box((-18, 15, -18), ( 18, 51,  18)),
                Box((-17,  1, -17), ( 17, 51,  17)),
            )
        ),
        Texture(
            Pigment(color=(0.5, 0.45, 0.25)),
            #Pigment(color=(0.025, 0.025, 0.025)),
            #Finish(reflection=0.05)
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
