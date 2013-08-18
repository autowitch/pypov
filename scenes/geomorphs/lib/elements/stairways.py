from pypov.pov import Cylinder, Box, Intersection, Difference, Union

def circular_stairs(height=10, radius=5, core_radius=1.5):

    stairway = Union(
            Cylinder((0, 0, 0), (0, height, 0), core_radius)
    )

    return stairway


