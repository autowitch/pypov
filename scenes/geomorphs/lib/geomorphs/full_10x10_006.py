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

def full_10x10_006_info():
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

def full_10x10_006(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2, cutaway=None):
    """docstring for gm02"""

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

                # Sides

                Box((22.5, 10.01, 22.999), (27.5, 21, 51)),
                Box((-22.5, 10.01, 27.999), (-27.5, 21, 51)),

                # Pit
                Box((-48, -85, -48), (-30, 21, 48)),
                Box((48, -85, -48), (30, 21, 48)),
                Box((-30.0001, -85.0001, -48.0001), (30.0001, 21, -30)),
                Box((-30.0001, -85.0001, 48.0001), (30.0001, 21, 30)),

                # Interior rooms

                Box((-28, 10, -28), (-5, 21, 10)),
                Box((-28, 10, 28), (0, 21, 12)),
#                Box((28, 10, 28), (10, 21, 15)),
                Cylinder((21, 10, 21), (21, 21, 21), 7.5),
                Box((28, 10, 12), (10, 21, -5)),
                Box((28, 10, -7), (15, 21, -15)),
                Box((28, 10, -17), (15, 21, -28)),
                Box((13, 10, -28), (-3, 21, -7)),
                Box((8, 10, 28), (2, 21, -5)),

                # Interior doors
                Box((6, 12, 27), (4, 17, 31)),
                Box((24, 10.0001, -18), (19, 18, 20)),
                Box((7, 10.001, -4), (3, 18, -8)),
                Box((-1, 10.001, 24), (20, 18, 20)),
                Box((13, 10.0001, -2), (7, 18, 2)),

                wall_texture_1,
            ),
        ),
        Union(
            # Bridges
            Difference(
                Box((-30, 10, -24), (-48, 0, -26)),
                Cylinder((-39, 0, -23), (-39, 0, -27), 9),
            ),
            Difference(
                Box((-24, 10, -30), (-26, 0, -48)),
                Cylinder((-23, 0, -39), (-27, 0, -39), 9),
            ),
            wall_texture_1,
        ),

        # Water
        Box((-49.5, -89.5, -49.5), (49.5, -25, 49.5),
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
        ),
        translate=translate,
        rotate=rotate
    )

    return geomorph

