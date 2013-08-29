from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object, Cylinder
from pypov.pov import Union, Difference, Intersection
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def corner_5x5_020_info():
    return Metadata("very curved corner passage with room", "c20",
                    description="Very curved corner corner with room",
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
                    keywords=['curved', 'round', 'boring', 'corner', 'halls', 'basic'])

def corner_5x5_020(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):

    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Box((-2.5, 10, -20), (  2.5, 21, -26)),
            Box((-20, 10, -2.5), (-26, 21,   2.5)),
            Difference(
                Cylinder((0, 10.00001, 0), (0, 21, 0), 22.5),
                Cylinder((0, 9, 0), (0, 22, 0), 17.5),
                Box((-2.249999, 8, -2.24999), (-23, 23, -23)),
            ),
            Cylinder((0, 10.00002, 0), (0, 21, 0), 12),
            Box((-2.5, 10.00003, 10), (2.5, 21, 19), "rotate <0, 45, 0>"),
            wall_texture_1,
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
