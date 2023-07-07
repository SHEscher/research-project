#!/bin/zsh

# Create a new conda environment and activate it
{% if cookiecutter.create_conda_env == 'y' -%}
CONDA_ENV_NAME="{{ cookiecutter.project_slug[:4]}}_{{cookiecutter.python_version[:4] }}"
echo "Creating and activating conda environment ${CONDA_ENV_NAME} ..."
# Check if conda is available
if command -v conda >/dev/null 2>&1; then
    # Create a new environment with Python version 3.8
    if conda env list | grep -q "^${CONDA_ENV_NAME}\s"; then
        echo "Conda environment ${CONDA_ENV_NAME} already exists."
    else
        conda create --name ${CONDA_ENV_NAME} python={{ cookiecutter.python_version }}
    fi

    # Activate the new environment
    
    # List of files to source
    files=("${HOME}/.bash_profile" "${HOME}/.bashrc" "${HOME}/.zprofile" "${HOME}/.zshrc" "${HOME}/.profile")

    # Loop over files and source them if they exist
    for file in "${files[@]}"; do
        if test -f "$file"; then
            # echo "$file"
            source "$file"
        fi
    done

    echo "Activate conda environment '${CONDA_ENV_NAME}' ..."
    conda activate ${CONDA_ENV_NAME}
    echo "Conda environment '${CONDA_DEFAULT_ENV}' is activated." 
    
    # Install the project in editable mode
    conda run -n ${CONDA_ENV_NAME} pip install --upgrade pip
    conda run -n ${CONDA_ENV_NAME} pip install -e .
    # We are already root folder of {{ cookiecutter.project_slug }} so . is enough

else
    echo "conda is not available. Please install conda and try again."
fi
{% endif %}

# Activate git in the project
{% if cookiecutter.init_git == 'y' -%}
echo "Activating git in {{ cookiecutter.project_slug }} ..."
git init
{% endif %}