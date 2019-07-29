from importlib import import_module

import pytest

sample_apps = [
    'environment_variables',
    'local_settings',
    'mode_dev',
    'mode_prod',
]

@pytest.fixture(params=sample_apps)
def sample_app(request):
    return request.param

def get_expected_settings(app):
    getter = import_module(
        f'sample_apps.{app}.expected'
    )
    return getter.settings

def get_actual_settings(app):
    getter = import_module(
        f'sample_apps.{app}.main'
    )
    return getter.get_settings()

def get_settings(app):    
    actual, expected = get_actual_settings(app), get_expected_settings(app)
    return actual, expected

def test_sample_app(sample_app):
    actual, expected = get_settings(sample_app)
    for key, val in expected.items():
        assert actual[key] == val
