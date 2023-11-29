# {{ cookiecutter.project_name }} – **code**

    Last update:    {% now 'local', '%B %e, %Y' %}
    Status:         work in progress

***

## Description

*List relevant information one needs to know about the code of this research project.
For instance, one could describe the computational model that was applied,
and which statistical approach has been chosen for.*

## Preprocessing

*General information regarding preprocessing could be written in the data [README.md](../data/README.md).
One could add here more implementation-specific information (e.g., which toolboxes were used).*

## Codebase

*Refer to the corresponding code/scripts written for the analysis/simulation/etc.
Which languages (Python, R, Matlab, ...) were used? Are there specific package versions,
which one should take care of? Or is there a container (e.g., Docker) or virtual environment?*

### R

*Initialize a new R-project in the project root of `{{ cookiecutter.project_slug }}` with `RStudio`.
R-scripts can be stored in `./code/Rscripts/`.*.

### Configs

Paths to data, parameter settings, etc. can be stored in the config file: `./code/configs/config.toml`

Private config files that contain, e.g., passwords, and therefore should not be shared,
or mirrored to a remote repository can be listed in: `./code/configs/private_config.toml`

*Fill the corresponding `*config.toml` files with your data. A script must be implemented to use these `*config.toml`.*

## COPYRIGHT/LICENSE

*One could add information about code sharing
(e.g., is the code published on GitLab or GitHub ...),
license and copy right issues*
