from pypov.pov import Cylinder, Box, Intersection, Difference, Union, Object
from lib.util import float_range
from lib.textures import wall_texture_1

def circular_stairs(height=10, radius=5, core_radius=1.5, step_height=1,
        step_angle=10, start_angle=0, step_texture=wall_texture_1,
        core_texture=wall_texture_1, wall_texture=wall_texture_1,
        hollow_core=False):

    steps = Union()
    angle = start_angle
    for x in float_range(0, height, step_height):
        steps.append(
            Box((0, x, 0), (radius, x + step_height, radius),
                rotate=(0, angle, 0)
            )
        )
        angle += step_angle


    stairway = Union(
            Object(Cylinder((0, 0, 0), (0, height, 0), core_radius), core_texture),
            Intersection(
                Object(steps, step_texture),
                Object(Cylinder((0, 0, 0), (0, height, 0), radius), wall_texture)
            )
    )

    return stairway


