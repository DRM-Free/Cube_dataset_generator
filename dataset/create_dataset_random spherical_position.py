""" Just a purple sphere """

from vapory import *
import math
# import numpy as np
from numpy import random, vstack

import csv
import os
from math import pi
scene_name = "cube_64_random_spherical_position"


def spherical_to_cartesian(spherical_position):
    r, theta, phi = spherical_position
    x = r * math.sin(theta)*math.cos(phi)
    y = r * math.sin(theta)*math.sin(phi)
    z = r * math.cos(theta)
    return [x, y, z]


def create_scene(camera):
    return Scene(camera,

                 objects=[

                     Background("color", [0.85, 0.75, 0.75]),

                     LightSource([0, 0, 0],
                                 'color', [1, 1, 1],
                                 'translate', [-5, 5, -5]),

                     LightSource([0, 0, 0],
                                 'color', [0.25, 0.25, 0.25],
                                 'translate', [6, -6, -6]),


                     Box([-0.5, -0.5, -0.5], [0.5, 0.5, 0.5],
                         Texture(Pigment('color', [1, 0, 0]),
                                 Finish('specular', 0.6),
                                 Normal('agate', 0.25, 'scale', 0.5)),
                         'rotate', [0, 0, 0])
                 ]
                 )


thetas = random.uniform(0, pi, 5000)
phis = random.uniform(0, 2*pi, 5000)
rs = random.uniform(1.8, 6, 5000)
# the sky position constrains the last rotation angle of the camera when camera position and watched point are determined
skys = random.uniform(-1, 1, [3, 5000])
camerapos = [rs, thetas, phis]
camerapos = vstack(camerapos)

thetas = random.uniform(0, pi, 5000)
phis = random.uniform(0, 2*pi, 5000)
rs = random.uniform(0, 1.8, 5000)
watchedpos = [rs, thetas, phis]
watchedpos = vstack(watchedpos)


if not os.path.isdir("dataset/"+scene_name):
    os.makedirs("dataset/"+scene_name)

if not os.path.isfile("dataset/{0}/camera_data.csv".format(scene_name)):
    os.mknod("dataset/{0}/camera_data.csv".format(scene_name))

with open("dataset/{0}/camera_data.csv".format(scene_name), 'w') as csvfile:
    fieldnames = ['view_no', 'theta', 'phi']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(0, len(thetas)):
        camera_pos = spherical_to_cartesian(camerapos[:, i])
        watched_pos = spherical_to_cartesian(watchedpos[:, i])
        camera = Camera('location',  camera_pos,
                        'direction', [0, 0, 1.5],
                        'look_at', watched_pos,
                        'sky', skys[:, i])
        scene = create_scene(camera)
        writer.writerow(
            {'view_no': i, 'theta': thetas[i], 'phi': phis[i]})

    # We use antialiasing. Remove this option for faster rendering.
        scene.render("dataset/{0}/viewpoint".format(scene_name) + str(i) + '.png', width=64,
                     height=64, antialiasing=0.0001)
