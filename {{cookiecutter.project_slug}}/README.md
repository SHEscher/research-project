# {{ cookiecutter.project_name }}

`[Last update: {% now 'local', '%B%e, %Y' %}]`

***
Period: {% now 'local', '%Y-%m' %} - ... <br>
Status: in preparation / work in progress / finalized

Author(s): {{ cookiecutter.full_name }} <br>
Contact:   {{ cookiecutter.email }}

***

*In general, one can add README's in nearly every folder. The guiding principle should always be that any person who is not familiar with the project can find their way exclusively via the README's. – 'It may be you one day'*

Check out following resources.

* https://www.makeareadme.com

* [The Simple Dublin Core Generator!](https://nsteffel.github.io/dublin_core_generator/generator_nq.html)

## Project description

*A brief general description of the project.*

## Project structure

*A brief description of the subsequent folder structure of the project (Where is what?). Anticipate new lab members who suppose to be able to orientate within this structure without your help. At the same time, avoid too detailed descriptions. Down the folder structure, there suppose to be further READMEs explaining subsequent folders & data.*

## Install project as package

```shell
CONDA_ENV_NAME="{{ cookiecutter.project_slug[:4]}}_{{cookiecutter.python_version[:4] }}"
conda create -n ${CONDA_ENV_NAME} python={{ cookiecutter.python_version }}
conda activate ${CONDA_ENV_NAME}
pip install --upgrade pip
pip install -e .
```

## Publications

*List resulted publications of this project here (including papers, posters, talks, ...)*

## Preregistration

*If applicable, was the project pre-registered and if yes, when and where (link)*

## Contributors/Collaborators

*Name people who are involved in this project, their position and/or contribution.
Optional: add contact data*