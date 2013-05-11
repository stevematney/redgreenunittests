from django.test.simple import DjangoTestSuiteRunner
import redgreenunittest

class RedGreenTestSuiteRunner(DjangoTestSuiteRunner):
    def run_suite(self, suite, **kwargs):
        return redgreenunittest.TextTestRunner(
            verbosity=self.verbosity, failfast=self.failfast).run(suite)
