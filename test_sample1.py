# _*_ coding=utf-8 _*_
import pytest


def func(x):
    return x + 1


@pytest.mark.case1
def test_file1_answer1():
    assert func(3) == 5


@pytest.mark.case1
def test_file1_answer2():
    assert func(5) == 5

