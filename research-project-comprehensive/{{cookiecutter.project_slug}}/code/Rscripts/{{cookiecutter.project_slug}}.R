# Title: {{ cookiecutter.project_slug }}
# Description:  This script is an example script using R in your research project.
#               Adapt it to your liking.
# Author: {{ cookiecutter.full_name }}
# Years: {% now 'local', '%Y' %}

# package dependencies
library(ggplot2)
source("code/Rscripts/configs.R")
# exposes config, paths, params, PROJECT_NAME, PROJECT_ROOT

# session info
# setwd(PROJECT_ROOT)
print(paste("Current working dir:", as.character(getwd())))
sessionInfo()
print(paste("The data folder is at:", config$paths$DATA))
print(paste("The weight decay is set to:", config$params$weight_decay))

# code
print("put your R code here")
