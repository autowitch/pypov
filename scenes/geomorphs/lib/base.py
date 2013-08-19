from pypov.pov import Box, Difference, Texture, Pigment, Union
from pypov.pov import Normal, Checker, Brick, Wrinkles, Finish
from pypov.pov import Interior, Material
from pypov.common import grey
from pypov.colors import Colors

# Basic checkerboard pattern on a 5x5 grid. tiles well.
cross_hatch = Texture(
    Pigment(Checker(Colors.LightWood, Colors.MediumWood)),
    scale=5
)

# Completely transparent.
cross_hatch_2 = Texture(
    Pigment(color=Colors.Clear)
)

# Glass
cross_hatch_3 = Material(
    Texture(
        Pigment(
            filter=0.7,
            transmit=0.7,
            color=(0.8, 1, 0.95, 0.9), # Quirky little bug here. The color argument
                                       # in POVRay must be listed FIRST, however, the
                                       # way the argument list is built makes it necessary
                                       # to put it last.
        ),
        Finish(
            ambient=0.1,
            diffuse=0.1,
            reflection=0.1,
            specular=0.8,
            roughness=0.0003,
            phong=1,
            phong_size=400,
        )
    ),
    Interior(
        ior=1.5
    )
)

# Wall Texture 1 - sandstone brick

wall_texture_1 = Texture(
    Pigment(
        Brick(
            Colors.Gray15, Colors.DarkTan,
            brick_size = (2.5, 1.5, 2.5),
            mortar = 0.1
        ),
        #Normal(
            #Wrinkles(0.75, scale=0.1)
        #),
        #Finish(diffuse=0.9, phong=0.2)
        translate=(0.15, 0.15, 0.15)
    )
)

five_by_five = Difference(
    Box((-25,     0,    -25),    ( 25,     20,  25)),
    Box(( -4.99, 10.01,  24.75), (  4.99,  21,  26)),
    Box(( -4.99, 10.01, -24.75), (  4.99,  21, -26)),
    Box((-24.75, 10.01,  -4.99), (-26,     21,   4.99)),
    Box(( 24.75, 10.01,  -4.99), ( 26,     21,   4.99)),
)

five_by_five_corner = Difference(
    Box((-25,    0,     -25),    ( 25,    20,  25)),
    Box(( -4.99, 10.01, -24.75), (  4.99, 21, -26)),
    Box((-24.75, 10.01,  -4.99), (-26,    21,   4.99)),
)


ten_by_ten = Difference(
        Box((-50, -0, -50), (50, 20, 50)),

)
    #geomorph = Union(
        #Texture(
            #Pigment(color=(0.025, 0.025, 0.025)),
            #Finish(reflection=0.05)
        #),
        #translate=translate,
        #rotate=rotate
    #)
    #return geomorph

class TenXTen(object):
    """docstring for TenXTen"""
    def __init__(self):
        super(TenXTen, self).__init__()

class TenXFive(object):
    """docstring for TenXFive"""
    def __init__(self):
        super(TenXFive, self).__init__()

class FiveByFive(object):

    """docstring for FiveByFive"""
    def __init__(self):
        super(FiveByFive, self).__init__()




