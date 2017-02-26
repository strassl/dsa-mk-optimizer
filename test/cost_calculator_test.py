from cost_calculator import *
import numpy as np

costs = read_costs()

def test_get_cost_should_return_correct_value():
    cost = get_cost(costs, 'A', 0, 3)
    assert cost == (1+2+3)

def test_get_cost_should_return_0_for_no_increase():
    cost = get_cost(costs, 'D', 3, 3)
    assert cost == 0

def test_get_cost_should_correctly_calculate_activation():
    cost = get_cost(costs, 'A', None, 3)
    assert cost == (5+1+2+3)

def test_get_cost_should_correctly_calculate_astar():
    cost = get_cost(costs, 'A*', None, 3)
    assert cost == (5+1+1+1)

def test_get_cost_should_correctly_calculate_over_31():
    cost = get_cost(costs, 'H', 29, 32)
    assert cost == (950+1000+1000)

def test_get_cost_should_correctly_calculate_sum():
    cost = get_cost(costs, 'H', 15, 17)
    assert cost == (450+480)

def test_get_cost_should_correctly_calculate_negative_steps():
    cost = get_cost(costs, 'D', -2, 2)
    assert cost == (20+20+3+7)

def test_get_cost_with_factor_should_correctly_calculate_value():
    cost = get_cost(costs, 'H', 15, 17, 0.75)
    assert cost == (338+360)