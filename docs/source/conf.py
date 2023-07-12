extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.imgconverter",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
source_suffix = ".rst"
root_doc = 'index'
project = "No Name"
year = "2023"
author = "Ugochukwu Nwosu"
copyright = f"{year}, {author}"
version = release = "0.0.0"
exclude_patterns = ['build']
modindex_common_prefix = ['no_name.']
templates_path = ["."]
extlinks = {
    "issue": ("https://github.com/ugognw/python-no-name/issues/%s", "#"),
    "pr": ("https://github.com/ugognw/python-no-name/pull/%s", "PR #"),
}

# -- Options for sphinx.ext.autodoc ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

autoclass_content = 'class'

# -- Options for Napoleon ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#module-sphinx.ext.napoleon

napoleon_google_docstring = True
napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_last_updated_fmt = '%a, %d %b %Y %H:%M:%S'
html_theme_options = {
    'source_repository': 'https://github.com/ugognw/python-no-name',
    'source_branch': 'main',
    'source_directory': 'docs/source',
}
pygments_style = 'sphinx'
pygments_dark_style = 'monokai'

smartquotes = True
html_split_index = False
html_short_title = f"{project}-{version}"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
