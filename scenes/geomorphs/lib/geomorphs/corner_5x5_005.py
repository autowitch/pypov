
from pypov.pov import Texture, Pigment
from pypov.pov import Finish, Box, Cone, Cylinder, Object
from pypov.pov import Union, Difference

from pypov.common import grey, white
from lib.base import five_by_five_corner
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1, cross_hatch_3


from lib.metadata import Metadata

def corner_5x5_005_info():
    return Metadata("Corner with side rooms", "c5",
            description="Corner with two small side rooms",
            block_type="corner",
            bottom=0, top=20,
            size="5x5",
            repeatable=True,
            fully_connected=True,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['multiple rooms', 'basic', 'side chambers'])

def corner_5x5_005(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""
    geomorph = Union(
        Difference(
            Object(five_by_five_corner(), cross_hatch_texture),
            Union(
                Box(( -2.5, 10, -2.4999), (  2.5, 21, -26)),
                Box((  2.5, 10, -2.5), (-26, 21,   2.5)),

                # Rooms
                Box(( 23, 10, 23), (  0, 21,   7)),
                Box(( -2, 10, 23), (-15, 21,   7)),

                # Doors
                Box((  0.1, 10.1, 14),  (-2.1, 15, 20)),
                Cylinder((0.1, 15, 17),  (-2.1, 15, 17), 3),

                Box((-13,   10.1, 2.4), (-7,   15,  7.1)),
                Cylinder((-10, 15, 2.4), (-10, 15, 7.1), 3),
                wall_texture_1
            )
        ),
        Texture(
            Pigment(color=(0.5, 0.45, 0.25)),
            #Pigment(color=(0.025, 0.025, 0.025)),
            #Finish(reflection=0.05)
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
