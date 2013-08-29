from pypov.pov import Texture, Pigment, Intersection, Cylinder, Torus
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
            fully_connected=True,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['temple', 'white', 'complex', 'columns', 'multiple rooms'])

def full_10x10_003(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    #Box((-15, 8, -10), (15, 21, 36)), # columnade
    columns = Union()
    for x in range (-4, 33, 8):
        columns.append(Cylinder((-11, 8, x), (-11, 21, x), 1.0))
        columns.append(Cylinder((11, 8, x), (11, 21, x), 1.0))
        columns.append(Cylinder((-5, 8, x), (-5, 21, x), 1.0))
        columns.append(Cylinder((5, 8, x), (5, 21, x), 1.0))

        columns.append(Cylinder((-11, 8, x), (-11, 8.5, x), 1.25))
        columns.append(Cylinder((11, 8, x), (11, 8.5, x), 1.25))
        columns.append(Cylinder((-5, 8, x), (-5, 8.5, x), 1.25))
        columns.append(Cylinder((5, 8, x), (5, 8.5, x), 1.25))

        columns.append(Torus(1.0, 0.15, "translate <-11, 8.5, %s>" % x, brown_plaster))
        columns.append(Torus(1.0, 0.15, "translate <-11, 20, %s>" % x, brown_plaster))
        columns.append(Torus(1.0, 0.15, "translate <-11, 21, %s>" % x, brown_plaster))

        columns.append(Torus(1.0, 0.15, "translate <11, 8.5, %s>" % x, brown_plaster))
        columns.append(Torus(1.0, 0.15, "translate <11, 20, %s>" % x, brown_plaster))
        columns.append(Torus(1.0, 0.15, "translate <11, 21, %s>" % x, brown_plaster))

        columns.append(Torus(1.0, 0.15, "translate <-5, 8.5, %s>" % x, brown_plaster))
        columns.append(Torus(1.0, 0.15, "translate <-5, 20, %s>" % x, brown_plaster))
        columns.append(Torus(1.0, 0.15, "translate <-5, 21, %s>" % x, brown_plaster))

        columns.append(Torus(1.0, 0.15, "translate <5, 8.5, %s>" % x, brown_plaster))
        columns.append(Torus(1.0, 0.15, "translate <5, 20, %s>" % x, brown_plaster))
        columns.append(Torus(1.0, 0.15, "translate <5, 21, %s>" % x, brown_plaster))

        columns.append(
            Difference(
                Cylinder((-11, 21, x), (-11, 22.5, x), 1.5),
                Torus(1.5, 0.5001, "scale <1, 2, 1> translate <-11, 21, %s>" % x, blue_plaster),
            )
        )

        columns.append(
            Difference(
                Cylinder((11, 21, x), (11, 22.5, x), 1.5),
                Torus(1.5, 0.5001, "scale <1, 2, 1> translate <11, 21, %s>" % x, blue_plaster),
            )
        )
        columns.append(
            Difference(
                Cylinder((-5, 21, x), (-5, 22.5, x), 1.5),
                Torus(1.5, 0.5001, "scale <1, 2, 1> translate <-5, 21, %s>" % x, blue_plaster),
            )
        )
        columns.append(
            Difference(
                Cylinder((5, 21, x), (5, 22.5, x), 1.5),
                Torus(1.5, 0.5001, "scale <1, 2, 1> translate <5, 21, %s>" % x, blue_plaster),
            )
        )

    columns.append(Cylinder((-7, 9, -15), (-7, 20, -15), 0.75))
    columns.append(Cylinder((-7, 9, -23), (-7, 20, -23), 0.75))
    columns.append(Cylinder((7, 9, -15), (7, 20, -15), 0.75))
    columns.append(Cylinder((7, 9, -23), (7, 20, -23), 0.75))

    columns.append(Cylinder((-7, 9, -15), (-7, 9.5, -15), 1))
    columns.append(Cylinder((-7, 9, -23), (-7, 9.5, -23), 1))
    columns.append(Cylinder((7, 9, -15), (7, 9.5, -15), 1))
    columns.append(Cylinder((7, 9, -23), (7, 9.5, -23), 1))

    columns.append(Cylinder((-7, 19.5, -15), (-7, 20.001, -15), 1))
    columns.append(Cylinder((-7, 19.5, -23), (-7, 20.001, -23), 1))
    columns.append(Cylinder((7, 19.5, -15), (7, 20.001, -15), 1))
    columns.append(Cylinder((7, 19.5, -23), (7, 20.001, -23), 1))

    geomorph = Union(
        Difference(
            Merge(
                Object(ten_by_ten(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box((-22.5, 10.0001,  -40), (-27.5, 21, -51)),
                Box((-27.4999, 10.0003,  -40), (-35, 21, -45)),
                Box((22.5, 10.0002,  -40), (27.5, 21, -51)),
                Box((-37, 10.01, -22.5), (-51, 21, -27.5)),

                Box((40, 10.01, -22.5), (51, 21, -27.5)),
                Box((-30, 10.01, 22.5), (-51, 21, 27.5)),
                Box((40, 10.01, 22.5), (51, 21, 27.5)),

                # Sides

                Box((22.5, 10.01, 45), (27.5, 21, 51)),
                Box((-22.5, 10.01, 45), (-27.5, 21, 51)),

                # Rooms and non-temple passages

                Box((45, 10.0002, -22.50001), (40, 21, 35)),
                Box((48, 10.0002, 37), (35, 21, 47)),
                Box((41, 10.0001, 34), (44, 18, 38)),

                Box((-40, 10, 48), (-29, 21, 29)),
                Box((-45, 10, 20), (-30, 21, 0)),
                Box((-35, 10.00003, 30), (-39, 18, 18)),
                Box((-38, 10.00001, 1), (-34, 21, -28)),
                Box((-35, 10, 45.0001), (-22.50001, 21, 40)),

                wall_texture_1,
            ),
            Union(
                Box((-14, 10, -28), (14, 21, -42)),    # court one
                Box((-10, 9, -12), (10, 21, -26)),     # court 2
                Box((-15, 8, -10), (15, 21, 36)),      # columnade
                Box((-17, 9, -10), (-27, 21, 0)),      # columnade side 1 rooms
                Box((-17, 9, 2), (-27, 21, 12)),       # columnade side 1 rooms
                Box((-17, 9, 14), (-27, 21, 24)),      # columnade side 1 rooms
                Box((-17, 9, 26), (-27, 21, 36)),      # columnade side 1 rooms
                Box((17, 9, -10), (27, 21, 0)),        # columnade side 2 rooms
                Box((17, 9, 2), (27, 21, 12)),         # columnade side 2 rooms
                Box((17, 9, 14), (27, 21, 24)),        # columnade side 2 rooms
                Box((17, 9, 26), (27, 21, 36)),        # columnade side 1 rooms
                Box((-8, 7, 38), (8, 21, 47)),         # inner sanctum
                Box((-10, 8, 38), (-20, 21, 45)),      # side chamber 1
                Box((10, 8, 38), (20, 21, 45)),        # side chamber 2

                # Entry chambers
                Union(
                    Box((16, 10, -38), (40, 21, -25)),
                    Box((-17, 10.00001, -30), (17, 18, -34)),

                    Box((-16, 10, -40), (-35, 21, -25)),
                    Box((-22, 10, -42), (-35, 21, -52)),
                    Box((-33, 10.0001, -39), (-28, 17, -43)),
                    wall_texture_1
                ),

                # Doors - axial
                Box((-4, 10.0001, -25), (4, 18, -29)),
                Box((-4, 9.0001, -9), (4, 18, -13)),
                Box((-3, 8.0001, 35), (3, 18, 39)),

                # Doors - Columnade side rooms
                Box((-14, 9.00001, -3), (-18, 16, -7)),
                Box((-14, 9.00001, 5), (-18, 16, 9)),
                Box((-14, 9.00001, 17), (-18, 16, 21)),
                Box((-14, 9.00001, 29), (-18, 16, 33)),

                Box((14, 9.00001, -3), (18, 16, -7)),
                Box((14, 9.00001, 5), (18, 16, 9)),
                Box((14, 9.00001, 17), (18, 16, 21)),
                Box((14, 9.00001, 29), (18, 16, 33)),

                # Side chambers
                Box((-7, 8.0001, 40), (-11, 16, 43)),
                Box((7, 8.0001, 40), (11, 16, 43)),

                # Back hallway
                Box((14, 12, 44), (16, 21, 51), wall_texture_1),

                white_plaster,
                rotate=(0, 11, 0),
            ),
            Box((-10, 12, -1.5), (10, 21, 1.5), "rotate <0, -30, 0> translate <35, 0, -27>", wall_texture_1),
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

