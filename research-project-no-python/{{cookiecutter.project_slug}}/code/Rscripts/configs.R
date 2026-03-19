# Title: configs
# Description:  Configurations for the {{ cookiecutter.project_name }} project.
#               Reads all *config.toml files from the configs/ folder and provides
#               config, paths, params, PROJECT_NAME, and PROJECT_ROOT for use in R scripts.
#
# Usage:
#   source("code/Rscripts/configs.R")
#   # Then access: config, paths, params, PROJECT_NAME, PROJECT_ROOT
#   # Example: print(config$paths$data_dir) or print(PROJECT_ROOT)
#
# Note:
#   * store private configs in the same folder as 'config.toml', namely: "./[PRIVATE_PREFIX]_configs.toml"
#   * keep the prefix such that it is ignored by git
#
# Author: Simon M. Hofmann
# GitHub: SHEscher
# Years: 2026

# Install/load RcppTOML for TOML parsing
if (!requireNamespace("RcppTOML", quietly = TRUE)) {
    install.packages("RcppTOML")
}
library(RcppTOML)

# --- Locate config files ---
# Resolve the path to the configs/ folder relative to this script's location
.configs_dir <- file.path(dirname(sys.frame(1)$ofile %||% "."), "..", "configs")
.configs_dir <- normalizePath(.configs_dir, mustWork = FALSE)

# If script location detection fails, fall back to project-relative path
if (!dir.exists(.configs_dir)) {
    .configs_dir <- "code/configs"
}

# --- Load and merge all *config.toml files ---
.merge_lists <- function(base, new) {
    # Recursively merge two nested lists (new values override base)
    for (name in names(new)) {
        if (is.list(base[[name]]) && is.list(new[[name]])) {
            base[[name]] <- .merge_lists(base[[name]], new[[name]])
        } else {
            base[[name]] <- new[[name]]
        }
    }
    base
}

config <- list()
.config_files <- sort(list.files(.configs_dir, pattern = "config\\.toml$", full.names = TRUE))

if (length(.config_files) == 0) {
    warning("No *config.toml files found in: ", .configs_dir)
} else {
    for (.cf in .config_files) {
        .parsed <- parseTOML(.cf)
        config <- .merge_lists(config, .parsed)
    }
}

# --- Extract useful globals ---
PROJECT_NAME <- config$PROJECT_NAME

# Determine PROJECT_ROOT
if (!is.null(config$paths$PROJECT_ROOT)) {
    PROJECT_ROOT <- normalizePath(config$paths$PROJECT_ROOT, mustWork = FALSE)
} else {
    # Walk up from the configs dir to find the project root (the folder named PROJECT_NAME)
    .candidate <- normalizePath(.configs_dir, mustWork = FALSE)
    PROJECT_ROOT <- NULL
    while (.candidate != dirname(.candidate)) {
        if (basename(.candidate) == PROJECT_NAME) {
            PROJECT_ROOT <- .candidate
            break
        }
        .candidate <- dirname(.candidate)
    }
    if (is.null(PROJECT_ROOT)) {
        PROJECT_ROOT <- getwd()
        warning("Could not determine PROJECT_ROOT; falling back to working directory: ", PROJECT_ROOT)
    }
    config$paths$PROJECT_ROOT <- PROJECT_ROOT
}

# --- Resolve relative paths to absolute paths ---
.resolve_paths <- function(lst, parent_path) {
    for (name in names(lst)) {
        val <- lst[[name]]
        if (is.list(val)) {
            lst[[name]] <- .resolve_paths(val, parent_path)
        } else if (is.character(val) && !startsWith(val, "/")) {
            # Resolve relative paths (those starting with "./" or lacking "/")
            candidate <- file.path(parent_path, val)
            if (grepl("^\\./|^[^/]", val)) {
                lst[[name]] <- normalizePath(candidate, mustWork = FALSE)
            }
        }
    }
    lst
}

config$paths <- .resolve_paths(config$paths, PROJECT_ROOT)

# --- Provide convenient access ---
paths <- config$paths
params <- config$params

# --- Set working directory to PROJECT_ROOT ---
if (dir.exists(PROJECT_ROOT)) {
    cat(sprintf("Current working dir:\t%s\n", getwd()))
    setwd(PROJECT_ROOT)
    cat(sprintf("New working dir:\t%s\n", getwd()))
}

# --- Welcome ---
.w <- 95
cat(paste0(
    "\n", strrep("*", .w), "\n", strrep("*", .w), "\n\n",
    strrep(" ", max(0, (.w - nchar(PROJECT_NAME)) %/% 2)), PROJECT_NAME, "\n\n",
    strrep("*", .w), "\n", strrep("*", .w), "\n\n"
))

# Clean up helper objects
rm(list = intersect(
    c(".configs_dir", ".config_files", ".cf", ".parsed", ".candidate", ".w",
      ".merge_lists", ".resolve_paths"),
    ls(all.names = TRUE)
))
