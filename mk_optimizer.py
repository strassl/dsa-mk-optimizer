import numpy as np
import argparse
import toml
import colorama
from colorama import Fore
from helden_parser import parse, Spell, SpellTrait
from cost import columns, read_costs, get_cost, shift_column

colorama.init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description='Optimize choice of MK in DSA 4.1')
    parser.add_argument('-f', '--file', type=str, dest='file', help='name of file containing the skills to consider')
    parser.add_argument('--held', type=str, dest='held', help='helden software file')

    args = parser.parse_args()

    with open(args.file) as f:
        config = toml.loads(f.read())

    if args.held is not None:
        with open(args.held) as f:
            held = parse(f.read())[0]
            config = held_to_config(config, held)

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


def held_to_config(config, held):
    config_spells = { s['name']: s for s in config['skills'] }
    for skill in held.skills:
        if isinstance(skill, Spell):
            cspell = config_spells.get(skill.name)
            if cspell is not None:
                cspell['attrs'] = skill.attributes
                cspell['from'] = skill.value
                cspell['mks'] = list(map(lambda x: str(x), skill.traits))

    config['skills'] = list(config_spells.values())
    return config


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
