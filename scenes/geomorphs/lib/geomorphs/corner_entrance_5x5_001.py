from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner, cross_hatch, wall_texture_1

from lib.metadata import Metadata

def corner_5x5_entrance_005_info():
    return Metadata("Corner with horizontal entrance", "ce1",
            description="Corner with passage extending to an entrance",
            block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=False, fully_connected=False,
            dead_ends=True, entrance=True, has_rooms=True,
            passage_type="hewn", wet=False)
