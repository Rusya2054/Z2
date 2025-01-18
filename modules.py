import numpy as np
import matplotlib.pyplot as plt
import math
from typing import List

def get_points_from_blender(path: str) -> List[List[float]]:
    """
    Reads a 3D model file in OBJ format and extracts vertexes coordinates.
    :param path: A string representing the file path to the OBJ file.
    :return: A list of lists, where each inner list contains the coordinates (x, y, z) of a vertexes.
    
    Returns an empty list if the file is not in OBJ format or if no vertices are found.
    """
    vertexes = []
    if not path.endswith(".obj"):
        return vertexes
    with open(path) as f:
        for line in f:
            if line.startswith('v '):
                # vertexes.append([float(i) for i in line.split()[1:]] + [1])
                vertexes.append([float(i) for i in line.split()[1:]])
    return vertexes


def plot_3d_points(vertexes: List[List[float]]) -> None:
    """
    Plots a 3D scatter plot of a given list of 3D points.
        This function takes a list of 3D points, where each point is represented as a list of three
    floats and creates a 3D scatter plot using matplotlib.

    :param vertexes:  A list of lists, where each inner list contains Cartesian coordinates [x, y, z]
    :return: None: This function does not return anything. It displays the 3D scatter plot directly.

    """
    figure = plt.figure()
    ax = figure.add_subplot(111, projection='3d')
    x, y, z = [], [], []
    for i in vertexes:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    ax.scatter(x, y, z)
    plt.show()


def cartesian_to_cylinder(vertexes: List[List[float]], value: float = 1.0) -> List[List[float]]:
    """
    Converts Cartesian coordinates (x, y, z) to cylindrical coordinates (r, θ, z).

    :param vertexes: A list of lists, where each inner list contains Cartesian coordinates [x, y, z]
    :param value: A scaling factor for the radial distance (default is 1.0).
    :return: A list of lists, where each inner list contains cylindrical coordinates [r, θ, z].
    angle θ in degrees.
    """
    new_vertexes = []
    """
    -> 1. Calculate the radial distance (r) using the Euclidean
        distance formula: r = value * sqrt(x² + y²).
    -> 2. Calculate the azimuthal angle (θ) using the arctangent function:
        θ = atan2(y, x) * (180 / π) to convert radians to degrees.
    -> 3. Keep the z-coordinate unchanged.
    """
    for i in vertexes:

        new_vertexes.append([value * np.sqrt(pow(i[0], 2) + pow(i[1], 2)),
                             math.atan2(i[1], i[0]) * (180 / np.pi), i[2]])
    return new_vertexes


def cylinder_to_cartesian(vertexes: List[List[float]])-> List[List[float]]:
    """
    Converts cylindrical coordinates (r, θ, z) to Cartesian coordinates (x, y, z).

    :param vertexes: A list of lists, where each inner list contains cylindrical coordinates [r, θ, z]. angel θ in degrees
    :return:
    """
    new_vertexes = []
    """
    -> 1. Calculate x = r * cos(θ), where θ is converted from degrees to radians.
    -> 2. Calculate y = r * sin(θ), where θ is converted from degrees to radians.
    -> 3. Keep the z-coordinate unchanged.
    """
    for i in vertexes:
        new_vertexes.append([i[0] * np.cos(i[1] * np.pi / 180), i[0] * np.sin(i[1] * np.pi / 180), i[2]])
    return new_vertexes


def z_rescaling(vertexes: List[List[float]], value: float = 1.0) -> List[List[float]]:
    """
    Rescales the z-coordinate of each vertex by a given scaling factor.

    :param vertexes: A list of lists, where each inner list contains coordinates [x, y, z] or [r, θ, z].
    :param value: A scaling factor for the z-coordinate (default is 1.0).
    :return: A list of lists, where each inner list contains the rescaled
     coordinates [x, y, z * value] or [r, θ, z * value]
    """
    new_vertexes = []
    for i in vertexes:
        new_vertexes.append([i[0], i[1], i[2] * value])
    return new_vertexes
