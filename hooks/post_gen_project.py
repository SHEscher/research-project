#!/usr/bin/env python
"""
This hook is run after cookiecutter finishes creating the project.
It should run after the post_gen_project.sh script.
"""

# %% Import
import os

# %% Set global vars & paths  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


# %% Functions  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

# %% __main__ o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    print("\033[32m\n\nI am done creating the new research project in: %s\n\033[0m" % PROJECT_DIRECTORY)

    if '{{ cookiecutter.create_conda_env }}' == 'y':
        CONDA_ENV_NAME="{{ cookiecutter.project_slug[:4]}}_{{cookiecutter.python_version[:4] }}"
        print("\nTo activate the conda environment, run:\n\nconda activate %s\n" % CONDA_ENV_NAME)

#  o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
