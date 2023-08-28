"""
Configuration for {{ cookiecutter.project_name }} project

Note:
    * store private configs in the same folder as 'config.toml', namely: "./[PRIVATE_PREFIX]_configs.toml"
    * keep the prefix, such that it is ignored by git

Alternatively, Configs could als be set using .env file together with python-dotenv package.

Author: Simon M. Hofmann | <[firstname].[lastname][at]pm.me> | 2023
"""

# %% Imports
import os
import sys

if sys.version_info >= (3, 11):
    # since python 3.11, there is also tomllib
    import tomllib as toml
else:
    import toml

from pathlib import Path
from typing import Any, Optional, Dict


# %% Config class & functions >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

class CONFIG:
    """Configuration object."""

    def __init__(self, config_dict: Optional[dict] = None):
        """Initialise CONFIG class object."""
        if config_dict is not None:
            self.update(config_dict)

    def __repr__(self):
        """Implement __repr__ of CONFIG."""
        str_out = "CONFIG("
        list_attr = [k for k in self.__dict__.keys() if not k.startswith("_")]
        ctn = 0  # counter for visible attributes only
        for key, val in self.__dict__.items():
            if key.startswith("_"):
                # ignore hidden attributes
                continue
            ctn += 1
            str_out += f"{key}="
            if isinstance(val, CONFIG):
                str_out += val.__str__()
            else:
                str_out += f"'{val}'" if isinstance(val, str) else f"{val}"

            str_out += ", " if ctn < len(list_attr) else ""
        return str_out + ")"

    def update(self, new_configs: Dict[str, Any]):
        """Update config object with new entries."""
        for k, val in new_configs.items():
            if isinstance(val, (list, tuple)):
                setattr(self, k, [CONFIG(x) if isinstance(x, dict) else x for x in val])
            else:
                setattr(self, k, CONFIG(val) if isinstance(val, dict) else val)

    def show(self, indent: int = 0):
        """Display configurations in nested way."""
        for key, val in self.__dict__.items():
            if isinstance(val, CONFIG):
                print("\t" * indent + f"{key}:")
                val.show(indent=indent + 1)
            else:
                print("\t" * indent + f"{key}: " + (f"'{val}'" if isinstance(val, str) else f"{val}"))

    def asdict(self):
        """Converts config object to dict."""
        dict_out = {}
        for key, val in self.__dict__.items():
            if isinstance(val, CONFIG):
                dict_out.update({key: val.asdict()})
            else:
                dict_out.update({key: val})
        return dict_out

    def update_paths(self, parent_path: Optional[str] = None):
        """Update relative paths to PROJECT_ROOT dir."""

        # Use project root dir as parent path if not specified
        parent_path = self.PROJECT_ROOT if hasattr(self, "PROJECT_ROOT") else parent_path

        if parent_path is not None:
            parent_path = str(Path(parent_path).absolute())

            for key, path in self.__dict__.items():
                if isinstance(path, str) and not Path(path).is_absolute():
                    self.__dict__.update({key: str(Path(parent_path).joinpath(path))})

                elif isinstance(path, CONFIG):
                    path.update_paths(parent_path=parent_path)

        else:
            print("Paths can't be converted to absolute paths, since no PROJECT_ROOT is found!")


def set_wd(new_dir: str) -> None:
    """
    Set given directory as new working directory of the project.

    :param new_dir: name of new working directory (must be in project folder)
    """
    assert PROJECT_NAME in str(Path.cwd()), \
        f'Current working dir "{Path.cwd()}" is outside of project "{PROJECT_NAME}".'

    print("\033[94m" + f"Current working dir:\t{Path.cwd()}" + "\033[0m")  # print blue

    # Check if new_dir is folder path or just folder name
    change_dir = False
    if os.path.isabs(new_dir):
        found = Path(new_dir).is_dir()
        change_dir = Path(new_dir).absolute() != Path.cwd()
        if found and change_dir:
            os.chdir(new_dir)

    else:
        # Remove '/' if new_dir == 'folder/' OR '/folder'
        new_dir = "".join(new_dir.split("/"))

        found = new_dir == Path.cwd().name
        change_dir = not found

        # First look down the tree
        if not found:
            # Note: This works only for unique folder names
            for path in sorted(Path(PROJECT_ROOT).glob(f"**/{new_dir}"), key=lambda x: len(str(x))):  # 2. '_' == files
                change_dir = path != Path.cwd()
                if change_dir:
                    os.chdir(path)
                found = True
                break
    if found and change_dir:
        print("\033[93m" + f"New working dir:\t{Path.cwd()}\n" + "\033[0m")  # yellow print
    elif found and not change_dir:
        pass
    else:
        print("\033[91mGiven folder not found. Working dir remains:\t{Path.cwd()}\n\033[0m")  # red print


# %% Setup configuration object << o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o >><< o

# Instantiate config object
config = CONFIG()

# Load config file(s)
for config_file in Path(__file__).parent.glob("../configs/*config.toml"):
    if sys.version_info >= (3, 11):
        with open(config_file, "rb") as f:
            config.update(new_configs=toml.load(f))
    else:
        config.update(new_configs=toml.load(str(config_file)))

# Extract some useful globals
PROJECT_NAME = config.PROJECT_NAME

# Get project root path
if hasattr(config.paths, "PROJECT_ROOT"):
    PROJECT_ROOT = config.paths.PROJECT_ROOT
else:
    PROJECT_ROOT = __file__[:__file__.find(PROJECT_NAME) + len(PROJECT_NAME)]
    # Set root path to config file & update paths
    config.paths.PROJECT_ROOT = PROJECT_ROOT
    config.paths.update_paths()

# Extract paths
path_to = config.paths
params = config.params

# Welcome
print("\n" + ("*"*95 + "\n")*2 + "\n" + "\t"*10 + PROJECT_NAME + "\n"*2 + ("*"*95 + "\n")*2)

# Set project working directory
set_wd(PROJECT_ROOT)

# <<<<<<<<<<< ooo >>>>>>>>>>>>>> ooo <<<<<<<<<<< ooo >>>>>>>>>>>>>> ooo <<<<<<<<<<< ooo >>>>>>>>>>>>>> END
