from pypov.pov import Texture, Pigment, Object, Cylinder, Merge
from pypov.pov import Finish, Box, Cone, Sphere
from pypov.pov import Union, Difference
from pypov.colors import Colors

from lib.base import five_by_five_corner
from lib.textures import cross_hatch_2, wall_texture_1
from lib.metadata import Metadata
from lib.util import float_range


def corner_5x5_008_info():
    return Metadata("Basic four entrance room", "f2",
            description="Basic four entrance room", block_type="normal",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def corner_5x5_008(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Union(
                Box((-2.5, 10, -9), (  2.5, 21, -26)),
                Box(( -9, 10, -2.5), (-26, 21,   2.5)),


                Box((-10, 10.00001, -10), (10, 21, 10)),
                wall_texture_1
            ),
        ),
        Merge(
            Box((-2, 10, -5), (2, 11, 5)),
            Box((-2, 11, -4), (2, 12, 5)),
            Box((-2, 12, -3), (2, 13, 5)),
            Box((-2, 13, -2), (2, 14, 5)),
            Box((-2, 14, -1), (2, 15, 5)),
            Box((-2, 15, 0), (2, 16, 5)),
            Box((-2, 16, 1), (2, 17, 5)),
            Box((-2, 17, 2), (2, 18, 5)),
            Box((-2, 22, 3), (2, 18, 5)),
            Pigment(color=Colors.Tan),
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph




