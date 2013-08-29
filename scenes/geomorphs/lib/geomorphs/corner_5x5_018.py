from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object, Cylinder
from pypov.pov import Union, Difference, Intersection
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def corner_5x5_018_info():
    return Metadata("Basic curved corner passage", "c18",
                    description="Basic curved corner corner",
                    block_type="corner",
                    bottom=0, top=20,
                    size="5x5",
                    repeatable=True,
                    fully_connected=True,
                    dead_ends=False,
                    entrance=False,
                    has_rooms=False,
                    passage_type="hewn",
                    wet=False,
                    multi_level=False,
                    keywords=['curved', 'boring', 'corner', 'halls', 'basic'])

def corner_5x5_018(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):

    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Box((-2.5, 10, -20), (  2.5, 21, -26)),
            Box((-20, 10, -2.5), (-26, 21,   2.5)),
            Intersection(
                Difference(
                    Cylinder((-20, 10.00001, -20), (-20, 21, -20), 22.5),
                    Cylinder((-20, 9, -20), (-20, 22, -20), 17.5),
                ),
                Box((3, 8, 3), (-20, 23, -20)),
            ),
            wall_texture_1,
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
