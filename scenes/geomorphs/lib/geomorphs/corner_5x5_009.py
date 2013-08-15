from lib.base import TenXTen

from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone
from pypov.pov import Union, Difference

from pypov.common import grey, white
from lib.base import five_by_five_corner, red


def corner_5x5_009(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            five_by_five_corner,
            Box((-5, 35, -5), (  5, 51, -26), red),
            Box(( 5, 35, -5), (-26, 51,   5), red),
        ),
        Texture(
            Pigment(color=(0.025, 0.025, 0.025)),
            Finish(reflection=0.05)
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
