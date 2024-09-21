from modules import *


if __name__ == '__main__':
    vertex = get_info_from_file(r'Tire.obj')  # получение точек
    new_vertex = decard_to_cylinder(vertex, 0.001)  # перевод точек в цилиндрическиую систему координат
    new_vertex = cylinder_to_decard(new_vertex)  # перевод точек из цилиндрической в декартову систему координат
    new_vertex = for_Z(vertex, 0.01)  # ремаштабирование оси Z

    model1 = get_info_from_file(r'rim.obj')  # получение точек
    # new_vertex=decard_to_cylinder([[-2,-2,1]],1)
    # print(new_vertex[0])
    # new_vertex=cylinder_to_decard(new_vertex)
    # print(new_vertex[0])
    # new_vertex=for_Z(vertex,0.0001) #ремаштабирование точки

    plotting_3D(new_vertex)
    # plotting_3D(model1)
    # plotting_3D(vertex)
    # plotting_3D(list([[-33.8284, 586.5621, 52.8456]]))
