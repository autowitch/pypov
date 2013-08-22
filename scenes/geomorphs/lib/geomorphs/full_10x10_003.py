from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere, Merge

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import ten_by_ten
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1, white_plaster
from lib.textures import blue_plaster, brown_plaster
from lib.metadata import Metadata
from lib.util import float_range

def full_10x10_002_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def full_10x10_002(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""


    columns = Union()
    for x in float_range(-25, 25, 2.5):
        print x

    geomorph = Union(
        Difference(
            Merge(
                Object(ten_by_ten(), cross_hatch_texture),
                Box((-26, -10, 33), (26, 0, -18)),
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001,  -48), ( -27.5, 21, -51)),
                Box((  22.5, 10.0002,  -48), (  27.5, 21, -51)),
                Box((-40, 10.01, -22.5), (-51, 21, -27.5)),

                Box((40, 10.01, -22.5), (51, 21, -27.5)),
                Box((-40, 10.01, 22.5), (-51, 21, 27.5)),
                Box((40, 10.01, 22.5), (51, 21, 27.5)),


                # Sides

                Box((22.5, 10.01, 45), (27.5, 21, 51)),
                Box((-22.5, 10.01, 45), (-27.5, 21, 51)),

                # Pool
                Box((-25, -5, 32), (25, 21, -17)),
                wall_texture_1,
            ),
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
