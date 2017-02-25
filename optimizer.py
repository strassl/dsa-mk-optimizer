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

    base_cost, mk_totals = process_config(config)

    print('{:>10}: {} AP'.format('Base', base_cost))
    for mk_name, mk_total in mk_totals.items():
        saved = mk_total - base_cost

        if mk_total < base_cost:
            rec_str = Fore.GREEN + 'YES'
        else:
            rec_str = Fore.RED + 'NO'

        print('{:>10}: {} AP ({}) => {}'.format(mk_name, mk_total, saved, rec_str))

def process_config(config):
    costs = read_costs()
    skills = config['skills']
    factor = config['factor']

    base_cost = calculate_cost_for_skills(costs, skills, factor, 0, None)

    mk_totals = {}
    for mk in config['mks']:
        mk_cost = mk['cost']
        name = mk['name']
        cost_with_mk = calculate_cost_for_skills(costs, skills, factor, -1, name)
        total = mk_cost + cost_with_mk
        mk_totals[name] = total

    return base_cost, mk_totals


def calculate_cost_for_skills(costs, skills, factor, offset, mk):
    total = 0

    for skill in skills:
        from_val = skill['from']
        to_val = skill['to']
        actual_col = skill['column']
        if mk in skill['mks']:
            actual_col = shift_column(actual_col, offset)
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