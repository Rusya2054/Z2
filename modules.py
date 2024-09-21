import numpy as np
import matplotlib.pyplot as plt
import math


def get_info_from_file(path):
    vertex, faces = [], []
    with open(path) as f:
        for line in f:
            if line.startswith('v '):
                # vertex.append([float(i) for i in line.split()[1:]] + [1])
                vertex.append([float(i) for i in line.split()[1:]])

    return vertex


def plotting_3D(array):
    figure = plt.figure()
    ax = figure.add_subplot(111, projection='3d')
    x, y, z = [], [], []
    for i in array:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    ax.scatter(x, y, z)
    plt.show()


def decard_to_cylinder(array, value):
    new_arr = []
    for i in array:
        new_arr.append([value * np.sqrt(pow(i[0], 2) + pow(i[1], 2)), math.atan2(i[1], i[0]) * (180 / np.pi), i[2]])
    return new_arr


def cylinder_to_decard(array):
    new_arr = []
    for i in array:
        new_arr.append([i[0] * np.cos(i[1] * np.pi / 180), i[0] * np.sin(i[1] * np.pi / 180), i[2]])
    return new_arr


def for_Z(array, value):
    new_arr = []
    for i in array:
        new_arr.append([i[0], i[1], i[2] * value])
    return new_arr
