from pypov.pov import Texture, Pigment, Intersection, Cylinder, Torus
from pypov.pov import Union, Difference, Object, Box, Sphere, Isosurface

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_011_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def edge_5x10_011(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    #def chain_link():
        #r_maj = 0.25
        #r_min - 0.1
        #link = Difference(
            #Torus(r_maj, r_min, rotate=(90, 0, 0)),
            #Box((0, 0 - r_maj - r_min, -r_min),
                #(r_maj + r_min, r_maj + r_min, r_min))
        #)
        #return link

    #def chain():
        #obj = Union()

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge()),
                # Boulder supports
                Box((-5, 20, 7), (5, 30, -7)),
                Box((-19, 20, 7), (-9, 30, -7)),
                Box((-31, 20, 7), (-21, 30, -7)),
                cross_hatch_texture,
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001,  -20), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002,  -20), (  27.5, 21, -26)),
                Box((  -51, 10,  -2.5), (-45, 21,   2.5)),
                Box((  51, 10,  -2.5), (45, 21,   2.5)),

                Box((  -45.0001, 10.0001,  -20), (45, 21,   -15)),
                Box((  -45.0002, 10.0001,  -20.001), (-40, 21,   2.50001)),
                Box((  45.0002, 10.0001,  -20.001), (40, 21,   2.50001)),

                # rooms
                Box(( -38, 10, -5), (10, 21, 5)),
                Box(( 12, 10, -10), (35, 21, 20)),
                Box(( -4, 10, 8), (10, 21, 20)),
                Box((-6, 10, 8), (-27, 21, 20)),
                # Halls
                Box(( -41, 10.0002, -2), (13, 18, 2)),
                Box((-7, 10.0001, 13), (13, 18, 17)),

                # Boulder supports
                Box((-4.5, 19, 5.5), (4.5, 31, -5.5)),
                Box((-4.5 - 14, 19, 5.5), (4.5 - 14, 31, -5.5)),
                Box((-4.5 - 28, 19, 5.5), (4.5 - 28, 31, -5.5)),

                Box((-33, 19, 5), (7, 31, -5)),

                wall_texture_1
            ),
        ),
        Union(
            Isosurface("function  { f_rounded_box (x, y, z, 1, 2.5, 6, 2.5 ) - " +
                "f_ridged_mf(x / 10, y / 15, z / 10, 1, 0.5, 0.5, 1.2, 1, 2) * 2 - " +
                "fn_Pigm(x, y, z).gray*0.05 } " +
                "contained_by { box { <-25.001, -25.001, -25.001>, <25.001, 25.001, 25.001> } " +
                "} max_gradient 10 ",
                translate=(-28, 25, 0),
            ),
            Isosurface("function  { f_rounded_box (x, y, z, 1, 2.5, 6, 2.5 ) - " +
                "f_ridged_mf((x + 1324) / 10, (y  - 34223)  / 15, (z + 23421) / 10, 1, 0.5, 0.5, 1.2, 1, 2) * 2 - " +
                "fn_Pigm(x, y, z).gray*0.05 } " +
                "contained_by { box { <-25.001, -25.001, -25.001>, <25.001, 25.001, 25.001> } " +
                "} max_gradient 10 ",
                translate=(-14, 25, 0),
            ),
            Isosurface("function  { f_rounded_box (x, y, z, 1, 2.5, 6, 2.5 ) - " +
                "f_ridged_mf((x + 34123) / 10, (y + 1231) / 15, (z - 95604) / 10, 1, 0.5, 0.5, 1.2, 1, 2) * 2 - " +
                "fn_Pigm(x, y, z).gray*0.05 } " +
                "contained_by { box { <-25.001, -25.001, -25.001>, <25.001, 25.001, 25.001> } " +
                "} max_gradient 10 ",
                translate=(0, 25, 0),
            ),
            Pigment(color=Colors.Tan),
        ),
        Union(
            Cylinder((0, 30, 0), (0, 34, 0), 1, Texture("T_Brass_1A")),
            Cylinder((-14, 30, 0), (-14, 34, 0), 1, Texture("T_Brass_1A")),
            Cylinder((-28, 30, 0), (-28, 34, 0), 1, Texture("T_Brass_1A")),
            Cylinder((0, 34, 0), (0, 34.5, 0), 0.25, Texture("T_Brass_1A")),
            Cylinder((-14, 34, 0), (-14, 34.5, 0), 0.25, Texture("T_Brass_1A")),
            Cylinder((-28, 34, 0), (-28, 34.5, 0), 0.25, Texture("T_Brass_1A")),

            Cylinder((-28, 34.5, 0), (-28, 40, 0), 0.05, Texture("T_Brass_1A")), # replace with rope or chain
            Cylinder((-14, 34.5, 0), (-14, 40, 0), 0.05, Texture("T_Brass_1A")), # replace with rope or chain
            Cylinder((0, 34.5, 0), (0, 40, 0), 0.05, Texture("T_Brass_1A")), # replace with rope or chain
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
