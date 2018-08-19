import pytest
from app import soma, is_number


# def test_soma():
#     assert soma(0,0) == 1
#     assert soma(-2,-5) == -6
    # self.assertEqual(soma(-2,-5), -7)
    # self.assertEqual(soma(-2,5), 3)
    # self.assertEqual(soma(7,5), 12)
    # self.assertEqual(soma(7.5,5.4), 12.9)
    # self.assertEqual(soma(2e3,1), 2001)

@pytest.mark.parametrize('a,b,expected', [(0, 0, 0), (-2,-5,-7), (-2, 5,3), (7.5, 5.4,12.9), (-1.0, -2.0,-3.0)])
def test_soma2(a,b, expected):
    assert soma(a,b) == expected
    # def test_isnumber(self):
    #     self.assertTrue(is_number(1))
    #     self.assertTrue(is_number(-1005))
    #     self.assertTrue(is_number(1.5))
    #     self.assertTrue(is_number(-1.5))
    #     self.assertTrue(is_number('1'))
    #     self.assertTrue(is_number('1.5'))
    #     self.assertTrue(is_number('-1.5'))
    #     self.assertTrue(is_number('2e3'))
    #     self.assertFalse(is_number('Fred'))
    #     self.assertFalse(is_number('1..2'))
    #     self.assertFalse(is_number('1*2'))


@pytest.mark.parametrize('a,expected', [(0, 0), (-2,-4), (5,10), (7.5, 15), (-1.3, -2.6), ('Fred', None)])
def test_dobro(a,expected):
    assert soma(a) == expected

@pytest.mark.parametrize('num,expected', [(0, True), (-1,True), (1.5,True), (-7.5, True), ('-7.5', True), ('1', True), ('2e3', True), ('Fred', False), ('7*5', False), ('1..2', False)])
def test_is_number(num,expected):
    assert is_number(num) == expected
