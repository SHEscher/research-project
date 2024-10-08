"""Check if cookiecutter >= 2.5.0 is installed."""

# %% Import
import sys

from cookiecutter import __version__ as cookiecutter_version

# %% __main__  >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o
if __name__ == "__main__":
    if tuple(map(int, cookiecutter_version.split("."))) < tuple(map(int, "2.5.0".split("."))):
        print(f"\ncookiecutter == {cookiecutter_version} is installed.")
        print("\033[31mERROR: You need to update cookiecutter to >= 2.5.0. Then rerun the command.\n\033[0m")
        sys.exit(1)

# o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o END
