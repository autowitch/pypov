from pypov.pov import Texture, Pigment, Object, Cylinder, Merge
from pypov.pov import Finish, Box, Cone, Sphere
from pypov.pov import Union, Difference
from pypov.colors import Colors

from lib.base import five_by_five_corner
from lib.textures import cross_hatch_2, wall_texture_1
from lib.metadata import Metadata
from lib.util import float_range


def corner_5x5_011_info():
    return Metadata("Basic roundish room with pillars", "c11",
            description="Basic roundish room with pillars",
            block_type="corner",
            bottom=0, top=20,
            size="5x5",
            repeatable=True,
            fully_connected=True,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['roundish', 'room', 'columns', 'basic'])

def corner_5x5_011(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Union(
                Box((-2.5, 10, -9), (  2.5, 21, -26)),
                Box(( -9, 10, -2.5), (-26, 21,   2.5)),


                Box((-8, 10.00001, -12), (8, 21, 12)),
                Box((-12, 10.00002, -8), (12, 21, 8)),
                Cylinder((-8, 10.0003, -8), (-8, 21, -8), 4),
                Cylinder((8, 10.0003, -8), (8, 21, -8), 4),
                Cylinder((-8, 10.0003, 8), (-8, 21, 8), 4),
                Cylinder((8, 10.0003, 8), (8, 21, 8), 4),
                wall_texture_1
            ),
        ),
        Union(
            Cylinder((6, 10, 6), (6, 20, 6), 2),
            Cylinder((-6, 10, 6), (-6, 20, 6), 2),
            Cylinder((6, 10, -6), (6, 20, -6), 2),
            Cylinder((-6, 10, -6), (-6, 20, -6), 2),
            wall_texture_1,
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph












