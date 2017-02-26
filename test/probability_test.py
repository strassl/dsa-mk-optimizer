from probability import *

def test_roll_tap_should_handle_taw_zero():
    attrs = (10,12,14)
    rolls = (10,12,14)

    tap = roll_tap(rolls, attrs, 0, 0)
    assert tap == 1

def test_roll_tap_should_calculate_correct_double_twenty_tap():
    attrs = (19,19,14)
    rolls = (20,20,1)

    tap = roll_tap(rolls, attrs, 8, 4)
    assert tap == 0

def test_roll_tap_should_calculate_correct_double_one_tap():
    attrs = (10,12,14)
    rolls = (1,20,1)

    tap = roll_tap(rolls, attrs, 8, 4)
    assert tap == 8

def test_roll_tap_should_handle_relaxation():
    attrs = (10,12,14)
    rolls = (10,12,15)

    tap = roll_tap(rolls, attrs, 2, -4)
    assert tap == 2

def test_roll_tap_should_calculate_correct_barely_success():
    attrs = (10,12,14)
    rolls = (10,12,15)

    tap = roll_tap(rolls, attrs, 1, 0)
    assert tap == 1

def test_roll_tap_should_calculate_correct_regular_failure():
    attrs = (10,12,14)
    rolls = (11,18,12)

    tap = roll_tap(rolls, attrs, 8, 4)
    assert tap == 0

def test_roll_tap_should_calculate_correct_regular_tap():
    attrs = (10,12,14)
    rolls = (11,10,12)

    tap = roll_tap(rolls, attrs, 8, 4)
    assert tap == 3

def test_roll_tap_should_handle_handicap_greater_than_taw_failure():
    attrs = (10,12,14)
    rolls = (9,10,12)

    tap = roll_tap(rolls, attrs, 8, 10)
    assert tap == 0

def test_roll_tap_should_handle_handicap_greater_than_taw_success():
    attrs = (10,12,14)
    rolls = (8,10,12)

    tap = roll_tap(rolls, attrs, 8, 10)
    assert tap == 1

def test_probability_should_be_calculated_correctly_for_taw_two_success():
    attrs = (10,12,14)
    prob_one_tap = probability(1, attrs, 2, 0)
    prob_two_tap = probability(2, attrs, 2, 0)
    assert (prob_one_tap + prob_two_tap) == 0.32375

def test_probability_should_be_calculated_correctly_for_taw_two_failure():
    attrs = (10,12,14)
    prob = probability(0, attrs, 2, 0)
    assert 0.67625 == prob

def test_probability_should_be_calculated_correctly_for_taw_zero_success():
    prob = probability(1, (10,10,10), 0, 0)
    assert 0.12875 == prob

def test_probability_should_be_calculated_correctly_for_taw_zero_failure():
    prob = probability(0, (10,10,10), 0, 0)
    assert 0.87125 == prob

def test_probability_should_be_calculated_correctly_for_max_tap():
    prob = probability(16, (10,12,14), 16, -2)
    assert 0.32375 == prob

def test_probability_should_be_calculated_correctly_with_handicap():
    prob = probability(6, (10,12,14), 8, 2)
    assert 0.20575 == prob

def test_probability_should_be_calculated_correctly_with_relaxation():
    prob = probability(6, (10,12,14), 8, -2)
    assert 0.067 == prob

def test_probability_for_tap_greater_taw_should_be_zero():
    prob = probability(9, (14,14,14), 8, -2)
    assert 0.0 == prob

def test_probability_should_propagate_below_zero_taw():
    prob_one_tap = probability(1, (10,10,10), 0, 5)
    assert 0.02125 == prob_one_tap

def test_probability_should_allow_crit():
    prob_one_tap = probability(1, (10,10,10), 0, 20)
    assert 0.00725 == prob_one_tap
