from lib.base import TenXTen

from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Cylinder
from pypov.pov import Union, Difference

from pypov.common import grey, white
from lib.base import five_by_five_corner, red


def corner_5x5_003(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1):
    """docstring for gm02"""

    geomorph = Union(
        Difference(
            five_by_five_corner,
            Union(
                Box(( -5, 35,  -5), (  5, 51, -26)),
                Box((  5, 35,  -5), (-26, 51,   5)),
                Box((-20, 35.00001, -20), ( 20, 51,  20)),
            )
        ),
        Union(
            Cylinder((-15, 35, -15), (-15, 50, -15), 2),
            Cylinder(( 15, 35, -15), ( 15, 50, -15), 2),
            Cylinder((-15, 35,  15), (-15, 50,  15), 2),
            Cylinder(( 15, 35,  15), ( 15, 50,  15), 2),

            Cylinder((-15, 35, -15), (-15, 36, -15), 3),
            Cylinder(( 15, 35, -15), ( 15, 36, -15), 3),
            Cylinder((-15, 35,  15), (-15, 36,  15), 3),
            Cylinder(( 15, 35,  15), ( 15, 36,  15), 3),
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
