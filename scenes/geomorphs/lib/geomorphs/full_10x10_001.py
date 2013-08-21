from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere, Merge

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import ten_by_ten
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
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
    for x in range(0, 8):
        # Halls
        spokes.append(Box((21, 10.0001, -2.5), (31, 21, 2.5),
            rotate=(0, x* angle + 10, 0)))

        # Doors
        spokes.append(Box((19, 10.0001, -2), (33, 16, 2),
            rotate=(0, x* angle + 10, 0)))
        spokes.append(Intersection(
            Cylinder((19, 16, -2), (33, 16, -2), 4),
            Cylinder((19, 16, 2), (33, 16, 2), 4),
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

        # Nichos
        spokes.append(Cylinder((19.9, 7, 0), (19.9, 14, 0), 2.5,
                rotate=(0, x * angle + 32.5, 0)))
        spokes.append(Sphere((19.9, 14, 0), 2.5,
                rotate=(0, x * angle + 32.5, 0)))

        # Columns
        columns.append(Cylinder((14, 5, 0), (14, 27, 0), 1.5,
            rotate=(0, x * angle + 10, 0)))
        columns.append(Cylinder((14, 5, 0), (14, 6.5, 0), 2,
            rotate=(0, x * angle + 10, 0)))
        columns.append(Cylinder((14, 27, 0), (14, 28, 0), 2,
            rotate=(0, x * angle + 10, 0)))

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
#                Box(( -22.5, 10.0001,  2.50001), ( -27.5, 21, -51)),
#                Box((  22.5, 10.0002,  2.50001), (  27.5, 21, -51)),
                spokes,

                # Halls
                # Ends
                Box((-40, 10.01, -22.5), (-51, 21, -27.5)),
                Box((-40.00001, 10.000001, -27.49999), (-45.00001, 21, -33)),

                Box((40, 10.01, -22.5), (51, 21, -27.5)),
                Box((-40, 10.01, 22.5), (-51, 21, 27.5)),
                Box((40, 10.01, 22.5), (51, 21, 27.5)),

                # Sides
                Box((22.5, 10.01, -40), (27.5, 21, -51)),

                Box((-22.5, 10.01, -40), (-27.5, 21, -51)),
                Box((-27.49999, 10.0001, -40.0001), (-33, 21, -45.0001)),

                Box((22.5, 10.01, 45), (27.5, 21, 51)),
                Box((-22.5, 10.01, 45), (-27.5, 21, 51)),
                Box((-27.49999, 10, 45.0001), (27.49999, 21, 40.00001)),

                # Rooms
                Box((-48, 10, -48), (-32, 21, -32)),

                wall_texture_1,
            ),
        ),
        Object(
            columns,
            Texture(Pigment(color=Colors.Tan)),
        ),
        Difference(
            Cylinder((0, 28, 0), (0, 30, 0), 16.25),
            Cylinder((0, 27, 0), (0, 31, 0), 11.75),
            Texture(Pigment(color=Colors.Tan)),
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
