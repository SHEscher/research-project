# Title: {{ cookiecutter.project_slug }}
# Description:  This script is an example script using R in your research project.
#               Adapt it to your liking.
# Author: {{ cookiecutter.full_name }}
# Contact: {{ cookiecutter.email }}
# Years: {% now 'local', '%Y' %}

# package dependencies
library(ggplot2)

# session info
# setwd(PROJECT_ROOT)
print(paste("Current working dir:", as.character(getwd())))
sessionInfo()

# code
print("put your R code here")
