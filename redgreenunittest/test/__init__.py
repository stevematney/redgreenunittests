import os
import sys
import redgreenunittest


here = os.path.dirname(__file__)
loader = redgreenunittest.defaultTestLoader

def suite():
    suite = redgreenunittest.TestSuite()
    for fn in os.listdir(here):
        if fn.startswith("test") and fn.endswith(".py"):
            modname = "redgreenunittest.test." + fn[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTest(loader.loadTestsFromModule(module))
    return suite


if __name__ == "__main__":
    redgreenunittest.main(defaultTest="suite")
