#!/usr/bin/env python
import simple_math
from simple_math import *
import pytest

@pytest.mark.parametrize("a1,a2, expected", [ (1,1 ,2), (3.5, 2, 5.5), (3.1, 5.2, 8.3)
])

def test_simple_add_parametrized(a1,a2, expected):
    assert simple_add(a1,a2) == expected


@pytest.mark.parametrize("a1,a2, expected", [ (1,1 ,1), (3.5, 2, 7.0), (3.0, 5.0, 15.0)
])

def test_simple_mult_parametrized(a1,a2, expected):
    assert simple_mult(a1,a2) == expected
