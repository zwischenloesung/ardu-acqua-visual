"""
MODULE:       hygrometer
PURPOSE:      visualize a hygrometer
AUTHOR(S):    michael lustenberger inofix.ch
COPYRIGHT:    (C) 2017 by Michael Lustenberger and the INOFIX GmbH

              This program is free software under the GNU General Public
              License (v3).
"""

from __future__ import division
from visual import box, materials, label

class GlassOfWater(object):
    """
    Create a box visualizing the relative humidity.
    """

    def __init__(self, pos=(-20,-10,10), axis=(0,5,1), length=8, height=8,\
                                                                    width=8):
        """
        Construct it with a preset or given geometry.
        """
        # calibration (see: calibrate(value))
        self.zero = None

        # color and material
        glass_color = (0,1,1)
        liquid_color = (0,0.8,1)
        glass_opacity = 0.5
        liquid_opacity = 0.5
        glass_material = materials.rough
        liquid_material = materials.rough

        # visualize the empty container
        self.glass = cylinder(pos=pos, axis=axis, radius=radius, length=length,\
                            color=glass_color, opacity=glass_opacity,\
                            material=glass_material)
        # visualize the liquid (just a little to start with)
        self.liquid = cylinder(pos=pos, axis=axis, radius=radius, length=.1,\
                            color=liquid_color, opacity=liquid_opacity,\
                            material=liquid_material)
        # add a label
        p = calc_label_pos(pos)
        self.label = label(pos=p, text='W: 0.0cm')

    def calc_label_pos(pos):
        """
        Explicit calculation of the label position to the
        lower right, relative to the main object.
        """
        p = (pos[0]+8,pos[1]+5,pos[2]+2)
        return p

    def calibrate(value):
        """
        Calibrate the sensor to a certain initial value.
        """
        pass

    def display_value(value):
        """
        Set the display to visualize the sensor measurement
        """
        pass

