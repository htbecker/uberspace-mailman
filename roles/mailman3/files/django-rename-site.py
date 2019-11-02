# This script will rename the default site if it exists
# otherwise just quit.
# It expects to get the domain and name as arguments

import sys, os, django
domain = sys.argv[1]
name = sys.argv[2]

# need to append the directory to path otherwise
# settings is not found
sys.path.append(os.getcwd())

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
django.setup()

from django.contrib.sites.models import Site
try:
  site = Site.objects.get(name='example.com')
  site.name = name
  site.domain = domain
  site.save()
  print("renamed site")
except django.contrib.sites.models.Site.DoesNotExist:
  print("example.com not found")
