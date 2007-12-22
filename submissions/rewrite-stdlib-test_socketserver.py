tags = "core,test"

summary = """
Rewrite test_socketserver to use unittest.
"""

description = """
Rewrite the following stdlib tests to use unittest:

	test_socketserver

See test_time or test_userdict (among many others) for an example of how to
structure the end of the script so that it can be run by regrtest as well as
from the command line.

Completion:

Attach the result of an 'svn diff' to this task and contact the
ghop-python mailing list.

Relevant Wiki pages:

 - HowToTest
 - RunningPythonTests
 - GettingAndCompilingPython

"""

owner = "bcannon,georg.brandl"
