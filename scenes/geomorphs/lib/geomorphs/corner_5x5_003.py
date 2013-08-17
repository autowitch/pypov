from lib.base import TenXTen

from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Cylinder, Object
from pypov.pov import Union, Difference

from pypov.common import grey, white
from lib.base import five_by_five_corner, cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def corner_5x5_003_info():
    return Metadata("Basic corner room", "c3",
            description="Basic boring corner with a room. This one has columns. Yay!",
            block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def corner_5x5_003(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Object(five_by_five_corner, cross_hatch_texture),
            Union(
                Box(( -5, 10,  -5), (  5, 21, -26)),
                Box((  5, 10,  -5), (-26, 21,   5)),
                Box((-20, 10.00001, -20), ( 20, 21,  20)),
                wall_texture_1
            )
        ),
        Union(
            Cylinder((-10, 10, -10), (-10, 20, -10), 2),
            Cylinder(( 10, 10, -10), ( 10, 20, -10), 2),
            Cylinder((-10, 10,  10), (-10, 20,  10), 2),
            Cylinder(( 10, 10,  10), ( 10, 20,  10), 2),

            Cylinder((-10, 10, -10), (-10, 11, -10), 3),
            Cylinder(( 10, 10, -10), ( 10, 11, -10), 3),
            Cylinder((-10, 10,  10), (-10, 11,  10), 3),
            Cylinder(( 10, 10,  10), ( 10, 11,  10), 3),
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
