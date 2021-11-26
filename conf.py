"""Demonstrate sphinx issue 9891 https://github.com/sphinx-doc/sphinx/issues/9891"""

import os
import sys

sys.path.insert(0, os.path.abspath("."))

project = "Sphinx Issue"
copyright = "2021, Michael McNeil Forbes"
author = "Michael McNeil Forbes"
extensions = [
    "sphinx.ext.autosummary",
    "myst_parser",
]


# This ordering works
source_suffix = {
    ".rst": "restructuredtext",
    ".myst": "myst",
}

# This ordering here breaks autosummary
source_suffix = {
    ".myst": "myst",
    ".rst": "restructuredtext",
}
