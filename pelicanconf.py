#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


#AUTHOR = u'NumFOCUS Foundation'
SITENAME = u'NumFOCUS Foundation'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = u'gumish'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# not Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('numfocus+subscribe@googlegroups.com', 'Join out mailing list'),
          ('https://groups.google.com/forum/#!forum/numfocus', 'Read the archives'),
          ('https://plus.google.com/communities/100008130850352595608', 'Google+'),
          ('https://github.com/numfocus', 'GitHub'),
          ('https://twitter.com/numfocus', 'Twitter'),
          )

MENUITEMS = [('Projects', 'projects.html'),
             ('Board', 'board.html'),
             ('Membership', 'membership.html'),
             ('Donations', 'donations.html'),
             ('Jobs', 'jobs.html'),
             ('Sponsors', 'sponsors.html'),
             ('Contact', 'contact.html'),
             ]

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sponsors')

EXTRA_TEMPLATE_PATHS = ('templates',)
#PAGINATED_DIRECT_TEMPLATES = []
DEFAULT_PAGINATION = False

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True