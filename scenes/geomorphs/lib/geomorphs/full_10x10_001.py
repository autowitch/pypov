from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere, Merge

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import ten_by_ten
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1, white_plaster
from lib.textures import blue_plaster, brown_plaster
from lib.metadata import Metadata

def full_10x10_001_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def full_10x10_001(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    spokes = Merge()
    columns = Union()
    angle = 45

    nicho_colors = [
            Colors.Gray20,
            Colors.Red,
            Colors.Orange,
            Colors.Yellow,
            Colors.Green,
            Colors.Blue,
            Colors.Violet,
            Colors.Gray90,
    ]

    for x in range(0, 8):
        # Halls
        spokes.append(Box((21, 10.0001, -2.5), (31, 21, 2.5),
            rotate=(0, x* angle + 10, 0)))

        # Doors
        spokes.append(Box((19, 10.0001, -2), (33, 15, 2),
            rotate=(0, x* angle + 10, 0)))
        spokes.append(Intersection(
            Cylinder((19, 15, -2), (33, 15, -2), 4),
            Cylinder((19, 15, 2), (33, 15, 2), 4),
            rotate=(0, x* angle + 10, 0)
            )
        )

        # Steps
        spokes.append(Box((19, 6, -2.0001), (22, 12, 2.0001),
            rotate=(0, x* angle + 10, 0)))
        spokes.append(Box((19, 7, -2.0002), (23, 12, 2.0002),
            rotate=(0, x* angle + 10, 0)))
        spokes.append(Box((19, 8, -2.0003), (24, 12, 2.0003),
            rotate=(0, x* angle + 10, 0)))
        spokes.append(Box((19, 9, -2.0004), (25, 12, 2.0004),
            rotate=(0, x* angle + 10, 0)))

        # Inner Nichos
        spokes.append(Cylinder((19.9, 7, 0), (19.9, 14, 0), 2.5,
                Pigment(color=nicho_colors[x]),
                rotate=(0, x * angle + 32.5, 0)))
        spokes.append(Sphere((19.9, 14, 0), 2.5,
                Pigment(color=nicho_colors[x]),
                rotate=(0, x * angle + 32.5, 0)))

        # Outer Nichos

        spokes.append(Cylinder((37.9, 11, 0), (37.9, 15, 0), 2.5,
                Pigment(color=nicho_colors[x]),
                rotate=(0, x * angle + 32.5, 0)))
        spokes.append(Sphere((37.9, 15, 0), 2.5,
                Pigment(color=nicho_colors[x]),
                rotate=(0, x * angle + 32.5, 0)))

        spokes.append(Cylinder((32.1, 11, 0), (32.1, 15, 0), 2.5,
                Pigment(color=nicho_colors[x]),
                rotate=(0, x * angle + 32.5, 0)))
        spokes.append(Sphere((32.1, 15, 0), 2.5,
                Pigment(color=nicho_colors[x]),
                rotate=(0, x * angle + 32.5, 0)))

        # Columns
        columns.append(Cylinder((14, 5, 0), (14, 27, 0), 1.5,
            rotate=(0, x * angle + 10, 0)))
        columns.append(Cylinder((14, 5, 0), (14, 6.5, 0), 2,
            rotate=(0, x * angle + 10, 0)))
        columns.append(Cylinder((14, 27, 0), (14, 28, 0), 2,
            rotate=(0, x * angle + 10, 0)))

    spokes.append(white_plaster)

    geomorph = Union(
        Difference(
            Union(
                Object(ten_by_ten(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Cylinder((0, 5, 0), (0, 21, 0), 20),
                Difference(
                    Cylinder((0, 10, 0), (0, 21, 0), 38),
                    Cylinder((0, 10, 0), (0, 21, 0), 32),
                ),
                Difference(
                    Cylinder((0, 10.0002, 0), (0, 11, 0), 38.00001),
                    Cylinder((0, 10.0002, 0), (0, 11, 0), 31.99999),
                    brown_plaster
                ),
                Difference(
                    Cylinder((0, 19, 0), (0, 21, 0), 38.00001),
                    Cylinder((0, 19, 0), (0, 21, 0), 31.99999),
                    blue_plaster
                ),
#                Box(( -22.5, 10.0001,  2.50001), ( -27.5, 21, -51)),
#                Box((  22.5, 10.0002,  2.50001), (  27.5, 21, -51)),
                spokes,
                white_plaster
            ),
            Union(
                # Halls
                # Ends
                Box((-40, 10.01, -22.5), (-51, 21, -27.5)),
                Box((-40.00001, 10.000001, -27.49999), (-45.00001, 21, -33)),

                Box((40, 10.01, -22.5), (51, 21, -27.5)),
                Box((-40, 10.01, 22.5), (-51, 21, 27.5)),
                Box((40, 10.01, 22.5), (51, 21, 27.5)),

                Box((34, 10.0001, -36), (47, 21, -49)),
                Box((35, 10.0002, -40.0001), (22, 21, -44)),
                Box((45.0001, 10.0002, -25), (41.0001, 21, -38)),

                Box((36, 10.0002, 21), (48, 21, 45)),

                # Sides
                Box((22.5, 10.01, -40), (27.5, 21, -51)),
                Box((21, 10.0001, -34), (31, 21, -44)),
                Box((-8, 11, -1.5), (5, 21, 1.5),
                    rotate=(0, 70, 0),
                    translate=(40, 0, 12),
                ),

                Box((-22.5, 10.01, -40), (-27.5, 21, -51)),
                Box((-27.49999, 10.0001, -40.0001), (-33, 21, -45.0001)),

                Box((22.5, 10.01, 45), (27.5, 21, 51)),
                Box((-22.5, 10.01, 45), (-27.5, 21, 51)),
                Box((-27.49999, 10, 45.0001), (27.49999, 21, 40.00001)),
                Box((-2, 11, 41), (-5, 21, 35)),
                # Rooms
                Box((-48, 10, -48), (-32, 21, -32)),

                Box((-48, 10.0001, 48), (-38, 21, 20)),
                Box((-12, 11, -1.5), (10, 21, 1.5),
                    rotate=(0, 30, 0),
                    translate=(-42, 0, 15),
                ),
                wall_texture_1,
            ),
        ),
        Object(
            columns,
            white_plaster,
#            Texture(Pigment(color=Colors.Tan)),
        ),
        Union(
            Cylinder((39, 10, 42), (39, 21, 42), 1),
            Cylinder((45, 10, 42), (45, 21, 42), 1),

            Cylinder((39, 10, 32), (39, 21, 32), 1),
            Cylinder((45, 10, 32), (45, 21, 32), 1),
            Texture(Pigment(color=Colors.Tan)),
#                Box((36, 10.0002, 21), (48, 21, 45)),
        ),
        Difference(
            Cylinder((0, 28, 0), (0, 30, 0), 16.25),
            Cylinder((0, 27, 0), (0, 31, 0), 11.75),
            white_plaster,
#            Texture(Pigment(color=Colors.Tan)),
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
