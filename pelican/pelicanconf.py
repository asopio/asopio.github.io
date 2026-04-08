import datetime

AUTHOR = 'Alex Sopio'
SITENAME = 'Alex Sopio'
SITEURL = ''

PATH = 'content'
THEME = 'theme'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

# Feeds — disabled for local development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL scheme
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Content source paths
ARTICLE_PATHS = ['']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# Direct templates: index = homepage, blog = /blog/ listing
DIRECT_TEMPLATES = ['index', 'blog']
INDEX_SAVE_AS = 'index.html'
BLOG_SAVE_AS = 'blog/index.html'

# Suppress unused auto-generated pages
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

# Site variables available in templates
SITE_DESCRIPTION = 'Physicist & AI Scientist — research, publications, and blog'
GITHUB_USERNAME = 'asopio'

# Expose datetime.now to Jinja2 templates (used for copyright year)
JINJA_GLOBALS = {'now': datetime.datetime.now}
