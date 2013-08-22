from pypov.pov import Texture, Pigment, Intersection, Cylinder, Merge
from pypov.pov import Union, Difference, Object, Box, Sphere
from pypov.pov import Material, Finish, Normal, Interior

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_007_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def edge_5x10_007(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001,  -12), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002,  2.50001), (  27.5, 21, -26)),
                Box((  22.50001, 10.0004,  -2.5), (51, 21,   2.5)),

                # End hall
                Box((  -51, 10,  -2.5), (-35, 21,   2.5)),
                # Two end rooms
                Merge(
                    Box((-10.00001, 10, -14), (15.0001, 21, -18)),
                    Box((-10.00001, 10, -7), (15.0001, 21, -11)),
                    Box((-10.00001, 10, 0), (15.0001, 21, -4)),
                    Box((-10.00001, 10, 7), (15.0001, 21, 3)),

                    Box((-10, 10.0001, -18.0001), (-6, 21, 3.00001)),
                    Box((1, 10.0001, -18.0001), (-3, 21, 3.00001)),
                    Box((4, 10.0001, -18.0001), (8, 21, 3.00001)),
                    Box((11, 10.0001, -18.0001), (15, 21, 3.00001)),

                    Box((-9.9999, 10.00002, -7), (-36, 21, -2)),
                    Box((-32, 10.0003, -9), (-41, 21, 0)),
                    rotate=(0, 6, 0)
                ),

                Box((-42, 10, -10), (-29, 21, -21)),
                Box((-39, 1, -13), (-32, 21, -18)),
                Box((-30, 10.0002, -11), (-25, 18, -15)),

                wall_texture_1,
            ),
        ),
        Box((-40, 0.4, -12), (-31, 9.5, -19)),
            Material(
                Texture(
                    Pigment(color="rgbt <0.2, 0.7, 0.3, 0.5>"),
                    Finish(
                        ambient=0,
                        diffuse=0,
                        reflection="{ 0.0, 1.0 fresnel on }",
                        specular=0.4,
                        roughness=0.0003
                    ),
                    Normal(
                        # "function { f_ridged_mf(x, y, z, 0.1, 3.0, 7, 0.7, 0.7, 2) } 0.8 scale 0.13",
                        "function { f_ridged_mf(x, y, z, 0.1, 3.0, 7, 0.7, 0.7, 2) } 0.12 scale 0.13",
                    )
                ),
                Interior(
                    ior=1.3,
                    media = "{ absorption <0.8, 0.6, 1.0, 0.5>  " +
                        "scattering { 3 <0.5, 0.65, 0.4> } } ",
                    #fade_distance = 4,
                    #fade_power = 1001,
                    #fade_color = (0.8, 0.2, 0.2, 0.5),
                ),
            ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
