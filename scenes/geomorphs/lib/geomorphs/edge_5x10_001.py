from pypov.pov import Texture, Pigment, Intersection, Cylinder
from pypov.pov import Union, Difference, Object, Box, Sphere

from pypov.common import grey, white
from pypov.colors import Colors
from lib.base import five_by_ten_edge
from lib.textures import cross_hatch, cross_hatch_2, wall_texture_1
from lib.metadata import Metadata

def edge_5x10_001_info():
    return Metadata("Basic corner room", "c2",
            description="Basic boring corner with a room", block_type="corner",
            bottom=0, top=20, size="5x5",
            repeatable=True, fully_connected=True,
            dead_ends=False, entrance=False, has_rooms=True,
            passage_type="hewn", wet=False)

def edge_5x10_001(rotate=(0, 0, 0), translate=(0, 0, 0), detail_level=1,
        cross_hatch_texture=cross_hatch_2):
    """docstring for gm02"""


    # Media definition
    #//-------------------------------------------------------
    #sphere{ <0,0,0>, 1.5  // media container shape
            #// radius increased from 1 to 1.5,
            #// because of turbulent pattern!
            #pigment{ rgbt 1 } // fully transparent
            #hollow // allows fog or media effects inside

     #interior{ //---------------------
        #media{ method 3
               #emission 0.6
               #scattering{ 1, // Type
                  #<1,1,1>*3.00 // color of scattering haze
                  #extinction  1.50
              #// how fast the scattering media absorbs light
              #// useful if the media absorbs too much light
               #} // end scattering
               #density{ spherical
                        #turbulence 0.85
                        #color_map {
                        #[0.00 rgb 0]
                        #[0.05 rgb 0]
                        #[0.20 rgb 0.2]
                        #[0.30 rgb 0.6]
                        #[0.40 rgb 1]
                        #[1.00 rgb 1]
                       #} // end color_map
               #} // end of density
               #samples 1,1   // 3,3 for adaptive sampling
               #intervals 3   // increase up to 15
               #confidence .9 // decrease down to .03
                             #//  for better quality
         #} // end of media ----------------------------------
      #} // end of interior
    #} //----------------------------------------------------

    geomorph = Union(
        Difference(
            Union(
                Object(five_by_ten_edge(), cross_hatch_texture),
            ),
            Union(
                # Halls
                Box(( -22.5, 10.0001,  2.50001), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002,  2.50001), (  27.5, 21, -26)),
                Box((  -27.5, 10.0003,  -2), (23, 15,   2)),
                Cylinder((-27.5, 15, 0), (23, 15, 0), 2),
                Box((  22.50001, 10.0004,  -2.5), (51, 21,   2.5)),
                # Middle room
                Box((-20, 10.000003, -20), ( 20, 21,  20)),

                # End hall
                Box((  -51, 10,  -2.5), (-35, 21,   2.5)),
                # Two end rooms
                Box((-48, 10, -4.5), (-30, 21, -20)),
                Box((-48, 10, 4.5), (-30, 21, 20)),
                # Connecting halls
                Box((-36, 10.0001, -5), (-40, 15, 5)),
                Intersection(
                    Cylinder((-36, 15, -5), (-36, 15, 5), 4),
                    Cylinder((-40, 15, -5), (-40, 15, 5), 4),
                ),
                # Sneaky passage
                Box((-31, 12, -5), (-33, 16, 5)),
                wall_texture_1
            ),
        ),
        # Cloud 1
        Sphere((0, 20, 0), 20,
            Pigment("rgbf 1"),
            """
            hollow
            interior {
                media {
                    method 3
                    emission 0.1
                    scattering {
                        1, <1,1,1>*3.00
                        extinction  1.50
                    }
                    density {
                        spherical
                        turbulence 0.85
                        color_map {
                            [0.00 rgb 0.0]
                            [0.05 rgb 0.0]
                            [0.20 rgb 0.2]
                            [0.30 rgb 0.6]
                            [0.40 rgb 1.0]
                            [1.00 rgb 1.0]
                        }
                    }
                    samples 1,1
                    intervals 3
                    confidence .9
                    scale <10, 10, 10>
                    translate <0, 20, 0>
                }
            }
            """,
        ),
        translate=translate,
        rotate=rotate
    )
    return geomorph
