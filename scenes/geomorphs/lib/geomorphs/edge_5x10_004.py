from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_004_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def edge_5x10_004(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    rooms = Union()
    start = -40
    for x in range(0, 7):
        rooms.append(Box((start - 5, 12, 4.5), (start + 5, 21, 19)))
        rooms.append(Box((start - 1.5, 11, 2), (start + 1.5, 18, 5)))
        print start
        start += 12

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001, -10), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002, -10), (  27.5, 21, -26)),
                Box(( -51,   10,       -2.5), (51,   21,   2.5)),
                Box(( -27.5, 10,      -10.0), (27.5, 21,  -5.0)),
                rooms,
                Box((-46, 10, -22), (-30, 21, -8)),
                Box((-25, 10.0003, -20), (-31, 21, -16)),
                wall_texture_1
            ),
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph