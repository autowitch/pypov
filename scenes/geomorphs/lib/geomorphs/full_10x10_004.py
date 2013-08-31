from pypov.pov import Texture, Pigment, Intersection, Cylinder, Torus
from pypov.pov import Union, Difference, Object, Box, Sphere, Merge, Isosurface

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import ten_by_ten
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1, white_plaster
from lib.textures import blue_plaster, brown_plaster
from lib.metadata import Metadata
from lib.util import float_range

def full_10x10_004_info():
    return Metadata("Deep pit", "ff4",
            description="Deep natural pit",
            block_type="full",
            bottom=-100, top=20,
            size="10x10",
            repeatable=False,
            fully_connected=False,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="hewn, cavern",
            wet=False,
            multi_level=False,
            keywords=['INCOMPLETE', 'pit', 'cavern', 'deep', 'isosurface'])

def full_10x10_004(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2, cutaway=None):
    """docstring for gm02"""

    cut_slice = None
    cutaway = True # TODO
    if cutaway:
        cut_slice = Box((-51, 0.0001, -21), (-20, -91, 31))

    geomorph = Union(
        Difference(
            Merge(
                Object(ten_by_ten()),
                Box((-50, 0, -20), (50, -90, 30)),
                cross_hatch_texture,
            ),
            Union(
                cut_slice,

                # Halls
                Box((-22.5, 10.0001,  -40), (-27.5, 21, -51)),
                Box((22.5, 10.0002,  -40), (27.5, 21, -51)),
                Box((-37, 10.01, -22.5), (-51, 21, -27.5)),

                Box((40, 10.01, -22.5), (51, 21, -27.5)),
                Box((-30, 10.01, 22.5), (-51, 21, 27.5)),
                Box((40, 10.01, 22.5), (51, 21, 27.5)),

                # Sides

                Box((22.5, 10.01, 45), (27.5, 21, 51)),
                Box((-22.5, 10.01, 45), (-27.5, 21, 51)),

                # Pit

                Object(
                    Isosurface("function  { f_rounded_box (x, y, z, 10, 30, 60, 8 ) - " +
                               "f_ridged_mf((x - 342) / 8, (y + 32423) / 25, (z + 6754654) / 8, 1, 0.5, 0.5, 1.2, 1, 2) * 2 - " +
                               "f_noise3d((x + 324321) / 4, (y - 349432) / 10, (z + 316247) / 4) - " +
                               "fn_Pigm(x, y, z).gray*0.05 } " +
                               "contained_by { box { <-50.001, -100.001, -50.001>, <50.001, 50.001, 50.001> } } " +
                               "max_gradient 10 " +
                               "all_intersections",
                               translate=(0, -20, 0),
                               rotate=(0, 10, 15),
                    ),
                    Texture("T_Stone10", scale=(10, 10, 10)),
                ),

                # Rooms and passages

                Box((-15, 10, -30), (5, 21, -42)),
                Box((-3, 10.0001, -30.0001), (2, 21, 0)),

                Box((-17, 10, -25), (-30, 21, -40)),

                wall_texture_1,
            ),
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph

