from modules import *


if __name__ == '__main__':
    vertex = get_points_from_blender(r'Tire.obj')

    # перевод точек в цилиндрическую систему координат
    new_vertexes = cartesian_to_cylinder(vertex, 0.1)
    # перевод точек из цилиндрической в декартову систему координат
    new_vertexes = cylinder_to_cartesian(new_vertexes)

    new_vertexes = z_rescaling(new_vertexes, 10)  # ремаштабирование оси Z

    # получение точек
    model1 = get_points_from_blender(r'rim.obj')
    # new_vertex=cylinder_to_cartesian(new_vertex)
    # print(new_vertex[0])
    # new_vertex=z_rescaling(vertex, 0.0001) #ремаштабирование точки

    plot_3d_points([*model1, *new_vertexes])
    # plot_3d_points(new_vertexes)
    # plot_3d_points(vertex)

    # plot_3d_points(list([[-33.8284, 586.5621, 52.8456]]))
    # plot_3d_points([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
