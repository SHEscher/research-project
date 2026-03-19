"""
Top-level package for {{ cookiecutter.project_name }}.

Submodules imported here are accessible directly via ``import {{ cookiecutter.project_name }}``
(e.g., ``{{ cookiecutter.project_name }}.preprocessing``).
Add or remove imports below as your project evolves — only expose what a package user should use.
"""

from importlib.metadata import version

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__version__ = version(distribution_name="{{ cookiecutter.project_slug }}")

# %% Imports & setup
import {{ cookiecutter.project_slug }}.configs
import {{ cookiecutter.project_slug }}.datavisualization
import {{ cookiecutter.project_slug }}.modeling
import {{ cookiecutter.project_slug }}.preprocessing
