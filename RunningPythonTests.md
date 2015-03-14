Every time you change the code of some Python standard library module,
before you submit the change you have to run the test suite to make
sure all regression tests still pass.

You do this by either
  * running `make test` in the root of the source tree or
  * running `Lib/test/regrtest.py`; make sure you use **the interpreter that you compiled yourself in that source tree**.  In UNIX/Linux/Mac OS X you can do that by typing `./python Lib/test/regrtest.py`.

The regrtest script then runs all regression tests (actually not all -- some are excluded by default because they take lots of time or need additional resources such as an audio device). After that process, which take some 10 minutes, it reports skips and failures, like so:

```
2 tests failed:
    test_compiler test_parser
21 tests skipped:
    test_aepack test_al test_applesingle test_bsddb185 test_cd test_cl
    test_gl test_hashlib_speed test_imgfile test_ioctl test_macfs
    test_macostools test_nis test_pep277 test_plistlib
    test_scriptpackages test_sunaudiodev test_tcl test_unicode_file
    test_winreg test_winsound
```

The skipped tests are mostly expected (for example, Windows-specific tests
will be skipped on Linux), but failures indicate that your change is not complete
or correct.

While you're working on one specific module, you might want to run tests that focus on that module.  You can do so like this:

```
./python Lib/test/regrtest.py test_doctest
```

to run just the doctest-module tests.