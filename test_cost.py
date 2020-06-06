from cost import *
import pytest

def test_simple_cost():
    price = 2
    units = 2
    assert calc_base_cost(price, units) == 4
