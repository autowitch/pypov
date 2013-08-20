from pypov.pov import Texture, Pigment
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
            Object(five_by_ten_edge(), cross_hatch_texture),
            Union(
                Box(( -22.5, 10.0001,  0), ( -27.5, 21, -26)),
                Box((  22.5, 10.0002,  0), (  27.5, 21, -26)),
                Box((  -51, 10,  -2.5), (51, 21,   2.5)),
                Box((-20, 10.000003, -20), ( 20, 21,  20)),
                wall_texture_1
            ),

        ),
        Sphere((0, 20, 0), 15,
            Pigment("rgbt 1"),
            """
             hollow
             interior{
                media{ method 3
                       emission 0.6
                       scattering{ 1,
                          <1,1,1>*3.00
                          // extinction  1.50
                       }
                       density{ spherical
                                turbulence 0.85
                                color_map {
                                [0.00 rgb 0]
                                [0.05 rgb 0]
                                [0.20 rgb 0.2]
                                [0.30 rgb 0.6]
                                [0.40 rgb 1]
                                [1.00 rgb 1]
                               }
                       }
                       samples 1,1
                       intervals 3
                       confidence .9
                 }
              }
            """,
        ),
    )
    return geomorph
