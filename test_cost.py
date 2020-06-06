from cost import *
import pytest

def test_simple_cost():
    category = 'pre'
    price = 2
    units = 2
    assert calc_base_cost(category, price, units) == 1

def test_simple_cost_and_type():
    category = 'per-unit'
    price = 2
    units = 2
    assert calc_base_cost(category, price, units) == 4

def test_simple_cost_and_types():
    category = 'per-unit'
    price = 2
    units = 1.7
    assert calc_base_cost(category, price, units) == 4

def test_simple_cost_and_markdown():
    category = 'markdown'
    price = 1
    units = 2
    assert calc_base_cost(category, price, units) == 1.4