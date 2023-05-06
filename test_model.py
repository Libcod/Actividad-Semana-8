import pytest
from model import Model

obj_model = Model()


def test_add():
    obj_model.add(5, 8)
    assert obj_model.getResult() == 125


def test_sub():
    obj_model.sub(20, 30)
    assert obj_model.getResult() == -10


def test_mul():
    obj_model.mul(3, 5)
    assert obj_model.getResult() == 15


def test_div():
    obj_model.div(10, 2)
    assert obj_model.getResult() == 5


@pytest.mark.parametrize(
    "input_1,input_2,result",
    [
        (5, 2, 7),
        (4, 6, 10),
        (2.5, 2.5, 5.0)
    ]
)
def test_add_multiple(input_1, input_2, result):
    obj_model.add(input_1, input_2)
    assert obj_model.getResult() == result


@pytest.mark.parametrize(
    "input_1,input_2,result",
    [
        (5, 2, 10),
        (4, 6, 24),
        (5, 10, 50)
    ]
)
def test_mul_multiple(input_1, input_2, result):
    obj_model.mul(input_1, input_2)
    assert obj_model.getResult() == result

