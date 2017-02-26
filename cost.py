import numpy as np

columns = ['A*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def read_costs():
    table = np.genfromtxt('costs.csv', dtype=int, delimiter='\t', names=True)
    return table

def shift_column(column, offset):
    shifted_index = columns.index(column) + offset
    shifted_index = min(shifted_index, len(columns)-1)
    shifted_index = max(shifted_index, 0)
    return columns[shifted_index]

def get_cost(costs, column, from_value, to_value, factor=1.0):
    if column not in columns:
        raise AssertionError('Not a valid column: ' + column)

    if from_value is None:
        from_value = -1

    if from_value > to_value:
        raise AssertionError('From > To')

    col_to_index = {
        'A*': 1,
        'A': 2,
        'B': 3,
        'C': 4,
        'D': 5,
        'E': 6,
        'F': 7,
        'G': 8,
        'H': 9
    }

    total = 0
    for i in range(from_value, to_value):
        index = i+1
        index = min(index, len(costs)-1)
        index = max(index, 0)
        cost = costs[index][col_to_index[column]]
        cost = int(round(cost * factor))
        total += cost

    return total