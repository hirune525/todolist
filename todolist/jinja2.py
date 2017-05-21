# -*- coding:utf-8 -*
from jinja2 import Environment

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from datetime import datetime


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'now': datetime.now,
    })
    return env
