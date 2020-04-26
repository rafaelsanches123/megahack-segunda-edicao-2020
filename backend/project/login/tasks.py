from __future__ import absolute_import, unicode_literals

from celery import shared_task

import os, json

@shared_task
def function_1(params):
    return 0