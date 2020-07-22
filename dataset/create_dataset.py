""" Just a purple sphere """

from vapory import *
import math
import numpy as np
import csv
import os
from numpy import random, vstack


scene_name = "cube_64_R_4_random_angles_test"


def spherical_to_cartesian(r, theta, phi):
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


nb_images = 10
r = 4
# thetas_steps = 200  # theta between 0 and pi
# phis_steps = 10  # Phi between 0 and 2*pi
#thetas = np.linspace(0, math.pi, thetas_steps-1)
#phis = np.linspace(0, 2*math.pi, phis_steps)
#phis = np.tile(phis[0:phis_steps], thetas_steps-1)
thetas = random.uniform(0, math.pi, nb_images)
phis = random.uniform(0, 2*math.pi, nb_images)

if not os.path.isdir("dataset/"+scene_name):
    os.makedirs("dataset/"+scene_name)

if not os.path.isfile("dataset/{0}/camera_data.csv".format(scene_name)):
    os.mknod("dataset/{0}/camera_data.csv".format(scene_name))

with open("dataset/{0}/camera_data.csv".format(scene_name), 'w') as csvfile:
    fieldnames = ['view_no', 'theta', 'phi']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(0, len(thetas)):
        cartesian_coords = spherical_to_cartesian(r, thetas[i], phis[i])
        camera = Camera('location',  cartesian_coords,
                        'direction', [0, 0, 1.5],
                        'look_at', [0, 0, 0])
        scene = create_scene(camera)
        writer.writerow(
            {'view_no': i, 'theta': thetas[i], 'phi': phis[i]})

    # We use antialiasing. Remove this option for faster rendering.
        scene.render("dataset/{0}/viewpoint".format(scene_name) + str(i) + '.png', width=64,
                     height=64, antialiasing=0.0001)
