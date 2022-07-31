import numpy as np
from pprint import pprint
from time import time


def get_v_and_e(shape):
    list_of_vertexes = []
    index = 0
    for line_idx, line in enumerate(shape):
        plus_index = line.find("+")
        while plus_index != -1:
            list_of_vertexes.append([index, line_idx, plus_index])
            plus_index = line.find("+", plus_index + 1)
            index += 1
    return np.array(list_of_vertexes)


def create_adjustice_matrix(list_of_vertexes):
    adjustice_matrix = np.zeros((len(list_of_vertexes) + 1, len(list_of_vertexes) + 1), dtype=list)
    adjustice_matrix[0, 1:] = range(len(list_of_vertexes))
    adjustice_matrix[1:, 0] = range(len(list_of_vertexes))
    return adjustice_matrix


def check_vertexes(main_vertex, sub_vertex, shape):
    delta_x, delta_y = sub_vertex[1:] - main_vertex[1:]
    # Horizon
    if delta_x == 0:
        x_str = (delta_y - 1) * "-"
        shape_str = shape[sub_vertex[1]][main_vertex[2] + 1:sub_vertex[2]]
        if x_str == shape_str:
            return True
    # Vertical
    if delta_y == 0:
        y_str = (delta_x - 1) * "|"
        shape_str = "".join([i[sub_vertex[2]] for i in shape[main_vertex[1] + 1:sub_vertex[1]]])
        if y_str == shape_str:
            return True
    return False


def fill_adjustice_matrix(adjustice_matrix, list_of_vertexes, shape):
    insertion = 1
    for main_vertex in list_of_vertexes:
        for vertex_ind in range(insertion, len(list_of_vertexes)):
            sub_vertex = list_of_vertexes[vertex_ind]
            if check_vertexes(main_vertex, sub_vertex, shape):
                # print(main_vertex, sub_vertex)
                adjustice_matrix[main_vertex[0] + 1][sub_vertex[0] + 1] = 1
                adjustice_matrix[sub_vertex[0] + 1][main_vertex[0] + 1] = 1
        insertion += 1
    return adjustice_matrix


def break_pieces(shape: str):
    shape = np.array(shape.split("\n")[1:])
    for line in shape:
        print(line)
    list_of_vertexes = get_v_and_e(shape)
    adjustice_matrix = create_adjustice_matrix(list_of_vertexes)
    adjustice_matrix = fill_adjustice_matrix(adjustice_matrix, list_of_vertexes, shape)
    return adjustice_matrix

            


# uncomment next line if you prefer raw error messages
# raw_errors = True
if __name__ == "__main__":
    # shape = '\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|      |     |\n+------+-----+'
    # shape = '\n+-------------------+--+\n|                   |  |\n|                   |  |\n|  +----------------+  |\n|  |                   |\n|  |                   |\n+--+-------------------+'
    # shape = '\n           +-+             \n           | |             \n         +-+-+-+           \n         |     |           \n      +--+-----+--+        \n      |           |        \n   +--+-----------+--+     \n   |                 |     \n   +-----------------+     '

    # shape = "\n+--+---+\n"
    # start = time()
    # pprint(break_pieces(shape))
    # print(time() - start)
    # print(shape)
    # n = 15
    # print(n + (5 - (n % 5)))
