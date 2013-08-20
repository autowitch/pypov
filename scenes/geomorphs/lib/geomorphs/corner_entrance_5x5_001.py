
from pypov.pov import Texture, Pigment, Isosurface, Function, Intersection
from pypov.pov import Finish, Box, Cone, Object, Cylinder
from pypov.pov import Union, Difference
from pypov.colors import Colors

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1

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
            Object(five_by_five_corner(), cross_hatch_texture),
            Union(
                #Box(( -5, 10,  -4.9999), (  5, 21, -26)), # hall 1
                #Box((  5.0001, 10,  -5), (-26, 21,   5)), # hall 2
                #Box((-20, 10.000001, -20), ( 20, 21,  20)), # big room

                # Halls
                Box(( -2.5, 10,  -17), (  2.5, 21, -26)),
                Box((  -12, 10,  -2.5), (-26, 21,   2.5)),

                # Rooms
                Box((8, 10.0002, -15), (-10, 21, 10)),
                Box((8, 10.0002, 12), (-10, 21, 23)),

                # Doors
                Box((25, 10.00003, 5), (-9, 16, 1.5)),
                Cylinder((25, 16, 3.25), (0, 16, 3.25), 1.75),
                Box((-2, 10.00002, -18), (2, 16, 14)),
                Cylinder((0, 16, -18), (0, 16, 14), 2),
                Box((-13, 10.00001, -2), (-9, 16, 2)),
                Cylinder((-13, 16, 0), (-9, 16, 0), 2),

                # Outside
                Object(
                    Box((11, -1, -26), (26, 21, 26),
                        cross_hatch_texture
                    ),
                ),

                wall_texture_1
            ),
        ),
        Intersection(
            Union(
                Difference(
                    Object(
                        Isosurface("function  { f_rounded_box (x, y, z, 1, 2, 20, 10 ) - f_ridged_mf(x / 10, y / 15, z / 10, 1, 0.5, 0.5, 1.2, 1, 2) * 2 - fn_Pigm(x, y, z).gray*0.05 } contained_by { box { <-25.001, -25.001, -25.001>, <25.001, 25.001, 25.001> } } max_gradient 10 ", #- fn_Pigm(x, y, z).gray*0.05} ",
                            translate=(14, 10, 5),
                            rotate=(0, 10, 15),
                        ),
                    ),
                    Box((25, 10.00003, 5), (-9, 16, 1.5)),
                    Cylinder((25, 16, 3.25), (0, 16, 3.25), 1.75),
                    Texture(Pigment(color=Colors.Tan))
                ),
                Object(
                    Isosurface("function { abs(y + f_noise3d(x / 20, 0, z / 20) * 15) - 4 } contained_by { box { <14.0002, -20, -10.0002>, <25.0002, 20, 14.0002> } } max_gradient 4 ",
                        translate=(0, 11, 0),
                    ),
                    Texture(Pigment(color=Colors.DarkOliveGreen))
                ),
            ),
            Object(
                Box((11, 3, -7), (25, 27, 11)),
                cross_hatch_texture
            )
        ),
        wall_texture_1,
        translate=translate,
        rotate=rotate
    )

    return geomorph
