import os
import sys	
sys.path.append('~/public_html/redevelopingcountries.com/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'JennaBlog.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
