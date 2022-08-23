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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import re
import datetime

# -- Project information -----------------------------------------------------

project = 'SpKit'
#copyright = '2022, Nikesh Bajaj'
copyright = '2019-%s, Nikesh Bajaj' % datetime.date.today().year
author = 'Nikesh Bajaj'

# The full version, including alpha/beta/rc tags
release = '0.0.9.4'

import spkit
version = re.sub(r'\.dev0+.*$', r'.dev', spkit.__version__)
release = spkit.__version__

print("spkit (VERSION %s)" % (version,))

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = []
#extensions = ['sphinx.ext.autodoc']
# extensions = ['sphinx.ext.doctest', 'sphinx.ext.autodoc', 'sphinx.ext.todo',
#               'sphinx.ext.extlinks', 'sphinx.ext.mathjax',
#               'sphinx.ext.autosummary', 'numpydoc',
#               'sphinx.ext.intersphinx',
#               'matplotlib.sphinxext.plot_directive']
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
#exclude_patterns = []
exclude_trees = ['_build']


source_suffix = '.rst'
master_doc = 'index'



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'press'
#html_theme = 'python_docs_theme'
#html_theme = 'sphinxdoc'
#html_theme = 'karma_sphinx_theme'


#import sphinx_pdj_theme
#html_theme = 'sphinx_pdj_theme'
#html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]

pygments_style = 'sphinx'

modindex_common_prefix = ['spkit.']

html_theme = 'nature'

#html_favicon = 'favicon.ico'
#html_favicon = 'docs/figures/spkitlogo1.ico'
html_favicon = '_static/spkitlogo6.ico'




html_last_updated_fmt = '%b %d, %Y'

html_title = 'SpKit'
import spkit


#html_sidebars = {
#   '**': ['localtoc.html', "relations.html", 'quicklinks.html', 'searchbox.html', 'editdocument.html'],
#}
html_sidebars = {
   '**': ['localtoc.html', "relations.html", 'quicklinks.html', 'searchbox.html'],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_show_sourcelink = False


html_use_opensearch = 'http://spkit-doc.readthedocs.org'

htmlhelp_basename = 'spkit-doc'


numpydoc_class_members_toctree = False

autodoc_typehints = "description"

# Don't show class signature with the class' name.

autodoc_class_signature = "separated"

# plot_directive options
plot_include_source = True
plot_formats = [('png', 96), 'pdf']
plot_html_show_formats = False
plot_html_show_source_link = False

intersphinx_mapping = {
    'numpy': ('https://numpy.org/devdocs', None)}
