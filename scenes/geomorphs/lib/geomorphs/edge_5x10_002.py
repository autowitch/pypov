from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_002_info():
    return Metadata("Edge passages", "e2",
            description="Edge passages",
            block_type="edge",
            bottom=0, top=20,
            size="5x10",
            repeatable=True,
            fully_connected=True,
            dead_ends=False,
            entrance=False,
            has_rooms=False,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['passages', 'basic', 'boring'])

def edge_5x10_002(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001,  2.50001), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002,  2.50001), (  27.5, 21, -26)),
                Box((  -51, 10,  -2.5), (51, 21,   2.5)),
                wall_texture_1
            ),
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
