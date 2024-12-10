"""Configuration file for the Sphinx documentation builder."""


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "IPyNiiVue"
project_copyright = "2024, Jan-Hendrik Müller, Trevor Manz, Bradley Alford, Anthony Androulakis, Taylor Hanayik, Christian O'Reilly"
author = "Jan-Hendrik Müller, Trevor Manz, Bradley Alford, Anthony Androulakis, Taylor Hanayik, Christian O'Reilly"
release = "2.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pyramid"
html_static_path = ["_static"]
