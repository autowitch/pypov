from pypov.pov import Texture, Pigment, Intersection, Cylinder, Merge
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_009_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def edge_5x10_009(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""

    steps = Merge()
    xpos = -44.0001
    zpos = -19.0001
    for x in range(11, 20):
        steps.append(Box((xpos, x, -2.50001), (xpos - 1.001, 21, 2.50001)))
        steps.append(Box((22.50001, x, zpos), (27.49999, 21, zpos - 1.0001)))
        xpos += 1
        zpos += 1

    outer_steps = Merge()
    for x in range(21, 30):
        outer_steps.append(Box((xpos, x, -2.50001), (xpos - 1.001, 19.9999, 2.50001)))
        outer_steps.append(Box((22.50001, x, zpos), (27.49999, 19.9999, zpos - 1.0001)))
        xpos += 1
        zpos += 1

    print xpos
    print zpos

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001,  10), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002,  -20), (  27.5, 21, -26)),
                Box((  51, 10,  -2.5), (45, 21,   2.5)),
                Box((  -51, 10,  -2.5), (-45, 21,   2.5)),

                Box((-27.5001, 10, 10.001), (35, 21, 15)),

                steps,
                wall_texture_1
            ),
        ),
        Union(
            outer_steps,
            Difference(
                Union(
                    Box((-28, 28, -3.5), (15, 32, 3.5)),
                    Box((-28.0001, 20, -3.5), (-40, 32, 3.5)),
                ),
                Box((-29, 29, -2.5), (16, 40, 2.5), wall_texture_1),
                Box((0, 0, -4), (-17, 17, 4), " rotate <0, 0, 45> translate <-28, 32, 0> "),
                Box((-40, 19, -2.5), (-28, 40, 2.5), wall_texture_1),
                cross_hatch_texture,
            ),
            wall_texture_1,
            # Pigment(color=Colors.Tan),
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
