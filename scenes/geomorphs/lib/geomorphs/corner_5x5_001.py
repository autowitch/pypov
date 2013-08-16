from lib.base import TenXTen

from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner, cross_hatch


def corner_5x5_001(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Object(five_by_five_corner, cross_hatch),
            Box((-5, 10, -5), (  5, 21, -26), Pigment(color=Colors.Red)),
            Box(( 5, 10, -5), (-26, 21,   5), Pigment(color=Colors.Red)),
        ),
        Texture(
            Pigment(color=(0.025, 0.025, 0.025)),
            Finish(reflection=0.05)
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
