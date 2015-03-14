# Basic Testing Concepts #

The basic idea behind all of the testing you'll have to do for this contest is to **automate** code tests.  This boils down to two things: understanding what the code is _supposed_ to do, and then making sure that _it does that_ by writing code to exercise specific functionality.

For example, suppose you have a function sum(...).  Here are some simple tests:

```
x = sum(5, 6)
assert x == 11

x = sum(-1, 1)
assert x == 0

x = sum(1, 1, 1, 1)
assert x == 4
```

(Here, `assert` fails if the condition specified isn't true.)

For any real function or application, there are an infinitude of things to test, but some tests are always better than none.  The art of testing starts with simply _doing something_.  When starting to write new tests, **test small** -- start out by simply running some of the code.  Then think a bit about how a specific function or group of functions **should** be working, and write some speculative code (that you think should work, based on your understanding of the docs).  If that codes does work, then great -- save it and integrate it into the automated tests!  If not, try to figure out whether or not you misunderstood or the test is broken.

## Python testing frameworks ##

There are several testing frameworks in Python to help you manage tests: [unittest](http://docs.python.org/lib/module-unittest.html) and [doctest](http://docs.python.org/lib/module-doctest.html) are included with Python, and you'll need to use them if you're doing any work on core Python.  Most thirdparty packages use these tools, too, although some may use py.test or nose.  The documentation for the package should say.

doctest is pretty self-explanatory and the documentation is good.  unittest is quite a bit more complicated and you'll probably have to look at existing unit tests in order to figure out how to write your own.  Ask for help if you need it.

See RunningPythonTests to run the tests that are included with the Python distribution.

## Targetting new tests with code coverage ##

You may notice that many of the tasks ask you to "increase code coverage".  Code coverage measures which lines of code are executed by a particular test; see RecordingTestCoverage for technical details.  Now, 100% code coverage doesn't _guarantee_ that code is good, but any code that isn't run by a test is definitely not being tested.  So your minimum goal for these tasks should be to increase code coverage, but the **real** goal is to do a more thorough job of testing the code's functionality.  Keep that in mind when you're writing the tests and you'll do a better job.

Note that if you discover a bug in the course of testing, that counts heavily towards extra credit!