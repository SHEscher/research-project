#!/usr/bin/env python
"""
This hook is run after cookiecutter finishes creating the project.
We can't dertermine whether this runs before or after post_gen_project.sh script. This depends on the OS.
"""

# %% Import
import os
from pathlib import Path
import subprocess

# %% Set global vars & paths >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
PROJECT_DIRECTORY = Path.cwd().resolve()  # os.path.realpath(os.path.curdir)
PROJECT_GITIGNORE = PROJECT_DIRECTORY / ".gitignore"
LINES_TO_ADD_TO_GITIGNORE = """# Bigger research folders
data/
literature/pdfs/
organisation/
publications/
results/

# Private configs in ./code/configs/
*_config.toml

"""


# %% Functions >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
pass


# %% __main__  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

if __name__ == "__main__":

    # Remove license file if not open source
    if "Not open source" in "{{ cookiecutter.open_source_license }}":
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

    {% if cookiecutter.init_git -%}
    # Run git add . & make first commit
    if not (PROJECT_DIRECTORY / ".git/").exists():
        print("\033[34m\nActivating git in {{ cookiecutter.project_slug }} ...\n\033[0m")
        subprocess.run(["git", "init", "--initial-branch=main"], check=False)
    print("\033[34m\nRunning git add . & do first project commit ...\n\033[0m")
    subprocess.run(["git", "add", "."], check=False)
    subprocess.run(["git", "commit", "-m", "Initial commit of {{ cookiecutter.project_slug }}"], check=False)
    {% else %}
    # Remove .gitingore file
    # PROJECT_GITIGNORE.unlink()
    pass
    {% endif %}

    print("\033[32m\n\nI am done creating the new research project in: %s\n\033[0m" % PROJECT_DIRECTORY)

    {% if cookiecutter.create_conda_env %}
    CONDA_ENV_NAME="{{ cookiecutter.project_slug[:4]}}_{{cookiecutter.python_version[:4] }}"
    print("\nTo activate the conda environment, run:\n\nconda activate %s\n" % CONDA_ENV_NAME)
    {%- endif %}

# o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
