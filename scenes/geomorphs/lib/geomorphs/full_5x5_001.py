from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Object
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def full_5x5_001_info():
    return Metadata("Basic four way intersection", "f1",
            description="Basic four way intersection",
            block_type="full",
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
            keywords=['basic', 'hallways', 'boring'])

def full_5x5_001(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Union(
                Box((-2.5, 10, 26), (    2.5, 21, -26), wall_texture_1),
                Box((26,   10.00002, -2.5), (-26,   21,   2.5), wall_texture_1),
            )
        ),
        Texture(
            Pigment(color=(0.025, 0.025, 0.025)),
            Finish(reflection=0.05)
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
