import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "missinghack.settings")
from hypothesis.extra.django import from_model


from case.models import Report
c = from_model(Report).example()