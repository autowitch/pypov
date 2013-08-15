from pypov.pov import Box, Difference, Texture, Pigment, Union
from pypov.common import grey

red = Texture(Pigment(color=(1, 0, 0)))

five_by_five = Difference(
        Box((-25,    0,  -25),    ( 25,   50,  25), grey),
        Box(( -5,    35,  24.75), (  5,   51,  26), red),
        Box(( -5,    35, -24.75), (  5,   51, -26), red),
        Box((-24.75, 35,  -5),    (-26,   51,   5), red),
        Box(( 24.75, 35,  -5),    ( 26,   51,   5), red),
)

five_by_five_corner = Difference(
        Box((-25,    0,  -25),    ( 25,   50,  25)),
        Union(
            Box(( -5,    35, -24.75), (  5,   51, -26)),
            Box((-24.75, 35,  -5),    (-26,   51,   5)),
        )
)


ten_by_ten = Difference(
        Box((-50, -0, -50), (50, 50, 50), grey),

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




