from bs4 import BeautifulSoup
from cost import shift_column
from helden_data import SpellTrait, get_traits

core_attr_long_to_short = {
    'Mut': 'MU',
    'Klugheit': 'KL',
    'Intuition': 'IN',
    'Charisma': 'CH',
    'Fingerfertigkeit': 'FF',
    'Gewandtheit': 'GE',
    'Konstitution': 'KO',
    'Körperkraft': 'KK',
}

attr_long_to_short = { **core_attr_long_to_short, **{
    'Sozialstatus': 'SO',
    'Lebensenergie': 'LE',
    'Ausdauer': 'AU',
    'Astralenergie': 'AE',
    'Karmaenergie': 'KE',
    'Magieresistenz': 'MR',
    'ini': 'INI',
    'at': 'AT',
    'pa': 'PA',
    'fk': 'FK',
}}

core_attrs = core_attr_long_to_short.values()

def reprify(cls_name, it):
    attrs = vars(it)
    return cls_name + '(' + ', '.join("%s=%s" % (item[0], repr(item[1])) for item in attrs.items()) + ')'

class Character:
    def __init__(self, name, attributes, skills):
        self.name = name
        self.attributes = attributes
        self.skills = skills

    def __repr__(self):
        return reprify('Character', self)

class Skill:
    def __init__(self, name, column, value, attributes):
        self.name = name
        self.column = column
        self.value = value
        self.attributes = attributes

    def __repr__(self):
        return reprify('Skill', self)

class Spell(Skill):
    def __init__(self, name, column, value, attributes, traits):
        super().__init__(name, column, value, attributes)
        self.traits = traits

    def __repr__(self):
        return reprify('Spell', self)

def load_and_parse(filename):
    with open(filename, 'r') as f:
        return parse(f.read())

def parse(data):
    s = BeautifulSoup(data, features='xml')
    chars = []
    for held in s.find_all('held'):
        attributes = {}
        for attr in held.find_all('eigenschaft'):
            attr_name = core_attr_long_to_short.get(attr.attrs['name'])
            if attr_name is not None:
                value = int(attr.attrs['value'])
                attributes[attr_name] = value

        skills = [] 
        for talent in held.find_all('talent'):
            skill = parse_skill(talent)
            skills.append(skill)

        for zauber in held.find_all('zauber'):
            skill = parse_skill(zauber, is_spell=True)
            skills.append(skill)

        name = held.attrs['name']
        char = Character(name, attributes, skills)
        chars.append(char)
    return chars

def parse_skill(element, is_spell=False):
    talent_name = element.attrs['name']
    talent_check_str = element.attrs['probe']
    talent_value = int(element.attrs['value'])
    talent_check_attrs = talent_check_str.strip().split('/')
    if is_spell:
        talent_column = element.attrs['k']
        is_house_spell = bool(element.attrs['hauszauber'])
        traits = get_traits(talent_name)
        skill = Spell(talent_name, talent_column, talent_value, talent_check_attrs, traits)
    else:
        talent_column = '?' # TODO
        skill = Skill(talent_name, talent_column, talent_value, talent_check_attrs)
    return skill