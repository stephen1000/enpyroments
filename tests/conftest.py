"""Configuration for pytest
"""

import pytest

from enpyronments.settings import Sensitive, Settings


def func():
    """ Just some function """


test_values = [
    int(),
    float(),
    str(),
    bytes(),
    list(),
    dict(),
    set(),
    func,
    object(),
    None,
]
test_values.extend([Sensitive(x) for x in test_values])


@pytest.fixture(params=test_values, scope="module")
def test_value(request):
    return request.param


@pytest.fixture(scope="module")
def is_sensitive(test_value):
    return isinstance(test_value, Sensitive)


@pytest.fixture(scope="module")
def actual_value(test_value, is_sensitive):
    if is_sensitive:
        return test_value.obj
    return test_value


@pytest.fixture(scope="module")
def test_key():
    """ Key used while testing Settings """
    return "foo"


@pytest.fixture(scope="module")
def bad_key():
    """ Key used while testing Settings """
    return "garbleblag"


@pytest.fixture(scope="module")
def test_dict(request, test_key, test_value):
    return {test_key: test_value}


@pytest.fixture(params=[0, 1, 2], scope="module")
def test_setting(request, test_dict):
    if request == 0:
        return Settings(iterable=test_dict)
    elif request == 1:
        return Settings(iterable=test_dict.items())
    else:
        return Settings(**test_dict)
