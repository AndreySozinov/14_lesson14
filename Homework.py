# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

# Занятие 13 Задача 1
import doctest
import unittest
import pytest


def give_me_number(a: str) -> int | float:
    try:
        number = int(a)
        return number
    except ValueError:
        try:
            number = float(a)
            return number
        except TypeError as e:
            print(f'Wrong value - {e}')


class TestCaseNumber(unittest.TestCase):

    def test_int(self):
        self.assertEqual(give_me_number('5'), 5)

    def test_float(self):
        self.assertEqual(give_me_number('5.5'), 5.5)

    def test_string(self):
        self.assertRaises(ValueError, give_me_number, 'five')


def test_int():
    assert give_me_number('5') == 5


def test_float():
    assert give_me_number('5.5') == 5.5


def test_string():
    with pytest.raises(ValueError, match=r"could not convert string to float: 'five'"):
        give_me_number('five')


if __name__ == '__main__':
    # doctest.testfile('doctest_homework.txt', verbose=True)
    # unittest.main(verbosity=2)
    pytest.main(['-v'])
