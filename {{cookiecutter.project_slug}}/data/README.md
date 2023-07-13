# {{ cookiecutter.project_name }} – **data**

`[Last update: {% now 'local', '%B %e, %Y' %}]`

***
Period: {% now 'local', '%Y-%m' %} - ... <br>
Status: in preparation / work in progress / finalized

Author(s): {{ cookiecutter.full_name }} <br>
Contact:   {{ cookiecutter.email }}

***

*Project data should lie in the `data/` folders, ideally in the [BIDS](https://bids-specification.readthedocs.io/en/stable/) format.
If your research data resides somewhere else and is too big to copy, you can easily create symbolic links from these sources to your `data/` folder in your project structure (`ln -s SOURCE_FOLDER ./data`).*

## Description of data

*List relevant information one needs to know about the (raw) data.
This could include how data was acquired.
Also, mention where are backups of raw data, intermediate preprocessed data, and derivatives.
Moreover, mention how the data is structured, e.g., in BIDS.*

## Preprocessing

*Which preprocessing steps were done, and why. List references and toolboxes (+version), & point to code*

## General information

*e.g. is it data from a multi-centre study, is the data part of a bigger project, who needs to be contacted, in case of ...*

## COPYRIGHT/LICENSE

*One could add information about data sharing, license and copy right issues*