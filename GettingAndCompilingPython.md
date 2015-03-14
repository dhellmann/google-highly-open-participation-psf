## Checking Out the Source ##

The source code for Python is stored in a [Subversion](http://subversion.tigris.org/) repository hosted on a python.org server.  Refer to [the FAQ](http://www.python.org/dev/faq/#how-do-i-get-a-checkout-of-the-repository-read-only-and-read-write) for details of how to check out the source.

You do not need commit permissions in the repository for any of the PSF-sponsored tasks for [the Google Highly Open Participation Contest](http://code.google.com/opensource/ghop/2007-8).  Each task includes details about how to submit your code or documentation changes, where appropriate.  In most cases, it will only be necessary to attach patches or files to the task and indicate that you have completed the work.

All tasks, unless stated explicitly, apply to Python version 2.6.  Use the URL http://svn.python.org/projects/python/trunk to check out a copy of the source for Python 2.6, if the task requires it.

For tasks based on Python 3.0, check out the source from http://svn.python.org/projects/python/branches/py3k/.

## Using Subversion ##

There are many tutorials on Subversion available on the net, so here's only a
very quick tour of frequently-used commands:

  * use `svn checkout URL` to check out a source tree
  * use `svn update` to update the source tree (you should do this frequently)
  * use `svn status` to see which files you changed locally
  * use `svn diff` to see in detail what changes you made locally, and to create patch files

Of course, for Windows there exist sophisticated graphical tools using which you don't
have to use the command line interface of Subversion.  Check out [TortoiseSVN](http://tortoisesvn.tigris.org/) for one free tool.

## Compiling Python from Source ##

If you are working on the Python core and want to test your changes, or you want to
test software with a fresh Python 3.0 (many things have happened since Alpha 1),
you need to compile it yourself.

### Linux and UNIX (Mac OS X) ###

In order to compile Python yourself, make sure you have installed GCC and related
build tools (e.g. the "build-essential" package on Ubuntu, or the Development Tools on Mac OS X). Then, in the root directory
of the Python checkout, execute the usual build steps:

```
./configure
make
```

Now you should have a `python` executable in the same directory, that when started,
runs the freshly compiled version of Python. It uses the standard library modules
from the `Lib/` directory.

### Windows ###

[Here are some instructions](http://ramblings.timgolden.me.uk/2007/11/22/building-the-python-trunk-with-visual-studio-2008-express/) for building Python on Windows with Visual Studio 2008 Express.