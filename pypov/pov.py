
# This code was adapted from:
## {{{ http://code.activestate.com/recipes/205451/ (r1)

import sys
import os
import subprocess
import argparse
import datetime

def parse_args(parser=None):

    if not parser:
        parser = argparse.ArgumentParser(description='Python POV processor',
                prefix_chars='+-')

    parser.add_argument('-H', '--height',
                        type=int,
                        default=Overrides.height,
                        dest='height',
                        help="height [%d]" % Overrides.height)
    parser.add_argument('-W', '--width',
                        type=int,
                        default=Overrides.width,
                        dest='width',
                        help="width [%d]" % Overrides.width)

    parser.add_argument('-r', '--radiosity',
                        default=None,
                        action='store_false',
                        dest='use_radiosity',
                        help='Turn off radisosity (if it is used in the scene)')
    parser.add_argument('+r', '++radiosity',
                        default=None,
                        action='store_true',
                        dest='use_radiosity',
                        help='Turn on radisosity (if it is used in the scene)')

    parser.add_argument('-l', '--camera-location',
                        nargs=3,
                        type=float,
                        default=None,
                        dest='camera_location',
                        metavar=('X', 'Y', 'Z'),
                        help='Set camera location')
    parser.add_argument('-L', '--camera-look-at',
                        nargs=3,
                        type=float,
                        default=None,
                        dest='camera_look_at',
                        metavar=('X', 'Y', 'Z'),
                        help='Set target of camera')
    parser.add_argument('-a', '--camera_angle',
                        default=None,
                        type=int,
                        dest='camera_angle',
                        help="set the camera angle")

    parser.add_argument('-d', '--display',
                        default=None,
                        action='store_false',
                        dest='display',
                        help='Do not display the render as it renders')
    parser.add_argument('+d', '++display',
                        default=None,
                        action='store_true',
                        dest='display',
                        help='Display the render as it renders')

    parser.add_argument('-p', '--pause',
                        default=None,
                        action='store_false',
                        dest='pause',
                        help='Do not pause after rendering')
    parser.add_argument('+p', '++pause',
                        default=None,
                        action='store_false',
                        dest='pause',
                        help='Pause after rendering')

    parser.add_argument('-v', '--verbose', action='count',
                        dest='verbose',
                        default=0,
                        help='debug level (repeat to increase detail)')

    args = parser.parse_args()

    # Create a closure that makes a very simple logger
    def make_log_fn(master_level):

        """ Create a simple logger """

        def log_fn(level, msg):

            """ A very simple logger """

            if level == 'ERROR':
                print >> sys.stderr, "ERROR: %s" % msg
            elif level <= master_level:
                print "%s %2d %s" % (datetime.datetime.now(), level, msg)

        return log_fn

    args.log = make_log_fn(args.verbose)

    args.log(5, "Run environment %s" % args)

    Overrides.update_overrides(args)

    return args


class Overrides(object):

    override_radiosity = False
    use_radiosity = None
    override_camera = False
    camera_look_at = None
    camera_location = None
    camera_angle = 60

    width = 640
    height = 480
    verbose = False
    warning_level = 5
    quality = 9
    antialias = 0.3
    sampling_method = 2
    jitter = 1
    antialias_depth = 2
    output_alpha = False
    light_buffer = False
    vista_buffer = False
    create_ini = False
    display = True
    pause = True

    @staticmethod
    def update_overrides(args):
        if args.camera_angle != Overrides.camera_angle or \
                args.camera_location != None or \
                args.camera_look_at != None:
            Overrides.override_camera = True
            Overrides.camera_angle = args.camera_angle
            Overrides.camera_location = args.camera_location
            Overrides.camera_look_at = args.camera_look_at

        if args.display != None:
            Overrides.display = args.display

        Overrides.height = args.height
        Overrides.width = args.width

        if args.pause != None:
            Overrides.pause = args.pause

        if args.use_radiosity != None:
            Overrides.override_radiosity = True
            Overrides.use_radiosity = args.use_radiosity


class Settings(object):

    """docstring for Settings"""

    def __init__(self):
        super(Settings, self).__init__()
        self.width = Overrides.width
        self.height = Overrides.height
        self.verbose = Overrides.verbose
        self.warning_level = Overrides.warning_level
        self.quality = Overrides.quality
        self.antialias = Overrides.antialias
        self.sampling_method = Overrides.sampling_method
        self.jitter = Overrides.jitter
        self.antialias_depth = Overrides.antialias_depth
        self.output_alpha = Overrides.output_alpha
        self.light_buffer = Overrides.light_buffer
        self.vista_buffer = Overrides.vista_buffer
        self.create_ini = Overrides.create_ini
        self.display = Overrides.display
        self.pause = Overrides.pause


class SettingsCollection(object):

    """docstring for SettingsCollection"""

    def __init__(self):
        super(SettingsCollection, self).__init__()
        self.settings = {}

    def load(self, filename):
        pass

    def save(self, filename):
        pass


class POV(object):

    """docstring for POV"""

    def __init__(self):
        super(POV, self).__init__()
        self.library_path = []

    def _build_command_line(self, settings):
        cmd = ['povray']
        cmd += ['-W%s' % settings.width]
        cmd += ['-H%s' % settings.height]
        cmd += ['-Q%s' % settings.quality]
        cmd += ['-A%s' % settings.antialias]
        if settings.display:
            cmd += ['+d']
        if settings.pause:
            cmd += ['+P']
        return cmd

    def render(self, pov_file, settings, animation_settings=False):
        pov_file.close()
        parms = self._build_command_line(settings)
        print parms

        pov_cmd = subprocess.Popen(parms + ['-I%s' % pov_file.fname, '-Oout.png'])
        pov_output = pov_cmd.communicate()[0]
        print pov_output


class File:

    def __init__(self, fname="out.pov", *items):
        self.pov_file = open(fname, "w")
        self.fname = fname
        self.__indent = 0
        self.write(*items)

    def include(self, name):
        self.writeln( '#include "%s"' % name )
        self.writeln()

    def indent(self):
        self.__indent += 1

    def dedent(self):
        self.__indent -= 1
        assert self.__indent >= 0

    def block_begin(self, use_block=True):
        if use_block:
            self.writeln("{")
        self.indent()

    def block_end(self, use_block=True):
        self.dedent()
        if use_block:
            self.writeln("}")
        if self.__indent == 0:
            # blank line if this is a top level end
            self.writeln()

    def write(self, *items):
        for item in items:
            if type(item) == str:
                self.include(item)
            else:
                item.write(self)

    def writeln(self, s=""):
        #print "    "*self.__indent+s
        self.pov_file.write("    "*self.__indent + s + os.linesep)

    def close(self):
        self.pov_file.close()


class Vector:

    def __init__(self, *args):
        if len(args) == 1:
            self.vector = args[0]
        else:
            self.vector = args

    def __str__(self):
        return "<%s>" % (", ".join([str(x) for x in self.vector]))

    def __repr__(self):
        return "Vector(%s)" % self.vector

    def __mul__(self, other):
        return Vector([r * other for r in self.vector])

    def __rmul__(self, other):
        return Vector([r * other for r in self.vector])


class Item:

    def __init__(self, name, args=[], opts=[], use_block=True, comment=False,
            **kwargs):
        self.name = name
        args = list(args)
        for i in range(len(args)):
            if type(args[i]) == tuple or type(args[i]) == list:
                args[i] = Vector(args[i])
        self.args = args
        self.opts = opts
        self._use_block = use_block
        self._comment = comment
        self.kwargs = kwargs

    def append(self, item):
        # self.opts.append(item)
        self.opts += (item, )

    def write(self, pov_file):
        if self._comment:
            pov_file.writeln('/*')

        pov_file.writeln(self.name)
        pov_file.block_begin(self._use_block)
        if self.args:
            pov_file.writeln(", ".join([str(arg) for arg in self.args]))

        for opt in self.opts:
            if hasattr(opt, "write"):
                opt.write(pov_file)
            else:
                pov_file.writeln(str(opt))

        for key, val in self.kwargs.items():
            if type(val) == tuple or type(val) == list:
                val = Vector(*val)
                pov_file.writeln("%s %s"%(key, val))
            else:
                pov_file.writeln("%s %s"%(key, val))
        pov_file.block_end(self._use_block)

        if self._comment:
            pov_file.writeln('*/')

    def __setattr__(self, name, val):
        self.__dict__[name] = val
        if name not in ["kwargs", "args", "opts", "name"] and \
                not name.startswith('_'):
            self.__dict__["kwargs"][name] = val

    def __setitem__(self, i, val):
        if i < len(self.args):
            self.args[i] = val
        else:
            i += len(self.args)
            if i < len(self.opts):
                self.opts[i] = val

    def __getitem__(self, i, val):
        if i < len(self.args):
            return self.args[i]
        else:
            i += len(self.args)
            if i < len(self.opts):
                return self.opts[i]

class Object(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "object", (), opts, **kwargs)

class GlobalSettings(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "global_settings", (), opts, **kwargs)

class Radiosity(Item):
    def __init__(self, *opts, **kwargs):
        if Overrides.override_radiosity and not Overrides.use_radiosity:
            Item.__init__(self, "radiosity", (), opts, comment=True, **kwargs)
        else:
            Item.__init__(self, "radiosity", (), opts, **kwargs)

class Texture(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "texture", (), opts, **kwargs)

class Material(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "material", (), opts, **kwargs)

class Interior(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "interior", (), opts, **kwargs)

class Pigment(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "pigment", (), opts, **kwargs)

class Checker(Item):
    def __init__(self, a, b, *opts, **kwargs):
        Item.__init__(self, "checker", (a, b), opts, use_block=False, **kwargs)

class Brick(Item):
    def __init__(self, a, b, *opts, **kwargs):
        Item.__init__(self, "brick", (a, b), opts, use_block=False, **kwargs)

class Wrinkles(Item):
    def __init__(self, a, *opts, **kwargs):
        Item.__init__(self, "wrinkles", (a), opts, use_block=False, **kwargs)

class Finish(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "finish", (), opts, **kwargs)


class Normal(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "normal", (), opts, **kwargs)

class SkySphere(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "sky_sphere", (), opts, **kwargs)

class Camera(Item):
    def __init__(self, *opts, **kwargs):
        if Overrides.override_camera:
            if Overrides.camera_look_at != None:
                kwargs['look_at'] = (Overrides.camera_look_at[0],
                        Overrides.camera_look_at[1],
                        Overrides.camera_look_at[2])
            if Overrides.camera_location != None:
                kwargs['location'] = (Overrides.camera_location[0],
                        Overrides.camera_location[1],
                        Overrides.camera_location[2])
            if Overrides.camera_angle != None:
                kwargs['angle'] = Overrides.camera_angle
        Item.__init__(self, "camera", (), opts, **kwargs)


class LightSource(Item):
    def __init__(self, v, *opts, **kwargs):
        Item.__init__(self, "light_source", (Vector(v), ), opts, **kwargs)


class Background(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "background", (), opts, **kwargs)

# Finite Solid Primitives

class Blob_Sphere(Item):
    def __init__(self, v, r, strength, *opts, **kwargs):
        Item.__init__(self, "sphere", (v, r, strength), opts, **kwargs)

class Blob_Cylinder(Item):
    def __init__(self, v1, v2, r, strength, *opts, **kwargs):
        Item.__init__(self, "cylinder", (v1, v2, r, strength), opts, **kwargs)

class Blob(Item):
    def __init__(self, blob_items, *opts, **kwargs):
        for x in blob_items:
            if x is not Blob_Sphere and x is not Blob_Cylinder:
                raise "%s must be Blob_Sphere or Blob_Cylinder"
        Item.__init__(self, "blob", blob_items, opts, **kwargs)

class Box(Item):
    def __init__(self, v1, v2, *opts, **kwargs):
        #self.v1 = Vector(v1)
        #self.v2 = Vector(v2)
        Item.__init__(self, "box", (v1, v2), opts, **kwargs)


class Cylinder(Item):
    def __init__(self, v1, v2, r, *opts, **kwargs):
        " opts: open "
        Item.__init__(self, "cylinder", (v1, v2, r), opts, **kwargs)


class Plane(Item):
    def __init__(self, v, r, *opts, **kwargs):
        Item.__init__(self, "plane", (v, r), opts, **kwargs)


class Torus(Item):
    def __init__(self, r1, r2, *opts, **kwargs):
        Item.__init__(self, "torus", (r1, r2), opts, **kwargs)


class Cone(Item):
    def __init__(self, v1, r1, v2, r2, *opts, **kwargs):
        " opts: open "
        Item.__init__(self, "cone", (v1, r1, v2, r2), opts, **kwargs)

class Polygon_4(Item):
    def __init__(self, a, b, c, d, *opts, **kwargs):
        Item.__init__(self, "polygon", (5, a, b, c, d, a), opts, **kwargs)


class Sphere(Item):
    def __init__(self, v, r, *opts, **kwargs):
        Item.__init__(self, "sphere", (v, r), opts, **kwargs)

class Isosurface(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "isosurface", opts, **kwargs)

class Function(Item):
    def __init__(self, f, *opts, **kwargs):
        Item.__init__(self, "function", (f), opts, **kwargs)

# CSG

class Union(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "union", (), opts, **kwargs)


class Intersection(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "intersection", (), opts, **kwargs)


class Difference(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "difference", (), opts, **kwargs)


class Merge(Item):
    def __init__(self, *opts, **kwargs):
        Item.__init__(self, "merge", (), opts, **kwargs)


