
from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner, cross_hatch, wall_texture_1, cross_hatch_2

from lib.metadata import Metadata
from lib.elements.stairways import circular_stairs

def corner_entrance_5x5_002_info():
    return Metadata("Corner with vertical entrance", "ce2",
            description="Corner with a sprial staircase leading to an entrance",
            block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=False, fully_connected=True,
            dead_ends=False, entrance=True, has_rooms=True,
            passage_type="hewn", wet=False)

def corner_entrance_5x5_002(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):

    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Object(five_by_five_corner, cross_hatch_texture),
            Union(
                Box(( -5, 10,  -5), (  5, 21, -26)),
                Box((  5.0001, 10,  -5), (-26, 21,   5)),
                Box((-20, 10.000001, -20), ( 20, 21,  20)),
                wall_texture_1
            )
        ),
        Object(
            circular_stairs(),
            Texture(wall_texture_1),
            translate=(0,10,0),
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph
