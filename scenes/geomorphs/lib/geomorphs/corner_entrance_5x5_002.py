
from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner, cross_hatch, wall_texture_1

from lib.metadata import Metadata

def corner_entrance_5x5_005_info():
    return Metadata("Corner with vertical entrance", "ce2",
            description="Corner with a sprial staircase leading to an entrance",
            block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=False, fully_connected=True,
            dead_ends=False, entrance=True, has_rooms=True,
            passage_type="hewn", wet=False)
