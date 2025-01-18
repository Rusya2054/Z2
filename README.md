3D Point Manipulation and Visualization
This Python project provides functionality to read 3D model files in OBJ format, extract vertex coordinates, and perform various coordinate transformations. It also includes a utility to visualize the 3D points using matplotlib.

Features
• Reading OBJ Files: Extracts vertex coordinates from OBJ files.
• 3D Visualization: Plots 3D scatter plots of the extracted points.
• Coordinate Transformations:
    Converts Cartesian coordinates to cylindrical coordinates:
    Converts cylindrical coordinates back to Cartesian coordinates.
• Z-axis Rescaling: Rescales the z-coordinate of each vertex by a given factor.

Dependencies:
• numpy
• matplotlib
• math

Installation:
Ensure you have Python3 >= 3.10.0 installed, then install the required dependencies using pip
• pip install numpy matplotlib

Usage:
• Reading OBJ Files
    vertexes = get_points_from_blender("path/to/your/file.obj")
• Plotting 3D Points
    plot_3d_points(vertexes)
• Coordinate Transformations
    cylindrical_vertexes = cartesian_to_cylinder(vertexes, value=1.0)
• Cylindrical to Cartesian
    cartesian_vertexes = cylinder_to_cartesian(cylindrical_vertexes)
• Z-axis Rescaling
    rescaled_vertexes = z_rescaling(vertexes, value=1.5)
