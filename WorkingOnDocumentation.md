This page aims to help you with working on the Python documentation.

### About the docs ###

The docs for new versions (2.6 and 3.0), which you'll be working on,
are written in reStructuredText (reST), which you may already know since
many other Python projects use it for documentation. If you haven't written
or seen reST before, it is very easy to learn. Python's documentation
adds a few elements to the basic reST elements, to help writing
readable and concise source.

An introduction to reST, as well as a complete description of Python's own
syntax elements, can be found in the ["Documenting Python" document](http://docs.python.org/dev/documenting/index.html) within the docs.

However, you most probably won't need to read through that document since
just looking into some documentation source is usually enough to get the
hang of it.

You can find daily builds of the 2.6 and 3.0 documentation at
http://docs.python.org/dev/ and http://docs.python.org/dev/3.0/, respectively.

### Getting the source ###

The documentation source is in Subversion at http://svn.python.org/projects/python/trunk/Doc for 2.6 and http://svn.python.org/projects/python/branches/py3k/Doc for 3.0. (If your task does not specifically refer to Python 3.0, you will be working with the 2.6 docs.)

You can of course also work in the `Doc/` subdirectory of a full checkout
of the Python source code.

Although you could edit the documentation without ever building it,
it is always nice to see the finished look of your work.
To build the documentation, that is, convert the source to HTML pages,
it should be enough to issue a `make html` inside the Doc directory if you're
using Linux. Under Windows, you need to check out some dependencies
and issue build commands yourself as described in the `Doc/README.txt` file.
Contact your mentor if you need help with this.


### Working on the docs ###

The docs are split into eleven sections. You will be most likely working in
the library reference, the C API reference or the "Using Python" document.
These can, unsurprisingly, be found in the "library", "c-api" and "using"
subdirectories of the `Doc` tree. Every page you see online at
http://docs.python.org/dev has a corresponding `.rst` file there.

When you have edited one or more of these files and want to submit your work,
it's best to create a patch file using the `svn diff` command. However, if
in doubt you can also submit whole files, and your mentor can sort out what
you changed. In any case, it's a good idea to update your checkout from time
to time using `svn update`.

Be sure to use `svn diff` to create a diff at the trunk/ level, e.g. the directory above Doc/.