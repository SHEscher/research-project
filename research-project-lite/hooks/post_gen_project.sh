#!/bin/bash

# Activate git in the project
{% if cookiecutter.init_git -%}
# check if .git/ exists
if [ -d ".git" ]; then
    echo -e ""
else
    echo -e "\033[34m\nActivating git in {{ cookiecutter.project_slug }} ...\n\033[0m"
    git init --initial-branch=main
fi
{% endif %}
