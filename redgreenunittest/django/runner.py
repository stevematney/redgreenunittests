# -*- coding: utf-8 -*-

# !important
# Native
# Django
from django.test.runner import DiscoverRunner
# 3rd Party
import redgreenunittest
# Custom


class RedGreenDiscoverRunner(DiscoverRunner):
    def run_suite(self, suite, **kwargs):
        return redgreenunittest.TextTestRunner(
            verbosity=self.verbosity,
            failfast=self.failfast,
        ).run(suite)
