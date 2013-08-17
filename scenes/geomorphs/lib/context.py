class Context(object):
    """docstring for Context"""
    def __init__(self, camera_location, slice=True, show_roof=False,
            rock_texture=None):

        super(Context, self).__init__()

        self.camera_location = camera_location
        self.slice = slice
        self.show_roof = show_roof
        self.rock_texture=None

