#!/usr/bin/env python
"""
This hook is run after cookiecutter finishes creating the project.
It should run after the post_gen_project.sh script.
"""

# %% Import
import os
from pathlib import Path
import subprocess

# %% Set global vars & paths  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
PROJECT_DIRECTORY = Path.cwd().resolve()  # os.path.realpath(os.path.curdir)
PROJECT_GITIGNORE = PROJECT_DIRECTORY / ".gitignore"
LINES_TO_ADD_TO_GITIGNORE = """# Bigger research folders
data/
literature/pdfs/
organisation/
publications/
results/

# Private configs in ./code/confings/
*_config.toml

"""


# %% Functions  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

pass


# %% __main__ o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

if __name__ == '__main__':

    # Remove license file if not open source
    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        (PROJECT_DIRECTORY / "LICENSE").unlink()

    # Remove all empty *_FILES
    print("\nRemoving empty placeholder files *_FILES from folders ...")
    for file_to_delete in Path(PROJECT_DIRECTORY).glob("**/*_FILES"):
        file_to_delete.unlink()

    # Add lines to .gitignore
    print("\nAdding project specific lines to .gitignore ...")
    with open(PROJECT_GITIGNORE, 'r+') as f:
        file_content = f.read()
        f.seek(0, 0)
        f.write(LINES_TO_ADD_TO_GITIGNORE + file_content)

    {% if cookiecutter.init_git == 'y' -%}
    # Run git add . & make first commit
    print("\033[34m\nRunning git add . & do first project commit ...\n\033[0m")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit of {{ cookiecutter.project_slug }}"], check=True)
    {% endif %}

    print("\033[32m\n\nI am done creating the new research project in: %s\n\033[0m" % PROJECT_DIRECTORY)

    if '{{ cookiecutter.create_conda_env }}' == 'y':
        CONDA_ENV_NAME="{{ cookiecutter.project_slug[:4]}}_{{cookiecutter.python_version[:4] }}"
        print("\nTo activate the conda environment, run:\n\nconda activate %s\n" % CONDA_ENV_NAME)

#  o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
