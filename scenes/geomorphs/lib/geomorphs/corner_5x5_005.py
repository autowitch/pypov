from lib.base import TenXTen

from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Cylinder
from pypov.pov import Union, Difference

from pypov.common import grey, white
from lib.base import five_by_five_corner, red


def corner_5x5_005(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            five_by_five_corner,
            Union(
                Box(( -5, 35, -5), (  5, 51, -26)),
                Box((  5, 35, -5.0001), (-26, 51,   5)),

                # Rooms
                Box(( 23, 35, 23), (  0, 51,   7)),
                Box(( -2, 35, 23), (-15, 51,   7)),

                # Doors
                Box((  0.1, 35, 14),  (-2.1, 45, 20)),
                Cylinder((0.1, 45, 17),  (-2.1, 45, 17), 3),

                Box((-13,   35, 4.9), (-7,   45,  7.1)),
                Cylinder((-10, 45, 4.9), (-10, 45, 7.1), 3),
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
