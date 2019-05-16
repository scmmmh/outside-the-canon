#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from filters import json_strftime


# Site defaults
AUTHOR = 'Mark Hall'
SITENAME = 'Under the Surface'
SITE_TAGLINE = 'Authors in hiding from the Canon'
BASE_SITEURL = ''
SITEURL = ''

# Path configuration
PATH = 'content'

PAGE_PATHS = ['people', 'pages']

ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

# Internationalisation
TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'
LANGUAGES = (
    ('de', 'Deutsch'),
    ('en', 'English'),
)
LANGUAGE_LABELS = dict(LANGUAGES)

# Plugins
PLUGINS = ('person_reader', )

# Theme configuration
THEME = './theme'
PERSON_METADATA = (
    ('Names', 'names', 'string'),
    ('Sex or Gender', 'gender', 'string'),
    ('Country of Citizenship', 'country_of_citizenship', 'string'),
    ('Date of Birth', 'date_of_birth', 'timestamp'),
    ('Location of Birth', 'location_of_birth', 'string'),
    ('Date of Death', 'date_of_death', 'timestamp'),
    ('Location of Death', 'location_of_death', 'string'),
    ('Residence', 'residence', 'string'),
    ('Languages used', 'languages_used', 'string'),
    ('Occupation', 'occupation', 'string'),
    ('Field of Work', 'field_of_work', 'string'),
    ('Religion', 'religion', 'string'),
    ('Religious Order', 'religious_order', 'string'),
    ('Canonisation Status', 'canonisation_status', 'string'),
)
PERSON_LINK_CATEGORIES = (
    ('Wikidata', 'wikidata'),
    ('Wikipedia', 'wikipedia'),
    ('VIAF', 'viaf'),
    ('GND', 'gnd'),
)
JINJA_FILTERS = {
    'format_timestamp': json_strftime
}

DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = []

# Social widget
SOCIAL = []

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
