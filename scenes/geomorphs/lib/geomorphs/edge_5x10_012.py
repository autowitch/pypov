from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_010_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def edge_5x10_010(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001,  -20), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002,  -20), (  27.5, 21, -26)),
                Box((  -51, 10,  -2.5), (-45, 21,   2.5)),
                Box((  51, 10,  -2.5), (45, 21,   2.5)),


                Box((  -45.0001, 10.0001,  -20), (45, 21,   -15)),
                Box((  -45.0002, 10.0001,  -20.001), (-40, 21,   2.50001)),
                Box((  45.0002, 10.0001,  -20.001), (40, 21,   2.50001)),
                wall_texture_1
            ),
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
