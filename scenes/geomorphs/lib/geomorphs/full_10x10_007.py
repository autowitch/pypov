from pypov.pov import Texture, Pigment, Intersection, Cylinder, Torus
from pypov.pov import Union, Difference, Object, Box, Sphere, Merge, Isosurface
from pypov.pov import Material, Normal, Finish, Interior

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import ten_by_ten
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1, white_plaster
from lib.textures import blue_plaster, brown_plaster
from lib.metadata import Metadata
from lib.util import float_range
import random


def full_10x10_007_info():
    return Metadata("Caves and stuf", "ff5",
            description="Caves and stuff",
            block_type="full",
            bottom=-100, top=20,
            size="10x10",
            repeatable=False,
            fully_connected=False,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="cavern",
            wet=False,
            multi_level=False,
            keywords=['INCOMPLETE', 'pit', 'cavern', 'deep', 'isosurface'])

def full_10x10_007(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2, cutaway=None):
    """docstring for gm02"""

    rooms = Union()
    for x in range(0, 360, 30):
        rooms.append(
            Object(
                Box((20, 10.0001, -5.0 + random.random()),
                    (30 + random.randint(0, 5) , 21, 5.0 - random.random()),
                    rotate=(0, x, 0))
            )
        )
        rooms.append(
            Object(
                Box((17, 10.0002, -1.5), (21, 18, 1.5), rotate=(0, x, 0))
            )
        )
    geomorph = Union(
        Difference(
            Merge(
                Object(ten_by_ten()),
                Box((-50, 10, -50), (50, -90, 50)),
                cross_hatch_texture,
            ),
            Union(
                # Halls
                Box((-22.5, 10.0001,  -27.999), (-27.5, 21, -51)),
                Box((22.5, 10.0002,  -27.999), (27.5, 21, -51)),
                Box((-27.999, 10.01, -22.5), (-51, 21, -27.5)),

                Box((27.999, 10.01, -22.5), (51, 21, -27.5)),
                Box((-27.999, 10.01, 22.5), (-51, 21, 27.5)),
                Box((22.999, 10.01, 22.5), (51, 21, 27.5)),

                Box((22.5, 10.01, 22.999), (27.5, 21, 51)),
                Box((-22.5, 10.01, 27.999), (-27.5, 21, 51)),

                Cylinder((0, 10, 0), (0, 26, 0), 18),

                rooms,
                wall_texture_1,

            ),
        ),
        Union(
            Box((-3, 10, -3), (3, 11, 3)),
            Box((-2, 11, -2), (2, 21, 2)),
            wall_texture_1,
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph

