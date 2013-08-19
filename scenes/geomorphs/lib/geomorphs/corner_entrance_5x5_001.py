
from pypov.pov import Texture, Pigment, Isosurface, Function, Intersection
from pypov.pov import Finish, Box, Cone, Object, Cylinder
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner, cross_hatch, wall_texture_1, cross_hatch_2

from lib.metadata import Metadata
from lib.elements.stairways import circular_stairs

def corner_entrance_5x5_001_info():
    return Metadata("Corner with horizontal entrance", "ce2",
            description="Corner with a horzontal entrance",
            block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=False, fully_connected=True,
            dead_ends=False, entrance=True, has_rooms=True,
            passage_type="hewn", wet=False)

def corner_entrance_5x5_001(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):

    """docstring for gm02"""

    step_texture = Texture(Pigment(color=Colors.Gray50))
    geomorph = Union(
        Difference(
            Object(five_by_five_corner, cross_hatch_texture),
            Union(
                #Box(( -5, 10,  -4.9999), (  5, 21, -26)), # hall 1
                #Box((  5.0001, 10,  -5), (-26, 21,   5)), # hall 2
                #Box((-20, 10.000001, -20), ( 20, 21,  20)), # big room

                # Halls
                Box(( -5, 10,  -17), (  5, 21, -26)),
                Box((  -12, 10,  -5), (-26, 21,   5)),

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
            Difference(
    #            Isosurface(Function("y + f_noised3d(x*2, 0, z*2)"),
                #Isosurface("function { abs(y + f_noise3d(x / 20, 0, z / 20) * 15) - 1 } contained_by { box { <-25, -20, -25>, <25, 20, 25> } } max_gradient 2 ",
                Isosurface("function { abs(y + f_wrinkles(x / 40, 0, z / 40) * f_crackle(x / 40, 0, z / 40) * -70 - f_agate(x / 20, 0, z / 20)- f_granite(x / 20, 0, z / 20)) - 1 } contained_by { box { <-250, -90, -250>, <250, 90, 250> } } max_gradient 2 ",
                    translate=(0, 10, 0),
                    rotate=(0, 45, 0),
                ),
                Cylinder((15, 20, 0), (15, 70, 0), 5.01),
                Texture(Pigment(color=Colors.DarkOliveGreen)),
            ),
        ),
        wall_texture_1,
        translate=translate,
        rotate=rotate
    )

    return geomorph
