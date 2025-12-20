# {{ cookiecutter.project_name }}

    Period:     {% now 'local', '%Y-%m' %} - ...
    Status:     work in progress

    Author(s):  {{ cookiecutter.full_name }}
    Contact:    {{ cookiecutter.email }}

***

![Last update](https://img.shields.io/badge/last_update-{% now 'local', '%b_%e,_%Y' %}-green)
[![🚀 scilaunch](https://img.shields.io/badge/based%20on-🚀%20scilaunch-salmon "🚀")](https://shescher.github.io/scilaunch/)

*In general, one can add READMEs in nearly every folder.
The guiding principle should always be that any person who is not familiar with the project can find their way exclusively via the READMEs
– 'This may be you one day'*

## Project description

{{ cookiecutter.project_short_description }}

## Project structure

*A brief description of the project's folder structure (Where is what?).
Anticipate new lab members who are supposed to be able to orientate within this structure without your help.
At the same time, avoid too detailed descriptions.
Down the folder structure, there are supposed to be further READMEs explaining subsequent folders & data.*

## Install research code as a package

In case there is no project-related virtual / conda environment yet, create one for the project:

```shell
conda create -n {{ cookiecutter.project_slug[:4]}}_{{cookiecutter.python_version[:4] }} python={{ cookiecutter.python_version }}
```

And activate it:

```shell
conda activate {{ cookiecutter.project_slug[:4]}}_{{cookiecutter.python_version[:4] }}
```

Then install the code of the research project as a `Python` package:

```shell
# assuming your current working directory is the project root
pip install -e ".[develop]"
```

**Note**: The `-e` flag installs the package in editable mode,
i.e., changes to the code will be directly reflected in the installed package.
Moreover, the code keeps its access to the research data in the underlying folder structure.
Thus, the `-e` flag is recommended to use.

*R*-projects should be initialized in the project root `.` with, e.g., `RStudio` as *existing directory*.
Corresponding *R*-scripts can be stored in `./code/Rscripts/`

Similarly, use this structure for Matlab or other programming languages, which are employed in this project.

## Publications

*List publications resulted from this project (including papers, posters, talks, ...)*

## Preregistration

*If applicable, was the project pre-registered and if yes, when and where (link)*

## Contributors/Collaborators

*Name people who are involved in this project, their position and/or contribution.
Optional: add contact data.*

***

*Based on the [🚀 scilaunch](https://shescher.github.io/scilaunch/ "🚀") project structure.*
