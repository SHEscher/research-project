#!/usr/bin/env python
"""This hook is run before cookiecutter starts creating the project."""

# %% Import
import re
import sys


# %% Set global vars & paths >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug }}'


# %% Functions >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
pass


# %% __main__  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

if __name__ == '__main__':

    if not re.match(MODULE_REGEX, module_name):

        print("\033[31mERROR: The project slug (%s) is not a valid Python module name. "
              "Please do not use a - and use _ instead\033[0m" % module_name)

        # Exit to cancel project
        sys.exit(1)

    print("\033[34m\n\nI am creating the research project: %s\n\033[0m" % module_name)

# o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
