from lib.base import TenXTen

from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone
from pypov.pov import Union

from pypov.common import grey, white


def gm01(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1):
    """docstring for gm01"""
    geomorph = Union(
        Box((-100, -0, -100), (100, 50, 100), grey),
        Texture(
            Pigment(color=(0.025, 0.025, 0.025)),
            Finish(reflection=0.05)
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
