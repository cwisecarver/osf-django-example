# -*- coding: utf-8 -*-
'''Consolidates settings from defaults.py and local.py.
::
    >>> from project import settings  # BAD
    >>> from django.conf import settings  # GOOD
    >>> settings.API_BASE
    'v2/'
'''
import warnings

from .defaults import *  # noqa

try:
    from .local import *  # noqa
except ImportError as error:
    warnings.warn('No project/settings/local.py settings file found. Did you remember to '
                  'copy local-dist.py to local.py?', ImportWarning)
