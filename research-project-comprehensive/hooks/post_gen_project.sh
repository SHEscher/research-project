#!/bin/bash

# Create a new conda environment and activate it
{% if cookiecutter.create_conda_env -%}

# Define the base environment name
BASE_CONDA_ENV_NAME="{{ cookiecutter.project_slug[:4]}}_{{cookiecutter.python_version[:4] }}"
# Initialize the counter
counter=0

# Generate the initial environment name
CONDA_ENV_NAME="${BASE_CONDA_ENV_NAME}"
# Loop until no matching environment name is found
while conda env list | grep -q -w "$CONDA_ENV_NAME"; do
    # Append the counter to the environment name
    if [ $counter -gt 0 ]; then
        echo "The conda environment name '$CONDA_ENV_NAME' does already exist. Adapting the name ..."
        CONDA_ENV_NAME="${BASE_CONDA_ENV_NAME}_${counter}"
    fi
    counter=$((counter + 1))
done

echo -e "\033[34mCreating and activating conda environment ${CONDA_ENV_NAME} ...\n\033[0m"
# Check if conda is available
if command -v conda >/dev/null 2>&1; then
    # Create a new environment with Python version 3.8
    if conda env list | grep -q "^${CONDA_ENV_NAME}\s"; then
        echo -e "\033[32mConda environment ${CONDA_ENV_NAME} already exists.\033[0m"
    else
        conda create --name ${CONDA_ENV_NAME} python={{ cookiecutter.python_version }} -y
    fi

    # Activate the new environment

    # List of files to source (bit of a hacky way to do it)
    files=("${HOME}/.bash_profile" "${HOME}/.bashrc" "${HOME}/.zprofile" "${HOME}/.zshrc" "${HOME}/.profile")

    # which conda
    # whereis conda

    # Loop over files and source them if they exist and contain __conda_setup
    # (this is necessary for the subprocess spawned by cookiecutter)
    for file in "${files[@]}"; do
        if test -f "$file"; then
            if grep -q "^__conda_setup" "$file"; then
                source "$file"
            fi
        fi
    done

    echo "Activate conda environment '${CONDA_ENV_NAME}' ..."
    conda activate ${CONDA_ENV_NAME}
    echo "Conda environment '${CONDA_DEFAULT_ENV}' is activated."

    # Install the project in editable mode
    # conda run -n ${CONDA_ENV_NAME} python -m pip install -e .  # this does not always work
    echo -e "\033[34m\nInstalling '{{ cookiecutter.project_slug }}' as python package in editable mode ...\n\033[0m"
    ${CONDA_PREFIX}/bin/python -m pip install -e ".[develop]"
    # We are already root folder of {{ cookiecutter.project_slug }} so . is enough

    # Add the new environment as kernel to jupyter (notebook and lab)
    echo -e "\033[34m\nAdding conda environment '${CONDA_ENV_NAME}' as kernel to jupyter ...\n\033[0m"
    ${CONDA_PREFIX}/bin/python -m ipykernel install --user --name=${CONDA_ENV_NAME}


else
    echo -e "\033[31mconda is not available. Please install conda and try again.\033[0m"
fi
{% endif %}
