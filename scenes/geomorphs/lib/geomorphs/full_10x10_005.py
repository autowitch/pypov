from pypov.pov import Texture, Pigment, Intersection, Cylinder, Torus
from pypov.pov import Union, Difference, Object, Box, Sphere, Merge, Isosurface

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import ten_by_ten
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1, white_plaster
from lib.textures import blue_plaster, brown_plaster
from lib.metadata import Metadata
from lib.util import float_range

def full_10x10_005_info():
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

def full_10x10_005(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2, cutaway=None):
    """docstring for gm02"""

    blob_threshold = 0.5

    geomorph = Union(
        Difference(
            Merge(
                Object(ten_by_ten()),
                cross_hatch_texture,
            ),
            Union(
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

                # Caverns

                # Object(
                #     Isosurface("function  { f_rounded_box (x, y, z, 10, 30, 60, 8 ) - " +
                #                "f_ridged_mf((x - 342) / 8, (y + 32423) / 25, (z + 6754654) / 8, 1, 0.5, 0.5, 1.2, 1, 2) * 2 - " +
                #                "f_noise3d((x + 324321) / 4, (y - 349432) / 10, (z + 316247) / 4) - " +
                #                "fn_Pigm(x, y, z).gray*0.05 } " +
                #                "contained_by { box { <-50.001, -100.001, -50.001>, <50.001, 50.001, 50.001> } } " +
                #                "max_gradient 10 " +
                #                "all_intersections",
                #                translate=(0, -20, 0),
                #                rotate=(0, 10, 15),
                #     ),
                #     Texture("T_Stone10", scale=(10, 10, 10)),
                # ),
                # Rooms and passages
                Object(
                    Isosurface("function  { " +
                               "( (1 + %s) " % blob_threshold +
                               "-pow(%s, f_rounded_box(x, y, z, 8, 17, 10, 10)) " % blob_threshold +
                               "-pow(%s, f_rounded_box(x + 4, y, z - 10, 3, 3, 8, 15)) " % blob_threshold  +
                               "-pow(%s, f_rounded_box(x - 7, y, z + 20, 5, 3, 5, 25)) " % blob_threshold  +
                               "-pow(%s, f_rounded_box(x + 2, y + 3, z + 40, 9, 30, 6, 8)) " % blob_threshold  +
                               "-pow(%s, f_sphere(x - 20, y - 3, z - 20, 10)) " % blob_threshold  +
                               "-pow(%s, f_sphere(x - 10, y - 3, z - 12, 7)) " % blob_threshold  +
                               "-pow(%s, f_rounded_box(x + 6, y, z + 12, 6, 4, 40, 6)) " % blob_threshold +
                               "-pow(%s, f_rounded_box(x + 5, y + 2, z - 38, 6, 12, 14, 7)) " % blob_threshold +
                               "-pow(%s, f_sphere(x + 8, y + 2, z - 25, 6)) " % blob_threshold  +
                               "-pow(%s, f_rounded_box(x + 9, y - 2, z + 20, 5, 6, 3, 18)) " % blob_threshold  +
                               "-pow(%s, f_sphere(x / 2 + 15, y, z + 21, 6)) " % blob_threshold +
                               "-pow(%s, f_sphere(x / 1.4 + 13, y * 1.25, (z * 4) + 24, 4)) " % blob_threshold +
                               "-pow(%s, f_sphere(x + 13, y, z + 27, 7)) ) " % blob_threshold +
                               "+ f_ridged_mf(x / 10, y / 15, z / 10, 1, 0.5, 0.5, 1.2, 1, 2) * 2 " +
                               "- f_ridged_mf((x - 34231) / 8, (y + 6427) / 4, (z - 9423421) / 12, 1, 0.5, 0.5, 1.2, 1, 2) * 1.5 " +
                               "- fn_Pigm(x, y, z).gray*0.10 " +
                               "} " +
                               "contained_by { box { <-50.001, -50.001, -50.001>, <50.001, 50.001, 50.001> } } " +
                               "max_gradient 20 " +
                               "all_intersections ",
                               translate=(0, 20, 0),
                               rotate=(0, 10, 0),
                    ),
                    Texture("T_Stone10", scale=(10, 10, 10)),
                ),

                wall_texture_1,
            ),
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph

