WHAT?!
===

This is literally an exact clone of unittest (from Python 2.7), but with colors.

HOW?!
===

You literally use it in the exact same way as [unittest](http://docs.python.org/2/library/unittest.html).

INSTALLATION?!
===

You can just install it into your path or your sourced virtual environment with this extremely easy command:

    pip install redgreenunittest

After that, just reference this package like a normal, regular old python package like this:

    import redgreenunittest

If you do want to use it as a direct replacement for unittest without doing any extra work, you can just import like this:

    import redgreenunittest as unittest

BUT WHAT ABOUT DJANGO?!
===

I assume you mean the Python framework. (Not that movie.) Remember when I said, "exact clone" before? I lied. There is one extra directory called "django" in there that contains a file called "simple.py"

If you want to use this as your test runner, and you're already using unittest, you can literally drop this line of code into your settings.py file, and it will straight up work if you followed those installation instructions. In fact you could even skip the referencing step since Python is smart.

    TEST_RUNNER="redgreenunittest.django.runner.RedGreenDiscoverRunner"

Go ahead. Run your tests. Colors. It's like we live in the future.

DJANGO < 1.6
==

Running a Django version pre-1.6? Then you'll want the simple runner.

    TEST_RUNNER="redgreenunittest.django.simple.RedGreenTestSuiteRunner"


CAVEATS?!
===

Ok, so if you're using a vim gui like MacVim or GVim and its shell to run your tests, they're going to look super weird. Sorry. You're boned for colors in that shell. You can use [conque](https://code.google.com/p/conque/) if you want. I made it work using [zsh](http://www.zsh.org/) and [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) and some medium-level vim scripting.

The reason it sucks is because `$TERM` is set to `dumb` in the vim gui shell ([literally](http://stackoverflow.com/a/13382717/1687623)). So if you're using any other shell where `$TERM` is set to `dumb`, you're also going to be boned in that case.

You may be boned in other scenarios. My experience in this area is limited. Let me know if you find yourself boned in other situations. I may be able to help, or I can at least make a note in this README.
