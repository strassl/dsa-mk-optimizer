import numpy as np
import argparse
import toml
import colorama
from colorama import Fore
from cost_calculator import read_costs, get_cost, shift_column

colorama.init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description='Optimize choice of attribute improvement in DSA 4.1')
    parser.add_argument('file', type=str, help='name of file containing the skills to consider')

    args = parser.parse_args()

    config = None
    with open(args.file) as f:
        config = toml.loads(f.read())

    attr_results = process_config(config)
    print(attr_results)

def process_config(config):
    costs = read_costs()
    skills = config['skills']
    attrs = config['attrs']

    attr_results = {}
    for attr in attrs:
        attr_name = attr['name']
        attr_val = attr['value']
        result = calculate_result_for_attr(attr_name, skills)
        attr_results[attr_name] = result

    return attr_results

def calculate_result_for_attr(attr, skills):
    count = 0
    for skill in skills:
        if attr in skill['attrs'] or '*' in skill['attrs']:
            count += 1
    return count


if __name__ == '__main__':
    main()
