from helden_data import *

def test_get_traits():
    assert get_traits('Tlalucs Odem Pestgestank') == [SpellTrait.BESCHW, SpellTrait.DAEMON, SpellTrait.SCHADEN]
    assert get_traits('Igniplano Flächenbrand') == [SpellTrait.ELE_FEUER, SpellTrait.SCHADEN, SpellTrait.UMWELT]
    assert get_traits('Hexagramma Dschinnenbann') == [SpellTrait.ANTI, SpellTrait.BESCHW, SpellTrait.ELE]
    assert get_traits('Pentagramma Sphärenbann') == [SpellTrait.ANTI, SpellTrait.BESCHW, SpellTrait.DAEMON, SpellTrait.GEIST]


def test_get_complexity_for_skill_with_groups():
    assert get_complexity_for_skill('Magiekunde') == 'B'
    assert get_complexity_for_skill('Athletik') == 'D'
    assert get_complexity_for_skill('Menschenkenntnis') == 'B'
    assert get_complexity_for_skill('Feinmechanik') == 'B'