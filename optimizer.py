import numpy as np
import argparse
import toml
import colorama
from colorama import Fore

colorama.init(autoreset=True)

columns = ['A*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def main():
    parser = argparse.ArgumentParser(description='Optimize choice of advantages in DSA 4.1')
    parser.add_argument('file', type=str, help='name of file containing the skills to consider')

    args = parser.parse_args()

    config = None
    with open(args.file) as f:
        config = toml.loads(f.read())

    base_cost, cost_with_mk, mk_cost = process_config(config)
    total_mk = cost_with_mk + mk_cost

    print('Base:\t{} AP'.format(base_cost))
    print('MK:\t{} AP ({} + {})'.format(total_mk, cost_with_mk, mk_cost))
    print('Saved:\t{} AP'.format(base_cost - total_mk))

    rec_str = 'Recommendation: '
    if total_mk < base_cost:
        rec_str += Fore.GREEN + 'BUY'
    else:
        rec_str += Fore.GREEN + 'DON\'T BUY'

    print(rec_str)

def process_config(config):
    costs = read_costs()
    skills = config['skills']
    mk_cost = config['cost']
    factor = config['factor']

    base_cost = calculate_cost_for_skills(costs, skills, factor, 0)
    cost_with_mk = calculate_cost_for_skills(costs, skills, factor, -1)

    return base_cost, cost_with_mk, mk_cost


def calculate_cost_for_skills(costs, skills, factor, offset):
    total = 0

    for skill in skills:
        from_val = skill['from']
        to_val = skill['to']
        col = skill['column']
        actual_col = shift_column(col, offset)
        cost = get_cost(costs, actual_col, from_val, to_val, factor)
        total += cost

    return total


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

if __name__ == '__main__':
    main()