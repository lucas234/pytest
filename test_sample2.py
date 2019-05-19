# _*_ coding=utf-8 _*_
import pytest


def func(x):
    return x + 1


@pytest.mark.case1
def test_file2_answer1():
    assert func(4) == 5


@pytest.mark.case2
def test_file2_answer2():
    assert func(6) == 5
