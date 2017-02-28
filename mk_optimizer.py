import numpy as np
import argparse
import toml
import colorama
from colorama import Fore
from cost import columns, read_costs, get_cost, shift_column

colorama.init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description='Optimize choice of MK in DSA 4.1')
    parser.add_argument('file', type=str, help='name of file containing the skills to consider')

    args = parser.parse_args()

    config = None
    with open(args.file) as f:
        config = toml.loads(f.read())

    base_cost, mk_totals = process_config(config)

    print('{:>10}: {:>6} AP'.format('Base', base_cost))
    for mk_name, mk_total_info in sorted(mk_totals.items(), key=lambda x: x[0]):
        mk_total = mk_total_info[0]
        mk_skill_total = mk_total_info[1]
        mk_cost = mk_total_info[2]
        saved = mk_total - base_cost

        if mk_total < base_cost:
            rec_str = Fore.GREEN + 'YES'
        else:
            rec_str = Fore.RED + 'NO'

        print('{:>10}: {:>6} ({:>6} + {:>3}) AP {:>6} => {}'.format(mk_name, mk_total, mk_skill_total, mk_cost, saved, rec_str))

def process_config(config):
    costs = read_costs()
    skills = config['skills']
    factor = config['factor']

    base_cost = calculate_cost_for_skills(costs, skills, factor, 0, None)

    mks = config['mks']
    mk_totals = {}
    for mk in mks:
        mk_cost = mk['cost']
        name = mk['name']
        cost_with_mk = calculate_cost_for_skills(costs, skills, factor, -1, name)
        total = mk_cost + cost_with_mk
        mk_totals[name] = (total, cost_with_mk, mk_cost)

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


if __name__ == '__main__':
    main()
