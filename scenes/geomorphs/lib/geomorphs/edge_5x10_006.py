from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_006_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def edge_5x10_006(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    columns = Union()
    for x in range(-25, 35, 5):
        columns.append(Cylinder((x, 10, 9), (x, 20, 9), 1))
        columns.append(Cylinder((x, 10, 17), (x, 20, 17), 1))

    columns2 = Union()
    for x in range(-10, 15, 5):
        columns2.append(Cylinder((x, 10, -4), (x, 20, -4), 1.25))
        columns2.append(Cylinder((x, 10, -15), (x, 20, -15), 1.25))

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001,  -12), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002,  2.50001), (  27.5, 21, -26)),
                Box((  22.50001, 10.0004,  -2.5), (51, 21,   2.5)),

                # End hall
                Box((  -51, 10,  -2.5), (-35, 21,   2.5)),
                # Two end rooms
                Union(
                    Box((-30, 10, 6), (35, 21, 20)),

                    Box((-32, 10, 10), (-41, 21, 16)),
                    Box((-41.001, 10.0001, 10.0001), (-36, 21, 4)),
                    Box((-33, 10.0002, 11), (-29, 18, 15)),

                    Box((37, 10, 10), (46, 21, 16)),
                    Box((38, 10, 11), (34, 18, 15)),
                    Box((46.001, 10.0001, 10.0001), (41, 21, -2)),
                    wall_texture_1,
                    rotate=(0, -5, 0)
                ),

                # Stepped floor room
                Box((-45, 9, -8), (-30, 21, -23)),
                Box((-43, 8, -10), (-32, 21, -21)),
                Box((-41, 7, -12), (-34, 21, -19)),
                Box((-43, 10.0002, 0), (-38, 21, -6)),
                Box((-42, 10.0003, 0), (-39, 18, -9)),

                # Secondary column room
                Box(( -27.5, 10.0004, -11), (25, 18, -8)),
                Box(( -27.5, 10.0003, -12), (-17, 21, -7)),
                Box(( 17, 10.0003, -12), (25, 21, -7)),
                Box(( -15, 10, 0), (15, 21, -19)),

                wall_texture_1,
            ),
        ),
        Object(columns, wall_texture_1,  rotate=(0, -5, 0)),
        Object(columns2, wall_texture_1),
        translate=translate,
        rotate=rotate
    )
    return geomorph
