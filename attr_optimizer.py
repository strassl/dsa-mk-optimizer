import numpy as np
import argparse
import toml
import colorama
from colorama import Fore
from cost import read_costs, get_cost, shift_column
from probability import expected_tap

colorama.init(autoreset=True)

COSTS = read_costs()

def main():
    parser = argparse.ArgumentParser(description='Optimize choice of attribute improvement in DSA 4.1')
    parser.add_argument('file', type=str, help='name of file containing the skills to consider')
    parser.add_argument('-w', '--weighted', dest='weighted', help='use weights for result', action='store_true')

    args = parser.parse_args()
    weighted = args.weighted

    config = None
    with open(args.file) as f:
        config = toml.loads(f.read())

    attr_results = process_config(config)

    tap_ratios = []
    tap_diffs = []
    for attr, result in attr_results.items():
        cost = result['cost']
        if weighted:
            tap_before = result['old']['tap_weighted']
            tap_after = result['new']['tap_weighted']
        else:
            tap_before = result['old']['tap']
            tap_after = result['new']['tap']
        tap_diff = tap_after - tap_before
        cost_to_tap_ratio = tap_diff / cost
        tap_ratios.append(cost_to_tap_ratio)
        tap_diffs.append(tap_diff)

    tap_ratios.sort(reverse=True)
    tap_diffs.sort(reverse=True)

    for attr, result in sorted(attr_results.items(), key=lambda x: x[0]):
        cost = result['cost']
        val_before = result['old']['value']
        val_after = result['new']['value']
        if weighted:
            count = result['old']['weighted']
            tap_before = result['old']['tap_weighted']
            tap_after = result['new']['tap_weighted']
        else:
            count = result['old']['count']
            tap_before = result['old']['tap']
            tap_after = result['new']['tap']
        tap_diff = tap_after - tap_before
        cost_to_tap_ratio = tap_diff / cost

        suffix = ''
        if cost_to_tap_ratio >= tap_ratios[0]:
            suffix += Fore.GREEN + '!!!'
        elif cost_to_tap_ratio >= tap_ratios[1]:
            suffix += Fore.GREEN + '!! '
        elif cost_to_tap_ratio >= tap_ratios[2]:
            suffix += Fore.GREEN + '!  '
        else:
            suffix += '   '
        suffix += Fore.RESET
        
        suffix += ' '
        if tap_diff >= tap_diffs[0]:
            suffix += Fore.BLUE + '!!!'
        elif tap_diff >= tap_diffs[1]:
            suffix += Fore.BLUE + '!! '
        elif tap_diff >= tap_diffs[2]:
            suffix += Fore.BLUE + '!  '
        else:
            suffix += '   '
        suffix += Fore.RESET


        print('{:>2} ({:>2} -> {:>2}): {:>3} => {:>7.2f} vs {:>7.2f} => {:>7.2f} for {:>4} ({:.4f}) {}'.format(attr, val_before, val_after, count, tap_before, tap_after, tap_diff, cost, cost_to_tap_ratio, suffix))

def process_config(config):
    costs = read_costs()
    skills = config['skills']
    attrlist = config['attrs']
    attrs = {}
    for attr in attrlist:
        attrs[attr['name']] = attr['value']

    attr_results = {}
    for attr_name, attr_val in attrs.items():
        result = calculate_result_for_attr(attr_name, attr_val, attrs, skills)
        attr_results[attr_name] = result

    return attr_results

def calculate_result_for_attr(attr_name, attr_value, attrs, skills):
    old_value = attr_value
    new_value = old_value + 1
    attr_improv_cost = get_cost(COSTS, 'H', old_value, new_value)

    old_result = calculate_result_for_attr_with_value(attr_name, old_value, attrs, skills)
    new_result = calculate_result_for_attr_with_value(attr_name, new_value, attrs, skills)

    return { 'cost': attr_improv_cost, 'old': old_result, 'new': new_result }

def calculate_result_for_attr_with_value(attr_name, attr_value, attrs, skills):
    total_count = 0
    total_weighted = 0
    total_tap = 0
    total_tap_weighted = 0
    for skill in skills:
        if attr_name in skill['attrs'] or '*' in skill['attrs']:
            total_count += 1
            total_weighted += skill['weight']

        taw = skill['taw']
        base_attr_names = skill['attrs'][:3]
        if '*' in base_attr_names:
            for aname in attrs.keys():
                attr_names = [aname if n == '*' else n for n in base_attr_names]
                tap = calculate_tap(attr_names, attr_name, attr_value, attrs, taw)
                total_tap += tap
                total_tap_weighted += tap * skill['weight']
        else:
            tap = calculate_tap(base_attr_names, attr_name, attr_value, attrs, taw)
            total_tap += tap
            total_tap_weighted += tap * skill['weight']


    return { 'value': attr_value, 'count': total_count, 'weighted': total_weighted, 'tap': total_tap, 'tap_weighted': total_tap_weighted }

def calculate_tap(attr_names, override_name, override_value, attrs, taw):
    def aval(name):
        return get_attr_value(override_name, override_value, name, attrs)

    attr_values = (aval(attr_names[0]), aval(attr_names[1]), aval(attr_names[2]))
    tap = expected_tap(attr_values, taw, 0)
    return tap

def get_attr_value(override_name, override_value, attr_name, attrs):
    if attr_name == override_name:
        return override_value
    else:
        return attrs[attr_name]

if __name__ == '__main__':
    main()
