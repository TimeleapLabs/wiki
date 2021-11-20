# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.append(os.path.abspath("./_ext"))

# -- Project information -----------------------------------------------------

project = "Kenshi"
license = "Apache 2.0"
author = "Pouya Eghbali"
version = "latest"
copyright = "Kenshi"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "video",
    "apex_chart",
    "sphinx_panels",
    "sphinxext.opengraph",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.katex"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

html_theme_options = {
    "navigation_with_keys": True,
    "light_css_variables": {
        "font-stack--monospace": '"Fira Code", monospace',
    },
    "dark_css_variables": {
        "font-stack--monospace": '"Fira Code", monospace',
    },
}

html_context = {
    "conf_py_path": "docs/source",  # Path in the checkout to the docs root
    "show_copyright": True,
    "furo_hide_toc": False,
    "root_url": "https://docs.kenshi.io"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/apexcharts/3.29.0/apexcharts.min.css',
    'css/custom.css',
]

html_js_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/medium-zoom/1.0.6/medium-zoom.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/apexcharts/3.29.0/apexcharts.min.js',
    'https://www.googletagmanager.com/gtag/js?id=G-R8SRWJG68W',
    'js/custom.js',
]


html_favicon = '_static/images/favicon.png'
html_logo = '_static/images/logo-512x512.png'
html_title = 'Kenshi Wiki'

pygments_style = "tokyo_night.TokyoNightLightStyle"
pygments_dark_style = "tokyo_night.TokyoNightStyle"

ogp_site_url = f"https://docs.kenshi.io"
ogp_type = "article"

mermaid_init_js = "mermaid.initialize({startOnLoad:true,theme:'dark',sequence:{showSequenceNumbers:true}});"
katex_prerender = True
