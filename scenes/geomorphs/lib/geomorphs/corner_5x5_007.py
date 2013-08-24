from pypov.pov import Texture, Pigment, Object, Cylinder
from pypov.pov import Finish, Box, Cone, Sphere
from pypov.pov import Union, Difference
from pypov.colors import Colors

from lib.base import five_by_five_corner
from lib.textures import cross_hatch_2, wall_texture_1
from lib.metadata import Metadata
from lib.util import float_range


def corner_5x5_007_info():
    return Metadata("Terminating rooms with a cage", "c7",
            description="Terminating rooms with a cage",
            block_type="corner",
            bottom=0, top=20,
            size="5x5",
            repeatable=False,
            fully_connected=False,
            dead_ends=True,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['cage', 'prison', 'rust', 'metal', 'dead ends'])

def corner_5x5_007(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""
    cage = Union()
    for x in float_range(0.5, 15, 0.75):
        cage.append(Cylinder((-5 + x, 10, 14.5), (-5 + x, 20, 14.5), 0.125))
        cage.append(Cylinder((-5 + x, 10, 0.5), (-5 + x, 20, 0.5), 0.125))
        cage.append(Cylinder((-4.5, 10, x), (-4.5, 20, x), 0.125))
        cage.append(Cylinder((9.5, 10, x), (9.5, 20, x), 0.125))

    for x in float_range(10.5, 20.5, 1):
        cage.append(Cylinder((-4.5, x, 14.5), (9.5, x, 14.5), 0.125))
        cage.append(Cylinder((-4.5, x, 0.5), (9.5, x, 0.5), 0.125))
        cage.append(Cylinder((-4.5, x, 0.5), (-4.5, x, 14.5), 0.125))
        cage.append(Cylinder((9.5, x, 0.5), (9.5, x, 14.5), 0.125))

    cage.append(Cylinder((-4.5, 9, 0), (-4.5, 20, 0), 0.25))
    cage.append(Cylinder((-4.5, 9, 14.5), (-4.5, 20, 14.5), 0.25))
    cage.append(Cylinder((9.5, 9, 0), (9.5, 20, 0), 0.25))
    cage.append(Cylinder((9.5, 9, 14.5), (9.5, 20, 14.5), 0.25))

    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Union(
                Box((-2.5, 10, -22), (  2.5, 21, -26)),
                Box(( -22, 10, -2.5), (-26, 21,   2.5)),

                Box((-23, 9, -5), ( 15, 21,  20)),

                Box((-10, 10, -23), (10, 21, -9)),
                wall_texture_1
            ),
        ),
        Object(Box((-5, 8.999, 0), (10, 10, 15)), wall_texture_1),
        Object(cage, Texture("Rust")),
        translate=translate,
        rotate=rotate
    )
    return geomorph
