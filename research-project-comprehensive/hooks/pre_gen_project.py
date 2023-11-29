#!/usr/bin/env python
"""This hook is run before cookiecutter starts creating the project."""

# %% Import
import re
import subprocess
import sys


# %% Set global vars & paths >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

MODULE_NAME = '{{ cookiecutter.project_slug }}'


# %% Functions >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

def is_conda_installed() -> bool:
    """Check if conda is installed on the machine."""
    try:
        subprocess.check_output(['conda', '--version'])
        return True
    except Exception:
        return False


# %% __main__  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

if __name__ == '__main__':

    {%- if cookiecutter.create_conda_env -%}
    # In case of True add your content here
    if not is_conda_installed():
        print("\033[31m\nERROR: Conda is not installed on your machine. Please install and run again!\033[0m\n")
        sys.exit(1)
    {% endif %}

    if not re.match(MODULE_REGEX, MODULE_NAME):

        print("\033[31mERROR: The project slug (%s) is not a valid Python module name. "
              "Please do not use a - and use _ instead\033[0m" % MODULE_NAME)

        # Exit to cancel project
        sys.exit(1)

    print("\033[34m\n\nI am creating the research project: %s\n\033[0m" % MODULE_NAME)

# o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
