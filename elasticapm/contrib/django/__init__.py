"""
opbeat.contrib.django
~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2011-2012 Opbeat

Large portions are
:copyright: (c) 2010 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

default_app_config = 'elasticapm.contrib.django.apps.OpbeatConfig'

from elasticapm.contrib.django.client import *