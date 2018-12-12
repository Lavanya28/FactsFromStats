
import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)
from app1.models import Articles


a = Articles.objects.create()
   