from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object, Cylinder
from pypov.pov import Union, Difference, Intersection
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def full_5x5_014_info():
    return Metadata("Circular intersection with room", "f14",
                    description="Circular intersection with room",
                    block_type="full",
                    bottom=0, top=20,
                    size="5x5",
                    repeatable=True,
                    fully_connected=False,
                    dead_ends=False,
                    entrance=False,
                    has_rooms=True,
                    passage_type="hewn",
                    wet=False,
                    multi_level=False,
                    keywords=['curved', 'round', 'halls', 'basic'])

def full_5x5_014(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):

    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Box((-2.5, 10, -20), (  2.5, 21, -26)),
            Box((-2.5, 10, 20), (  2.5, 21, 26)),
            Box((-20, 10, -2.5), (-26, 21,   2.5)),
            Box((20, 10, -2.5), (26, 21,   2.5)),
            Difference(
                Cylinder((0, 10.00001, 0), (0, 21, 0), 21),
                Cylinder((0, 9, 0), (0, 22, 0), 16),
            ),
            Cylinder((0, 10, 0), (0, 21, 0), 12),
            Box((-2.5, 10.00002, -18), (2.5, 21, 18), "rotate <0, 45, 0>"),
            Box((-2.5, 10.00002, -18), (2.5, 21, 18), "rotate <0, -45, 0>"),
            wall_texture_1,
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
