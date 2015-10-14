"""
WSGI config for yolobid project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application
#from mezzanine.utils.conf import real_project_name

#os.environ.setdefault("DJANGO_SETTINGS_MODULE",
#                      "%s.settings" % real_project_name("yolobid"))

#application = get_wsgi_application()

import os
import time
import traceback
import signal
from django.core.wsgi import get_wsgi_application
import sys
from mezzanine.utils.conf import real_project_name

try:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","%s.settings" % real_project_name("yolobid"))
    application = get_wsgi_application()
    print('WSGI without exception')
except Exception:
    print('handling WSGI exception')
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)
