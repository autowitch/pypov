from pypov.pov import Texture, Pigment, Intersection, Cylinder, Finish, Interior
from pypov.pov import Union, Difference, Object, Box, Sphere, Isosurface

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_017_info():
    return Metadata("Gelatinous Cube!", "e17",
            description="Room with huge Gelatinous Cube",
            block_type="edge",
            bottom=0, top=20,
            size="5x10",
            repeatable=False,
            fully_connected=True,
            dead_ends=False,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=False,
            multi_level=False,
            keywords=['monster', 'gelatinous cube'])

def edge_5x10_017(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001, -10), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002, -10), (  27.5, 21, -26)),
                Box(( -51,   10,       -2.5), (51,   21,   2.5)),
                Box(( -27.5, 10,      -10.0), (27.5, 21,  -5.0)),

                Box(( -7, 10.00003, -10), (-17, 21, 2.50001)),

                Box(( 10, 10.00003, 5), (35, 21, -15)),

                Box(( 14, 10, 7), (32, 21, 22)),
                Box(( 20, 10.001, 4), (24, 17, 8)),

                Box(( -6, 10, 7), (12, 21, 22)),
                Box((11, 10.0001, 12), (15, 17, 16)),
                wall_texture_1
            ),
        ),
        Union(
            Isosurface("function  { f_rounded_box (x, y, z, 0.25, 7, 7, 7 ) - f_noise3d( x / 7, y / 7, z / 7) * 4 } " +
                #                "f_ridged_mf(x / 10, y / 15, z / 10, 1, 0.5, 0.5, 1.2, 1, 2) * 2 - " +
                #"fn_Pigm(x, y, z).gray*0.05 } " +
                "contained_by { box { <-25.001, -25.001, -25.001>, <25.001, 25.001, 25.001> } " +
                "} max_gradient 10 ",
                translate=(22, 17, -5),
            ),
            Texture(
                Pigment(color="rgbf <0.4, 1, 0.55, 0.8>"),
                Finish("conserve_energy",
                    specular=0.6,
                    roughness=0.005,
                    ambient=0,
                    diffuse=0.15,
                    brilliance=4,
                    reflection="{ 0.05, 0.25 fresnel on }",
                ),
            ),
            Interior(ior=1.3,
                dispersion=1.15,
                fade_distance=10,
                fade_power=1001,
            ),
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph
