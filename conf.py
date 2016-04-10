#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- General configuration ------------------------------------------------

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'DFGraphics'
copyright = '2016, DFGraphics Team'
author = 'DFGraphics Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.  The full version, including alpha/beta/rc tags.
version = release = '0.1'

# There are two options for replacing |today|: either, you set `today` to some
# non-false value, or `today_fmt` is used as the format for a strftime call.
today_fmt = html_last_updated_fmt = '%Y-%%M-%D'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'graphics-packs', 'README.rst']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'ref'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    #'logo': 'logo.png',
    'github_user': 'DFgraphics',
    'github_repo': 'DFgraphics',
    'github_button': True,
    'travis_button': True,
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'DFGraphics Docs'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': [
        'about.html',
        'relations.html',
        'searchbox.html',
        'localtoc.html',
    ]
}

# If false, no module index is generated.  If false, no index is generated.
html_domain_indices = html_use_index = False

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'DFGraphics.tex', 'DFGraphics Documentation',
   'DFGraphics Team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = 'True'  # sphinx-build wants a string here...

# If false, no module index is generated.
latex_domain_indices = False


# -- Monkey-patch to silence warnings on README badges --------------------
# See https://stackoverflow.com/questions/12772927
try:
    import sphinx.environment
    from docutils.utils import get_source_line

    def _warn_node(self, msg, node):
        if not msg.startswith('nonlocal image URI found:'):
            self._warnfunc(msg, '%s:%s' % get_source_line(node))

    sphinx.environment.BuildEnvironment.warn_node = _warn_node
except:
    pass
