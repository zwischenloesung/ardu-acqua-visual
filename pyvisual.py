#!/usr/bin/env python

# just to visualize some sensor values..
from __future__ import division
from visual import *
from time import sleep

# registering some globals
os = {}

###
def clean_up():
    for k in os:
        os[k].visible = False

def setup_water():
    # water container
    ## visual empty container
    os["w"] = cylinder(pos=(12,-16,8), axis=(0,5,1), radius=6, length=20, color=(0,1,1), opacity=0.5, material=materials.rough)
    ## visual water
    os["wv"] = cylinder(pos=(12,-16,8), axis=(0,5,1), radius=6, length=.1, color=(0,0.8,1), opacity=0.5, material=materials.rough)
    ## visual label
    os["wt"] = label(pos=(22,-10,10), text='W: 0.0cm')

def set_water(v):
    ## water = max distance .38 m - dist * 100
    n = (.38 - v) * 100
    os["wv"].length = n
    os["wt"].text = 'W: ' + str(n) + 'cm'

def setup_temperature():
    # temperature
    os["ts"] = sphere(pos=(-20,-1,9.8), radius=1.6, color=(1,0,0))
    os["tv"] = cylinder(pos=(-20,0,10), axis=(0,5,1), radius=.6, length=1, color=(1,0,0))
    os["tt"] = label(pos=(-12,4,10), text=u'T: 0\xb0C')

def set_temperature(v):
    tn = v / 2
    os["tv"].length = tn
    os["tt"].text = u'T: ' + str(v) + u'\xb0C'

def setup_humidity():
    os["bv"] = box(pos=(-20,-10,10), axis=(0,5,1), length=8, height=8, width=8, color=(0,0,1), opacity=0.5)
    os["b"] = box(pos=(-20,-10,10), axis=(0,5,1), length=8, height=8, width=8, color=(1,1,1), opacity=0.5)
    os["bt"] = label(pos=(-12,-10,10), axis=(0,5,1), text='H: 100%')

def set_humidity(v):
    bn = v / 10
    os["bv"].length = bn
    os["bv"].height = bn
    os["bv"].width = bn
    os["bt"].text = 'H: ' + str(v) + '%'

setup_water()
setup_temperature()
setup_humidity()

## test values to see how it would look like..
waters = [ .370, .367, .362, .288, .264, .249, .27, .32, .35 ]
temps = [ 18.8, 19.3, 20, 20.1, 19.4 ]
humids = [ 60, 61, 62, 61 ]

## some indices
wi = 0
ti = 0
hi = 0

## a first test run..
while True:
    sleep(1)
    set_water(waters[wi])
    if wi >= len(waters) - 1:
        wi = 0
    else:
        wi += 1
    set_temperature(temps[ti])
    if ti >= len(temps) - 1:
        ti = 0
    else:
        ti += 1
    set_humidity(humids[hi])
    if hi >= len(humids) - 1:
        hi = 0
    else:
        hi += 1
