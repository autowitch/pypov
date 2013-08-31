from pypov.pov import Vector, Texture, Pigment, POV, File, Camera, Cylinder
from pypov.pov import LightSource, Sphere, Finish, Settings, Plane, Box, Cone
from pypov.pov import Checker, SkySphere, Union, GlobalSettings, Radiosity
from pypov.pov import Polygon_4, Difference, Object, parse_args

dark_glass = Texture(
    Pigment(color=(0.025, 0.025, 0.025)),
    Finish(reflection=0.05)
)

grass = Texture(Pigment(color=(0, 1, 0)))


def general(pov_file):
    GlobalSettings(
        Radiosity(
            pretrace_start = 0.08,
            pretrace_end   = 0.005,
            count = 400,
#            nearest_count = 5,
            error_bound = 0.1,
            recursion_limit = 1,
#            low_error_factor = .5,
#            gray_threshold = 0.0,
#            minimum_reuse = 0.015,
#            brightness = 1,
#            adc_bailout = 0.01/2,
            media="on",
        ),
        assumed_gamma = 1.0,
        max_trace_level=100,
        ambient_light = (0.1, 0.1, 0.1),
    ).write(pov_file)

    Camera(
            location=(-600, 150, -110),
            look_at=(0, 25, 0)
#            angle=30
    ).write(pov_file)
    LightSource((100000, 100000, 100000), color=(0.6, 0.6, 0.5)).write(pov_file)
    LightSource((150000, 150000, -100000), color=(0.25, 0.25, 0.3)).write(pov_file)
#    LightSource((-150000, 150000, 100000), color=(0.25, 0.3, 0.25)).write(pov_file)
#    LightSource((-150000, 150000, -100000), color=(0.3, 0.25, 0.25)).write(pov_file)

    pov_file.declare('fn_Pigm', 'function { pigment { agate color_map { [0 color rgb 0] [1 color rgb 1] } } }')


def ground(pov_file, offset=0):
    Plane(
        (0, 1, 0), -0.0,
        Texture(
            Pigment(Checker((0.75, 0.75, 0.75), (1, 1, 1))),
            scale=10
        ),
        translate=(0, -1 * offset, 0)
    ).write(pov_file)
    SkySphere(Pigment(color="MidnightBlue")).write(pov_file)



