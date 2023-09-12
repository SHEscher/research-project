"""
Main module for {{ cookiecutter.project_slug }}

Author: {{ cookiecutter.full_name }}
Contact: {{ cookiecutter.email }}
Years: {% now 'local', '%Y' %}
"""

# %% Import
from {{ cookiecutter.project_slug }}.configs import config, params, path_to
from {{ cookiecutter.project_slug }}.preprocessing.freesurfer import foo


# %% Set global vars & paths >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
pass


# %% Functions >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o


def main():
    print(f"Access service x using my private key: {config.service_x.api_key}")
    foo()
    print(f"{path_to.results.GLM}/{params.weight_decay}/")


# %% __main__  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

if __name__ == "__main__":
    # Run main
    main()

# o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
