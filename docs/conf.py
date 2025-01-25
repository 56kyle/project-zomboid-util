"""Sphinx configuration."""

project = "Project Zomboid Util"
author = "Kyle Oliver"
copyright = "2025, Kyle Oliver"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
