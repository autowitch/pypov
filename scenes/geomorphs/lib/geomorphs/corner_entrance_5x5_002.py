from pypov.pov import Texture, Pigment, Isosurface, Function, Intersection
from pypov.pov import Finish, Box, Cone, Object, Cylinder
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, wall_texture_1, cross_hatch_2

from lib.metadata import Metadata
from lib.elements.stairways import circular_stairs

def corner_entrance_5x5_002_info():
    return Metadata("Corner with vertical entrance", "ce2",
            description="Corner with a sprial staircase leading to an entrance",
            block_type="corner",
            bottom=0, top=20,
            size="5x5",
            repeatable=False,
            fully_connected=True,
            dead_ends=False,
            entrance=True,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=True,
            keywords=['entrance', 'side chambers', 'multiple rooms', 'stairway', 'spiral staircase'])

def corner_entrance_5x5_002(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):

    """docstring for gm02"""

    step_texture = Texture(Pigment(color=Colors.Gray50))
    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Union(
                #Box(( -5, 10,  -4.9999), (  5, 21, -26)), # hall 1
                #Box((  5.0001, 10,  -5), (-26, 21,   5)), # hall 2
                #Box((-20, 10.000001, -20), ( 20, 21,  20)), # big room

                # Halls
                Box(( -2.5, 10,  -17), (  2.5, 21, -26)),
                Box((  -12, 10,  -2.5), (-26, 21,   2.5)),

                # Stair Base
                Cylinder((15, 10, 0), (15, 21, 0), 5),

                # Rooms
                Box((8, 10.0002, -15), (-10, 21, 10)),
                Box((8, 10.0002, 12), (-10, 21, 23)),
                Box((23, 10.0002, 7), (10, 21, 23)),

                # Doors
                Box((15, 10.00003, 5), (-9, 16, 1.5)),
                Cylinder((15, 15, 3.25), (0, 15, 3.25), 2),
                Box((-2, 10.00002, -18), (2, 16, 14)),
                Cylinder((0, 16, -18), (0, 16, 14), 2),
                Box((-13, 10.00001, -2), (-9, 16, 2)),
                Cylinder((-13, 16, 0), (-9, 16, 0), 2),
                Box((11, 10.000003, 21), (7, 15, 18)),
                Cylinder((11, 15, 19.5), (7, 15, 19.5), 1.5),

                wall_texture_1
            ),
        ),
        Object(
            circular_stairs(height=50, step_height=0.75, step_angle=15,
                step_texture=step_texture),
            translate=(15,10,0),
        ),
        Difference(
            Cylinder((15, 20, 0), (15, 60, 0), 7),
            Object(Cylinder((15, 19, 0), (15, 61, 0), 5), wall_texture_1),
            Box((15, 19, -8), (8, 61, 8)),
            cross_hatch_texture
        ),
        Object(
            Difference(
    #            Isosurface(Function("y + f_noised3d(x*2, 0, z*2)"),
                Isosurface("function { abs(y + f_noise3d(x / 20, 0, z / 20) * 15) - 2 } contained_by { box { <-10, -20, -15>, <25, 20, 15> } } max_gradient 2 ",
                    translate=(0, 61, 0),
                ),
                Cylinder((15, 20, 0), (15, 70, 0), 5.01),
                Texture(Pigment(color=Colors.DarkOliveGreen)),
            ),
        ),
        Union(
            Difference(
                Box((24, 56.0, -8), (-2, 69.999, 8)),
                Cylinder((15, 57, 0), (15, 62, 0), 5.011),
                Box((23, 60.00001, -7), (10, 70, 7)),
                Box((9, 60.5, -7), (-1, 70, 7)),
                Box((-3, 60.500001, -2), (0, 65, 2)),
                Intersection(
                    Cylinder((-3, 65, -2), (0, 65, -2), 4),
                    Cylinder((-3, 65, 2), (0, 65, 2), 4),
                ),
                Box((8, 60.500001, 2), (11, 65, 6)),
                Intersection(
                    Cylinder((8, 65, 2), (11, 65, 2), 4),
                    Cylinder((8, 65, 6), (11, 65, 6), 4),
                ),
                Box((2, 64, 9), (5, 67.5, -9)),
                Cylinder((3.5, 67.5, 9), (3.5, 67.5, -9), 1.5),
            ),
            Box((-2, 58, -2), (-3, 60.5, 2)),
            Box((-3, 58, -2), (-4, 60, 2)),
            Box((-4, 58, -2), (-5, 59.5, 2)),
            Box((-5, 58, -2), (-6, 59, 2)),
        ),
        wall_texture_1,
        translate=translate,
        rotate=rotate
    )

    return geomorph
