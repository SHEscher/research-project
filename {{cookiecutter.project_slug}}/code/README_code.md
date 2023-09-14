# {{ cookiecutter.project_name }} – **code**

`[Last update: {% now 'local', '%B %e, %Y' %}]`

***
Period: {% now 'local', '%Y-%m' %} - ... <br>
Status: in preparation / work in progress / finalized

Author(s): {{ cookiecutter.full_name }} <br>
Contact:   {{ cookiecutter.email }}

***

## Description of analysis

*List relevant information one needs to know about the analysis. For instance, one could describe the computational model that was applied, and which statistical approach has been chosen for.*

## Preprocessing

*General information regarding preprocessing could be written in the data [README.md](../data/README.md). One could add here more implementation-specific information (e.g., which toolboxes were used)*

## Codebase

*Refer to the corresponding code/scripts written for the analysis. Which languages (Python, R Matlab, ...) where used? Are there specific package versions, which one should take care of? Or is there a container (e.g., Docker) or virtual environment?*

### Python
Pyhton code (in the structure of a python package) is stored in `./code/{{ cookiecutter.project_slug }}/`

#### Jupyter Notebooks
Jupyter notebooks are stored in `./code/notebooks/`

### R
*Initialize a new R-project in the project root of `{{ cookiecutter.project_slug }}` with `RStudio`. R-scripts can be stored in `./code/Rscripts/`.
Use R-packages in Python with, e.g., [rpy2](https://rpy2.github.io/), or use Python packages in R using, e.g., [reticulate](https://rstudio.github.io/reticulate/)*.

### Configs

Paths to data, parameter settings, etc. are stored in the config file: `./code/configs/config.toml`

Private config files that contain, e.g., passwords, and therefore should not be shared,
or mirrored to a remote repository can be listed in: `./code/configs/private_config.toml`

To use configs, do the following in the python scripts:

```python
from {{ cookiecutter.project_slug }}.configs import config, path_to

# get the path to data
path_to_data = path_to.DATA

# Get parameter from config
weight_decay = config.params.weight_decay

# Get private parameter from config
api_key = config.service_x.api_key
```

For other programming languages, and corresponding script must be implemented.

## COPYRIGHT/LICENSE

*One could add information about code sharing (e.g., is the code published on [GitLab](https://gitlab.gwdg.de/users/sign_in) or Github ...), license and copy right issues*
