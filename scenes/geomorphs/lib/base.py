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
        Box((-25.00001,     0,    -25.00001),    ( 25.00001,     20,  25.00001)),
        exits
    )
    return obj

def five_by_five_corner(highlight_exits=False):
    exits = Union(
        Box(( -2.499, 10.01, -24.75), (  2.499, 21, -26)),
        Box((-24.75, 10.01,  -2.499), (-26,    21,   2.499)),
    )
    if highlight_exits:
        exits = Union(
            Box(( -4.99, 10.01, -24.75), (  4.99, 21, -26), Pigment(color=Colors.Red)),
            Box((-24.75, 10.01,  -4.99), (-26,    21,   4.99), Pigment(color=Colors.Red)),
        )
    obj = Difference( # two exits 90 degrees
        Box((-25.00001,    0,     -25.00001),    ( 25.00001,    20,  25.00001)),
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
        Box((-25.00001,    0,     -25.00001),    ( 25.00001,    20,  25.00001)),
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
        Box((-25.00001,    0,     -25.00001),    ( 25.00001,    20,  25.00001)),
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
        Box((-25.00001,    0,     -25.00001),    ( 25.00001,    20,  25.00001)),
        exits,
    )
    return obj

def five_by_ten_edge(highlight_exits=False):
    exits = Union(
        # Ends
        Box((-49.75, 10.01,  -2.499), (-51,     21,   2.499)),
        Box(( 49.75, 10.01,  -2.499), ( 51,     21,   2.499)),

        # Sides
        Box((22.5, 10.01, -24.75), (27.5, 21, -26)),
        Box((-22.5, 10.01, -24.75), (-27.5, 21, -26)),
    )
    if highlight_exits:
        exits = Union(
            Box((-49.75, 10.01,  -2.499), (-51,     21,   2.499), Pigment(color=Colors.Red)),
            Box(( 49.75, 10.01,  -2.499), ( 51,     21,   2.499), Pigment(color=Colors.Red)),

            # Sides
            Box((22.5, 10.01, -24.75), (27.5, 21, -26), Pigment(color=Colors.Red)),
            Box((-22.5, 10.01, -24.75), (-27.5, 21, -26), Pigment(color=Colors.Red)),
        )
    obj = Difference(
        Box((-50.00001, -0, -25.00001), (50.00001, 20, 25.00001)),
        exits
    )
    return obj

def five_by_ten_full(highlight_exits=False):
    exits = Union(
        # Ends
        Box((-49.75, 10.01,  -2.499), (-51,     21,   2.499)),
        Box(( 49.75, 10.01,  -2.499), ( 51,     21,   2.499)),

        # Sides
        Box((22.5, 10.01, -24.75), (27.5, 21, -26)),
        Box((-22.5, 10.01, -24.75), (-27.5, 21, -26)),
        Box((22.5, 10.01, 24.75), (27.5, 21, 26)),
        Box((-22.5, 10.01, 24.75), (-27.5, 21, 26)),
    )
    if highlight_exits:
        exits = Union(
            # Ends
            Box((-49.75, 10.01,  -2.499), (-51,     21,   2.499), Pigment(color=Colors.Red)),
            Box(( 49.75, 10.01,  -2.499), ( 51,     21,   2.499), Pigment(color=Colors.Red)),

            # Sides
            Box((22.5, 10.01, -24.75), (27.5, 21, -26), Pigment(color=Colors.Red)),
            Box((-22.5, 10.01, -24.75), (-27.5, 21, -26), Pigment(color=Colors.Red)),
            Box((22.5, 10.01, 24.75), (27.5, 21, 26), Pigment(color=Colors.Red)),
            Box((-22.5, 10.01, 24.75), (-27.5, 21, 26), Pigment(color=Colors.Red)),
        )
    obj = Difference(
        Box((-50.00001, -0, -25.00001), (50.00001, 20, 25.00001)),
        exits
    )
    return obj

def ten_by_ten(highlight_exits=False):
    exits = Union(
        # Ends
        Box((-49.75, 10.01, -22.5), (-51, 21, -27.5)),
        Box((49.75, 10.01, -22.5), (51, 21, -27.5)),
        Box((-49.75, 10.01, 22.5), (-51, 21, 27.5)),
        Box((49.75, 10.01, 22.5), (51, 21, 27.5)),

        # Sides
        Box((22.5, 10.01, -49.75), (27.5, 21, -51)),
        Box((-22.5, 10.01, -49.75), (-27.5, 21, -51)),
        Box((22.5, 10.01, 49.75), (27.5, 21, 51)),
        Box((-22.5, 10.01, 49.75), (-27.5, 21, 51)),
    )
    if highlight_exits:
        exits = Union(
            # Ends
            Box((-49.75, 10.01, -22.5), (-51, 21, -27.5), Pigment(color=Colors.Red)),
            Box((49.75, 10.01, -22.5), (51, 21, -27.5), Pigment(color=Colors.Red)),
            Box((-49.75, 10.01, 22.5), (-51, 21, 27.5), Pigment(color=Colors.Red)),
            Box((49.75, 10.01, 22.5), (51, 21, 27.5), Pigment(color=Colors.Red)),

            # Sides
            Box((22.5, 10.01, -49.75), (27.5, 21, -51), Pigment(color=Colors.Red)),
            Box((-22.5, 10.01, -49.75), (-27.5, 21, -51), Pigment(color=Colors.Red)),
            Box((22.5, 10.01, 49.75), (27.5, 21, 51), Pigment(color=Colors.Red)),
            Box((-22.5, 10.01, 49.75), (-27.5, 21, 51), Pigment(color=Colors.Red)),
        )
    obj = Difference(
        Box((-50.00001, -0, -50.00001), (50.00001, 20, 50.00001)),
        exits,
    )
    return obj

def ten_by_twenty(highlight_exits=False):
    exits = Union(
        # Ends
        Box((-99.75, 10.01, -22.5), (-101, 21, -27.5)),
        Box((99.75, 10.01, -22.5), (101, 21, -27.5)),
        Box((-99.75, 10.01, 22.5), (-101, 21, 27.5)),
        Box((99.75, 10.01, 22.5), (101, 21, 27.5)),

        # Sides
        Box((22.5, 10.01, -49.75), (27.5, 21, -51)),
        Box((-22.5, 10.01, -49.75), (-27.5, 21, -51)),
        Box((22.5, 10.01, 49.75), (27.5, 21, 51)),
        Box((-22.5, 10.01, 49.75), (-27.5, 21, 51)),

        Box((72.5, 10.01, -49.75), (77.5, 21, -51)),
        Box((-72.5, 10.01, -49.75), (-77.5, 21, -51)),
        Box((72.5, 10.01, 49.75), (77.5, 21, 51)),
        Box((-72.5, 10.01, 49.75), (-77.5, 21, 51)),
    )
    if highlight_exits:
        exits = Union(
            # Ends
            Box((-99.75, 10.01, -22.5), (-101, 21, -27.5), Pigment(color=Colors.Red)),
            Box((99.75, 10.01, -22.5), (101, 21, -27.5), Pigment(color=Colors.Red)),
            Box((-99.75, 10.01, 22.5), (-101, 21, 27.5), Pigment(color=Colors.Red)),
            Box((99.75, 10.01, 22.5), (101, 21, 27.5), Pigment(color=Colors.Red)),

            # Sides
            Box((22.5, 10.01, -49.75), (27.5, 21, -51), Pigment(color=Colors.Red)),
            Box((-22.5, 10.01, -49.75), (-27.5, 21, -51), Pigment(color=Colors.Red)),
            Box((22.5, 10.01, 49.75), (27.5, 21, 51), Pigment(color=Colors.Red)),
            Box((-22.5, 10.01, 49.75), (-27.5, 21, 51), Pigment(color=Colors.Red)),

            Box((72.5, 10.01, -49.75), (77.5, 21, -51), Pigment(color=Colors.Red)),
            Box((-72.5, 10.01, -49.75), (-77.5, 21, -51), Pigment(color=Colors.Red)),
            Box((72.5, 10.01, 49.75), (77.5, 21, 51), Pigment(color=Colors.Red)),
            Box((-72.5, 10.01, 49.75), (-77.5, 21, 51), Pigment(color=Colors.Red)),
        )
    obj = Difference(
        Box((-100.00001, -0, -50.00001), (100.00001, 20, 50.00001)),
        exits,
    )
    return obj

def twenty_by_twenty(highlight_exits=False):
    exits = Union(
        # Ends
        Box((-99.75, 10.01, -22.5), (-101, 21, -27.5)),
        Box((99.75, 10.01, -22.5), (101, 21, -27.5)),
        Box((-99.75, 10.01, 22.5), (-101, 21, 27.5)),
        Box((99.75, 10.01, 22.5), (101, 21, 27.5)),


        Box((-99.75, 10.01, -72.5), (-101, 21, -77.5)),
        Box((99.75, 10.01, -72.5), (101, 21, -77.5)),
        Box((-99.75, 10.01, 72.5), (-101, 21, 77.5)),
        Box((99.75, 10.01, 72.5), (101, 21, 77.5)),

        # Sides
        Box((22.5, 10.01, -99.75), (27.5, 21, -101)),
        Box((-22.5, 10.01, -99.75), (-27.5, 21, -101)),
        Box((22.5, 10.01, 99.75), (27.5, 21, 101)),
        Box((-22.5, 10.01, 99.75), (-27.5, 21, 101)),

        Box((72.5, 10.01, -99.75), (77.5, 21, -101)),
        Box((-72.5, 10.01, -99.75), (-77.5, 21, -101)),
        Box((72.5, 10.01, 99.75), (77.5, 21, 101)),
        Box((-72.5, 10.01, 99.75), (-77.5, 21, 101)),
    )
    if highlight_exits:
        exits = Union(
            # Ends
            Box((-99.75, 10.01, -22.5), (-101, 21, -27.5), Pigment(color=Colors.Red)),
            Box((99.75, 10.01, -22.5), (101, 21, -27.5), Pigment(color=Colors.Red)),
            Box((-99.75, 10.01, 22.5), (-101, 21, 27.5), Pigment(color=Colors.Red)),
            Box((99.75, 10.01, 22.5), (101, 21, 27.5), Pigment(color=Colors.Red)),

            Box((-99.75, 10.01, -72.5), (-101, 21, -77.5), Pigment(color=Colors.Red)),
            Box((99.75, 10.01, -72.5), (101, 21, -77.5), Pigment(color=Colors.Red)),
            Box((-99.75, 10.01, 72.5), (-101, 21, 77.5), Pigment(color=Colors.Red)),
            Box((99.75, 10.01, 72.5), (101, 21, 77.5), Pigment(color=Colors.Red)),

            # Sides
            Box((22.5, 10.01, -99.75), (27.5, 21, -101), Pigment(color=Colors.Red)),
            Box((-22.5, 10.01, -99.75), (-27.5, 21, -101), Pigment(color=Colors.Red)),
            Box((22.5, 10.01, 99.75), (27.5, 21, 101), Pigment(color=Colors.Red)),
            Box((-22.5, 10.01, 99.75), (-27.5, 21, 101), Pigment(color=Colors.Red)),

            Box((72.5, 10.01, -99.75), (77.5, 21, -101), Pigment(color=Colors.Red)),
            Box((-72.5, 10.01, -99.75), (-77.5, 21, -101), Pigment(color=Colors.Red)),
            Box((72.5, 10.01, 99.75), (77.5, 21, 101), Pigment(color=Colors.Red)),
            Box((-72.5, 10.01, 99.75), (-77.5, 21, 101), Pigment(color=Colors.Red)),
        )
    obj = Difference(
        Box((-100.00001, -0, -100.00001), (100.00001, 20, 100.00001)),
        exits,
    )
    return obj
