from pypov.pov import Box, Difference, Texture, Pigment, Union
from pypov.pov import Normal, Checker, Brick, Wrinkles, Finish
from pypov.common import grey
from pypov.colors import Colors

cross_hatch = Texture(
    Pigment(Checker(Colors.LightWood, Colors.MediumWood)),
    scale=5
)

wall_texture_1 = Texture(
    Pigment(
        Brick(
            Colors.DimGrey, Colors.DarkTan,
            brick_size = (2.5, 1.5, 2.5),
            mortar = 0.1
        ),
        #Normal(
            #Wrinkles(0.75, scale=0.1)
        #),
        #Finish(diffuse=0.9, phong=0.2)
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




