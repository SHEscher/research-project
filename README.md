# Research-Project – a cookiecutter template for research projects

![version](https://img.shields.io/badge/template_version-2.0.0-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template for (scientific) **research projects**.

## Usage

This template is used by [`scilaunch`](https://github.com/SHEscher/scilaunch) (a `cookiecutter` wrapper for scientific research projects):

```shell
# Install scilaunch
pip install -U scilaunch

# Create a new project in current folder
scilaunch

# alternatively link to parent folder
scilaunch path/to/parent/folder
```

The template can also be employed directly with [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) using:

```shell
cookiecutter gh:SHEscher/research-project
```

However, ideally use this template with `scilaunch` to create your project, since there is some additional magic happening in the background.

And this is an excerpt of what you get:

```
🚀 yourgreatstudy/
├── 📄 README.md
├── 📂 code
│   ├── 📁 Rscripts
│   ├── 📁 configs
│   ├── 📂 notebooks
│   │   └── 🐍 yourgreatstudy.ipynb
│   ├── 📁 tests
│   └── 📂 yourgreatstudy
│       ├── 🐍 __init__.py
│       └── 📁 preprocessing
├── 📂 data
│   ├── 📋 participants.tsv
│   ├── 📁 sub-01
│   ├── 📁 sub-02
│   └── 📁 sub-03
├── 📂 literature
│   ├── 📁 pdfs
│   └── 📙 yourgreatstudy.bib
├── 📂 organisation
│   ├── 📁 ethics
│   ├── 📁 participation_forms
│   ├── 📁 preregistration
├── 📂 publications
│   ├── 📁 articles
│   ├── 📁 poster
│   └── 📁 presentations
├── 📄 pyproject.toml
├── 📂 results
│   └── 📁 datavisualization
└── 🐍 setup.py
```

## TODO's

- [ ] Option to add multiple authors
- [ ] Option to add project keywords
- [ ] Optional: Add examples for other data types than MRI, including simulation studies
- [ ] ...

## Credits

Thanks to [audreyfeldroy](https://github.com/audreyfeldroy) for her inspiration with her [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) and the great [cookiecutter](https://github.com/cookiecutter/cookiecutter) package in general.
