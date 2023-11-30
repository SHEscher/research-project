"""Tests for `{{ cookiecutter.project_slug }}` package."""

# %% Import
{% if cookiecutter.use_pytest -%}
import pytest
{% else %}
import unittest
{%- endif -%}
from {{ cookiecutter.project_slug }}.preprocessing.freesurfer import foo


# %% Set global vars & paths >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
{%- if cookiecutter.use_pytest %}
@pytest.fixture()
def response():
    """
    Sample pytest fixture.

    See more at: https://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get("https://github.com/shescher/research-project")
{% else %}
pass
{% endif %}

# %% Test Functions o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
{%- if cookiecutter.use_pytest %}


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_foo():
    """Test the foo function."""
    assert foo() is None


{% else -%}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""


{% endif -%}
# o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END