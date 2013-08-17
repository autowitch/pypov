from lib.base import TenXTen

from pypov.pov import Texture, Pigment
from pypov.pov import Union, Difference, Object, Box

from pypov.common import grey, white
from lib.base import five_by_five_corner, cross_hatch
from lib.metadata import Metadata

def corner_5x5_002_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def corner_5x5_002(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Object(five_by_five_corner, cross_hatch),
            Union(
                Box(( -5, 10,  -5), (  5, 21, -26)),
                Box((  5.0001, 10,  -5), (-26, 21,   5)),
                Box((-20, 10.000001, -20), ( 20, 21,  20)),
            )
        ),
        Texture(
            Pigment(color=(0.5, 0.45, 0.25)),
            #Pigment(color=(0.025, 0.025, 0.025)),
            #Finish(reflection=0.05)
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
