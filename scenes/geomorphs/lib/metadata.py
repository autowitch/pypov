class Metadata(object):
    """docstring for Metadata"""
    def __init__(self, name, shortcode, description=None, block_type="normal",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=False,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False):

        super(Metadata, self).__init__()

        # Indicates Y position of the bottom of the geomorph
        self.bottom = bottom

        # Indicates the Y position of the top of the geomorph

        self.top = top
        self.name = name

        # Shortcodes are a quick way to include the block in a config file
        # So, if you are
        self.shortcode = shortcode
        self.description = description

        # Block types really only apply to 5x5 blocks. They are: "dead end",
        # "corner", "tee", and "normal"
        self.block_type = block_type

        # Repeatable geomorphs can be used more than once when constructing a
        # random dungeon

        self.repeatble = repeatable

        # Fully connected geomorphs have all entrances connected to each other
        self.fully_connected = fully_connected

        # Dead end geomorphs have at least one entrance that connects to no
        # other entrances
        self.dead_ends = dead_ends

        # The size indicates the tile size of the geomorph. The legal values are
        # 5x5, 10x5, and 10x10. 10x20 and 20x20 tiles can also be used. These
        # latter two tiles are considered special.
        self.size = size

        # Set to true if this is an entrance
        self.entrance = entrance

        # has_rooms indicates if the tile contains rooms
        self.has_rooms = has_rooms

        # The passage type indicates the type of passages found in the tile
        # These are "hewn", "natural", "mixed"
        self.passage_type = passage_type

        # Indicates that water is found in the tile
        self.wet = wet

    @property
    def deep(self):
        return self.bottom < -20

    @property
    def tall(self):
        return self.top > 40

