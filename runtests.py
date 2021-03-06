#!/usr/bin/env python

from os.path import dirname, abspath
import sys

from django.conf import settings as django_settings

if not django_settings.configured:
    django_settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            },
        },
        INSTALLED_APPS=(
            'django.contrib.sessions',
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'lockdown',
        ),
        ROOT_URLCONF='lockdown.tests.urls',
    )

def runtests(*test_args):
    if not test_args:
        test_args = ['lockdown']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    from django.test.simple import DjangoTestSuiteRunner
    runner = DjangoTestSuiteRunner(verbosity=1, interactive=True)
    failures = runner.run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
