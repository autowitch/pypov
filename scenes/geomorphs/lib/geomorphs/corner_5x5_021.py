from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object, Cylinder
from pypov.pov import Union, Difference, Intersection
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def corner_5x5_021_info():
    return Metadata("very curved corner passage with room and pit", "c21",
                    description="Very curved corner corner with room and pit",
                    block_type="corner",
                    bottom=-100, top=20,
                    size="5x5",
                    repeatable=True,
                    fully_connected=True,
                    dead_ends=False,
                    entrance=False,
                    has_rooms=True,
                    passage_type="hewn",
                    wet=False,
                    multi_level=False,
                    keywords=['pit', 'round', 'curved', 'boring', 'corner', 'halls', 'basic'])

def corner_5x5_021(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):

    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_five_corner()),
                Cone((0, 0, 0), 10, (0, -100, 0), 6),
                Box((4, -75, 4), (24, -65, 24)),
                cross_hatch_texture
            ),
            Box((-2.5, 10, -20), (  2.5, 21, -26)),
            Box((-20, 10, -2.5), (-26, 21,   2.5)),
            Difference(
                Cylinder((0, 10.00001, 0), (0, 21, 0), 22.5),
                Cylinder((0, 9, 0), (0, 22, 0), 17.5),
                Box((-2.249999, 8, -2.24999), (-23, 23, -23)),
            ),
            Cylinder((0, 10.00002, 0), (0, 21, 0), 12),
            Box((-2.5, 10.00003, 10), (2.5, 21, 19), "rotate <0, 45, 0>"),

            Cone((0, 10.5, 0), 8, (0, -98, 0), 4),
            Box((6, -74, 6), (22, -64, 22)),
            Box((-3, -64.0001, 3), (3, -75.001, 12), "rotate <0, 45, 0>"),
            Cylinder((0, -64, 0), (12, -64, 12), 3),

            wall_texture_1,
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
