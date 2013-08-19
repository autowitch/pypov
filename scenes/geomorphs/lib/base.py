from pypov.pov import Box, Difference, Texture, Pigment, Union, Object
from pypov.pov import Normal, Checker, Brick, Wrinkles, Finish
from pypov.pov import Interior, Material
from pypov.common import grey
from pypov.colors import Colors

def five_by_five_full(highlight_exits=False):
    exits = Union(
        Box(( -2.499, 10.01,  24.75), (  2.499,  21,  26)),
        Box(( -2.499, 10.01, -24.75), (  2.499,  21, -26)),
        Box((-24.75, 10.01,  -2.499), (-26,     21,   2.499)),
        Box(( 24.75, 10.01,  -2.499), ( 26,     21,   2.499)),
    )
    if highlight_exits:
        exits = Union(
            Box(( -2.499, 10.01,  24.75), (  2.499,  21,  26), Pigment(color=Colors.Red)),
            Box(( -2.499, 10.01, -24.75), (  2.499,  21, -26), Pigment(color=Colors.Red)),
            Box((-24.75, 10.01,  -2.499), (-26,     21,   2.499), Pigment(color=Colors.Red)),
            Box(( 24.75, 10.01,  -2.499), ( 26,     21,   2.499), Pigment(color=Colors.Red)),
        )
    obj = Difference( # 4 exits
        Box((-25,     0,    -25),    ( 25,     20,  25)),
        exits
    )
    return obj

def five_by_five_corner(highlight_exits=False):
    exits = Union(
        Box(( -4.99, 10.01, -24.75), (  4.99, 21, -26)),
        Box((-24.75, 10.01,  -4.99), (-26,    21,   4.99)),
    )
    if highlight_exits:
        exits = Union(
            Box(( -4.99, 10.01, -24.75), (  4.99, 21, -26), Pigment(color=Colors.Red)),
            Box((-24.75, 10.01,  -4.99), (-26,    21,   4.99), Pigment(color=Colors.Red)),
        )
    obj = Difference( # two exits 90 degrees
        Box((-25,    0,     -25),    ( 25,    20,  25)),
        exits,
    )
    return obj

def five_by_five_pipe(highlight_exits=False):
    exits = Union(
        Box(( -4.99, 10.01, -24.75), (  4.99, 21, -26)),
        Box(( -4.99, 10.01,  24.75), (  4.99, 21, 26)),
    )
    if highlight_exits:
        exits = Union(
            Box(( -4.99, 10.01, -24.75), (  4.99, 21, -26), Pigment(color=Colors.Red)),
            Box(( -4.99, 10.01,  24.75), (  4.99, 21, 26), Pigment(color=Colors.Red)),
        )
    obj= Difference( # two exits 180 degrees
        Box((-25,    0,     -25),    ( 25,    20,  25)),
        exits
    )
    return obj

def five_by_five_edge(highlight_exits=False): # three exits
    exits = Union(
        Box(( -4.99, 10.01, -24.75), (  4.99, 21, -26)),
        Box(( -4.99, 10.01,  24.75), (  4.99, 21, 26)),
        Box((-24.75, 10.01,  -4.99), (-26,    21,   4.99)),
    )
    if highlight_exits:
        exits = Union(
            Box(( -4.99, 10.01, -24.75), (  4.99, 21, -26), Pigment(color=Colors.Red)),
            Box(( -4.99, 10.01,  24.75), (  4.99, 21, 26), Pigment(color=Colors.Red)),
            Box((-24.75, 10.01,  -4.99), (-26,    21,   4.99), Pigment(color=Colors.Red)),
        )
    obj = Difference(
        Box((-25,    0,     -25),    ( 25,    20,  25)),
        exits,
    )
    return obj

def five_by_five_dead_end(highlight_exits=False): # one exit
    exits = Object(
        Box(( -4.99, 10.01, -24.75), (  4.99, 21, -26))
    )
    if highlight_exits:
        exits = Object(
            Box(( -4.99, 10.01, -24.75), (  4.99, 21, -26), Pigment(color=Colors.Red)),
        )
    obj = Difference(
        Box((-25,    0,     -25),    ( 25,    20,  25)),
        exits,
    )
    return obj

def five_by_ten(highlight_exits=False):
    exits = Union(
        Box((-49.75, 10.01,  -2.499), (-51,     21,   2.499)),
        Box(( 49.75, 10.01,  -2.499), ( 51,     21,   2.499)),
    )
    if highlight_exits:
        exits = Union(
            Box((-49.75, 10.01,  -2.499), (-51,     21,   2.499), Pigment(color=Colors.Red)),
            Box(( 49.75, 10.01,  -2.499), ( 51,     21,   2.499), Pigment(color=Colors.Red)),
        )
    obj = Difference(
        Box((-50, -0, -25), (50, 20, 25)),
        exits
    )
    return obj

def ten_by_ten(highlight_exits=False):
    obj = Difference(
        Box((-50, -0, -50), (50, 20, 50)),
    )
    return obj

def ten_by_twenty(highlight_exits=False):
    obj = Difference(
    )
    return obj

def twenty_by_twenty(highlight_exits=False):
    obj = Difference(
    )
    return obj
