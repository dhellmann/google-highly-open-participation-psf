# Recording test coverage #

Test coverage is a great way to target your automated test efforts; see HowToTest.

There are two coverage analysis tools available for Python; one is
[coverage.py](http://nedbatchelder.com/code/modules/coverage.html), and the other
is [figleaf](http://darcs.idyll.org/~t/projects/figleaf/README.html).  The basic idea
behind both is that you run your test script(s) under the control of coverage or figleaf, and then ask them to output a test coverage summary.  Just look at the instructions in the linked pages for how to do this.

The only real trick to using either of these tools to measure code coverage of a newly compiled Python is to make sure to execute your scripts with the right version of Python.  For example, you would have to do

```
./python /path/to/figleaf Lib/test/regrtest.py
```

in the Python compilation directory in order to use figleaf to record code coverage with the right version of Python.