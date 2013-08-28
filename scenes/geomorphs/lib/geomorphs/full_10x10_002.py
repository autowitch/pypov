from pypov.pov import Texture, Pigment, Intersection, Cylinder, Material, Interior
from pypov.pov import Union, Difference, Object, Box, Sphere, Merge, Finish, Normal

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import ten_by_ten
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1, white_plaster
from lib.textures import blue_plaster, brown_plaster
from lib.metadata import Metadata
from lib.util import float_range

def full_10x10_002_info():
    return Metadata("Cistern", "ff2",
            description="Deep complex pit full of water and columns",
            block_type="full",
            bottom=-10, top=20,
            size="10x10",
            repeatable=False,
            fully_connected=False,
            dead_ends=True,
            entrance=False,
            has_rooms=True,
            passage_type="hewn",
            wet=True,
            multi_level=True,
            keywords=['INCOMPLETE', 'cistern', 'columns', 'water', 'pit', 'boat'])

def full_10x10_002(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    columns = Union()
    for x in range(-25, 30, 10):
        for z in range(-17, 37, 10):
            columns.append(Cylinder((x, -4, z), (x, 29, z), 0.75))
            columns.append(Cylinder((x, -5, z), (x, -4, z), 1))
            columns.append(Cylinder((x, 29, z), (x, 30, z), 1))

    geomorph = Union(
        Difference(
            Merge(
                Object(ten_by_ten()),
                Box((-27, -10, 34), (27, 0, -19)),
                cross_hatch_texture,
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001,  -48), ( -27.5, 21, -51)),
                Box((  22.5, 10.0002,  -48), (  27.5, 21, -51)),
                Box((-40, 10.01, -22.5), (-51, 21, -27.5)),

                Box((40, 10.01, -22.5), (51, 21, -27.5)),
                Box((-40, 10.01, 22.5), (-51, 21, 27.5)),
                Box((40, 10.01, 22.5), (51, 21, 27.5)),


                # Sides

                Box((22.5, 10.01, 45), (27.5, 21, 51)),
                Box((-22.5, 10.01, 45), (-27.5, 21, 51)),

                # Pool
                Box((-25, -5, 33), (25, 21, -17)),
                Box((-15, 10, -17), (15, 21, -36)),
                wall_texture_1,
            ),
        ),

        Object(
            columns,
            Pigment(color=Colors.Tan)
        ),

        Box((-25, -5, 33), (25, 9, -17),
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
            #"""
            #hollow
            #interior {
                #media {
                    #method 3
                    #scattering {
                        #1, <1,1,1>*3.00
                        #extinction  1.50
                    #}
                    #density {
                        #spherical
                        #color_map {
                            #[0.00 rgb 0.0]
                            #[0.05 rgb 0.0]
                            #[0.20 rgb 0.2]
                            #[0.30 rgb 0.6]
                            #[0.40 rgb 1.0]
                            #[1.00 rgb 1.0]
                        #}
                    #}
                    #samples 1,1
                    #intervals 3
                    #confidence .9
                    #scale <10, 10, 10>
                    #translate <0, 20, 0>
                #}
            #}
            #""",
        ),

        translate=translate,
        rotate=rotate
    )
    return geomorph
