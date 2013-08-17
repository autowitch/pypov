from pypov.pov import Box

def calculate_slice(source_bounding_box, context):
    pass

def slice_ground(metadata_list, context):
    # Will remove a box from the gound plane from the back of the furthest
    # object to the camera - as deep as the camera.

    deepest_object = 0
    x_min = 0
    z_min = 0
    x_max = 0
    z_max = 0
    for x in metadata_list:
        if x.bottom < deepest_object:
            deepest_object = x.bottm

    if deepest_object >= 0:
        # Nothing is deep, no new box is needed
        return None



