import pytest
from app import soma, is_number


@pytest.mark.parametrize('a,b,expected', [(0, 0, 0), (-2,-5,-7), (-2, 5,3), (7.5, 5.4,12.9), (-1.0, -2.0,-3.0)])
def test_soma(a,b, expected):
    assert soma(a,b) == expected

# @pytest.mark.parametrize('a,expected', [(0, 0), (-2,-4), (5,10), (7.5, 15), (-1.3, -2.6), ('Fred', None)])
# def test_dobro(a,expected):
#     assert soma(a) == expected

@pytest.mark.parametrize('num,expected', [(0, True), (-1,True), (1.5,True), (-7.5, True), ('-7.5', True), ('1', True), ('2e3', True), ('Fred', False), ('7*5', False), ('1..2', False)])
def test_is_number(num,expected):
    assert is_number(num) == expected
