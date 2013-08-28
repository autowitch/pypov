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

    geomorph = Union(
        Difference(
            Merge(
                Object(ten_by_ten(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box((-22.5, 10.0001,  -48), (-27.5, 21, -51)),
                Box((22.5, 10.0002,  -48), (27.5, 21, -51)),
                Box((-40, 10.01, -22.5), (-51, 21, -27.5)),

                Box((40, 10.01, -22.5), (51, 21, -27.5)),
                Box((-40, 10.01, 22.5), (-51, 21, 27.5)),
                Box((40, 10.01, 22.5), (51, 21, 27.5)),


                # Sides

                Box((22.5, 10.01, 45), (27.5, 21, 51)),
                Box((-22.5, 10.01, 45), (-27.5, 21, 51)),

                # Rooms and non-temple passages

#                Box((22.50001, 10.0002, 10), (-22.50001, 21, 15)),

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
