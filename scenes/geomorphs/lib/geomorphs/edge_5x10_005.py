from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere, Isosurface

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_005_info():
    return Metadata("More cells", "e5",
            description="More cells",
            block_type="edge",
            bottom=0, top=20,
            size="5x10",
            repeatable=False,
            fully_connected=False,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['cells', 'side chambers', 'multiple rooms', 'secret passage'])

def edge_5x10_005(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    rooms = Union()
    start = -40
    for x in range(0, 7):
        rooms.append(Box((start - 5, 12, 4.5), (start + 5, 21, 16)))
        rooms.append(Box((start - 5, 12, -4.5), (start + 5, 21, -16)))
        rooms.append(Box((start - 1.5, 11, -5), (start + 1.5, 18, 5)))
        print start
        start += 12

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001, -20), ( -27.5, 21, -26)),

                Box(( -51,   10,       -2.5), (37,   21,   2.5)),
                Box((  39,   10,       -2.5), (51,   21,   2.5)),

                Box((  39,   10.00001, 0),    (44,   21,   -24)),
                Box((  39.0001, 10.00003, -23.9999), (25, 21, -19)),
                Box((  22.5, 10.0002, -19.0001), (  27.5, 21, -26)),
                rooms,
                wall_texture_1
            ),
            Object(
                #                Box((-10, 0, -10), (20, 21, 20),
                Isosurface("function  { f_rounded_box (x, y, z, 0.15, 0.75, 2, 3 ) - " +
                    "f_ridged_mf(x / 10, y / 15, z / 10, 1, 0.5, 0.5, 1.2, 1, 2) * 2 - " +
                    "fn_Pigm(x, y, z).gray*0.05 } " +
                    "contained_by { box { <-50, -5, -25>, <50, 21, 25> } } " +
                    "max_gradient 10 " +
                    "all_intersections ",
                    translate=(-26, 17, -18.5),
                    rotate=(0, 0, 0),
                ),
                Pigment(color=Colors.Tan),
            ),
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph
