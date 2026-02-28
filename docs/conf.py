# Configuration file for the Sphinx documentation builder.

project = 'Plex Plugin Docs'
author = 'Xavier-Lam'

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = []

master_doc = 'index'

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'titles_only': False,
}

# Add GitHub link in the theme header (sphinx_rtd_theme uses these html_context keys)
html_context = {
    'display_github': True,
    'github_user': 'Xavier-Lam',
    'github_repo': 'plex-plugin-docs',
    'github_version': 'main',
    'conf_py_path': '/docs/',
}
