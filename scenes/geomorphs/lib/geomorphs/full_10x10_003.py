from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere, Merge

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import ten_by_ten
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1, white_plaster
from lib.textures import blue_plaster, brown_plaster
from lib.metadata import Metadata
from lib.util import float_range

def full_10x10_003_info():
    return Metadata("White Temple", "ff3",
            description="White columned temple",
            block_type="full",
            bottom=0, top=20,
            size="10x10",
            repeatable=False,
            fully_connected=False,
            dead_ends=True,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['INCOMPLETE', 'temple', 'white', 'complex', 'columns', 'multiple rooms'])

def full_10x10_003(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    #Box((-15, 8, -10), (15, 21, 36)), # columnade
    columns = Union()
    for x in range (-8, 33, 4):
        columns.append(Cylinder((-12, 8, x), (-12, 21, x), 1.0))
        columns.append(Cylinder((12, 8, x), (12, 21, x), 1.0))
        columns.append(Cylinder((-8, 8, x), (-8, 21, x), 1.0))
        columns.append(Cylinder((8, 8, x), (8, 21, x), 1.0))
        columns.append(Cylinder((-4, 8, x), (-4, 21, x), 1.0))
        columns.append(Cylinder((4, 8, x), (4, 21, x), 1.0))

    geomorph = Union(
        Difference(
            Merge(
                Object(ten_by_ten(), cross_hatch_texture),
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

                wall_texture_1,
            ),
            Union(
                Box((-14, 10, -28), (14, 21, -42)), # court one
                Box((-10, 9, -12), (10, 21, -26)), # court 2
                Box((-15, 8, -10), (15, 21, 36)), # columnade
                Box((-17, 9, -8), (-27, 21, 0)), # columnade side 1 rooms
                Box((-17, 9, 2), (-27, 21, 12)), # columnade side 1 rooms
                Box((-17, 9, 14), (-27, 21, 24)), # columnade side 1 rooms
                Box((-17, 9, 26), (-27, 21, 36)), # columnade side 1 rooms
                Box((17, 9, -8), (27, 21, 0)), # columnade side 2 rooms
                Box((17, 9, 2), (27, 21, 12)), # columnade side 2 rooms
                Box((17, 9, 14), (27, 21, 24)), # columnade side 2 rooms
                Box((17, 9, 26), (27, 21, 36)), # columnade side 1 rooms
                Box((-8, 7, 38), (8, 21, 47)), # inner sanctum
                Box((-10, 8, 38), (-20, 21, 45)), # side chambe 1
                Box((10, 8, 38), (20, 21, 45)), # side chambe 2
                white_plaster,
                rotate=(0, 11, 0),
            )
        ),
        Object(
            columns,
            white_plaster,
            rotate=(0, 11, 0),
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
