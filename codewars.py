import numpy as np
from pprint import pprint


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
    shape = '\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|      |     |\n+------+-----+'
    shape = '\n+-------------------+--+\n|                   |  |\n|                   |  |\n|  +----------------+  |\n|  |                   |\n|  |                   |\n+--+-------------------+'
    shape = '\n           +-+             \n           | |             \n         +-+-+-+           \n         |     |           \n      +--+-----+--+        \n      |           |        \n   +--+-----------+--+     \n   |                 |     \n   +-----------------+     '

    # shape = "\n+--+---+\n"
    pprint(break_pieces(shape))
    # print(shape)
    
    
# from solution import break_pieces
# try: from solution import raw_errors
# except ImportError: raw_errors = False
# import codewars_test as test

# test_data = [
#     ('Description example',
#      [('\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|      |     |\n+------+-----+', ['+-----+\n|     |\n|     |\n+-----+', '+------+\n|      |\n|      |\n+------+', '+------------+\n|            |\n|            |\n|            |\n+------------+'])]),
#     ('Simple shapes',
#      [('\n+-------------------+--+\n|                   |  |\n|                   |  |\n|  +----------------+  |\n|  |                   |\n|  |                   |\n+--+-------------------+', ['                 +--+\n                 |  |\n                 |  |\n+----------------+  |\n|                   |\n|                   |\n+-------------------+', '+-------------------+\n|                   |\n|                   |\n|  +----------------+\n|  |\n|  |\n+--+']),
#       ('\n           +-+             \n           | |             \n         +-+-+-+           \n         |     |           \n      +--+-----+--+        \n      |           |        \n   +--+-----------+--+     \n   |                 |     \n   +-----------------+     ', ['+-+\n| |\n+-+', '+-----+\n|     |\n+-----+', '+-----------+\n|           |\n+-----------+', '+-----------------+\n|                 |\n+-----------------+']),
#       ('\n+---+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+---+', ['+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+']),
#       ('\n+---+------------+---+\n|   |            |   |\n+---+------------+---+\n|   |            |   |\n|   |            |   |\n|   |            |   |\n|   |            |   |\n+---+------------+---+\n|   |            |   |\n+---+------------+---+', ['+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n|   |\n|   |\n|   |\n+---+', '+---+\n|   |\n|   |\n|   |\n|   |\n+---+', '+------------+\n|            |\n+------------+', '+------------+\n|            |\n+------------+', '+------------+\n|            |\n|            |\n|            |\n|            |\n+------------+']),
#       ('\n                 \n   +-----+       \n   |     |       \n   |     |       \n   +-----+-----+ \n         |     | \n         |     | \n         +-----+ ', ['+-----+\n|     |\n|     |\n+-----+', '+-----+\n|     |\n|     |\n+-----+'])]),
#     ('Nested pieces',
#      [('\n+--------+\n|        |\n|  +--+  |\n|  |  |  |\n|  +--+  |\n|        |\n+--------+', ['+--+\n|  |\n+--+', '+--------+\n|        |\n|  +--+  |\n|  |  |  |\n|  +--+  |\n|        |\n+--------+'])]),
#     ('Convoluted borders',
#      [('\n+-------+ +----------+\n|       | |          |\n| +-+ +-+ +-+    +-+ |\n+-+ | |     |  +-+ +-+\n    | +-----+--+\n+-+ |          +-+ +-+\n| +-+  +----+    | | |\n| |    |    |    +-+ |\n| +----++ +-+        |\n|       | |          |\n+-------+ +----------+', ['+-+\n| |\n| |\n| +-----+\n|       |\n+-------+', '+-------+\n|       |\n| +-+ +-+\n+-+ | |\n    | +--------+\n    |          +-+ +-+\n  +-+  +----+    | | |\n  |    |    |    +-+ |\n  +----+  +-+        |\n          |          |\n          +----------+', '+----------+\n|          |\n+-+    +-+ |\n  |  +-+ +-+\n  +--+'])]),
#     ('edo_red97\'s big shape',
#      [('\n         +------------+--+      +--+\n         |            |  |      |  |\n         | +-------+  |  |      |  |\n         | |       |  |  +------+  |\n         | |       |  |            |\n         | |       |  |    +-------+\n         | +-------+  |    |        \n +-------+            |    |        \n |       |            |    +-------+\n |       |            |            |\n +-------+            |            |\n         |            |            |\n    +----+---+--+-----+------------+\n    |    |   |  |     |            |\n    |    |   |  +-----+------------+\n    |    |   |                     |\n    +----+---+---------------------+\n    |    |                         |\n    |    | +----+                  |\n+---+    | |    |     +------------+\n|        | |    |     |             \n+--------+-+    +-----+             ', ['    +----+\n    |    |\n    |    |\n+---+    |\n|        |\n+--------+', '+--+\n|  |\n|  +------------------+\n|                     |\n+---------------------+', '+--+      +--+\n|  |      |  |\n|  |      |  |\n|  +------+  |\n|            |\n|    +-------+\n|    |\n|    |\n|    +-------+\n|            |\n|            |\n|            |\n+------------+', '+---+\n|   |\n|   |\n|   |\n+---+', '+----+\n|    |\n|    |\n|    |\n+----+', '+-----+\n|     |\n+-----+', '+-------+\n|       |\n|       |\n+-------+', '+-------+\n|       |\n|       |\n|       |\n+-------+', '+------------+\n|            |\n+------------+', '+------------+\n|            |\n| +-------+  |\n| |       |  |\n| |       |  |\n| |       |  |\n| +-------+  |\n|            |\n|            |\n|            |\n|            |\n|            |\n+------------+', '+-------------------------+\n|                         |\n| +----+                  |\n| |    |     +------------+\n| |    |     |\n+-+    +-----+'])])]

# @test.describe('Sample tests')
# def sample_tests():
#     for name, test_cases in test_data:
#         @test.it(name)
#         def tests():
#             for shape, expected in test_cases:
#                 actual = break_pieces(shape)
#                 if raw_errors:
#                     test.assert_equals(sorted(break_pieces(shape)), expected)
#                 else:
#                     if not isinstance(actual, list):
#                         test.fail(f'break_pieces should return a list; actual result: {actual}')
#                         continue
#                     actual = sorted(actual)
#                     if actual == expected:
#                         test.pass_()
#                         continue
#                     message = ['break_pieces failed on this shape:', shape, '', 'Actual result:']
#                     message.extend(actual)
#                     message.append('\nExpected result:')
#                     message.extend(expected)
#                     test.fail('\n'.join(message))