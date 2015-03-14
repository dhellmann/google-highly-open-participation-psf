# Introduction #

These are notes from task suggestions which came in while we were planning the contest.  This information is here for historical context only.  The authoritative source of tasks for contestants is the Open issues list.  These notes may diverge from the final tasks as they were written up.  When in doubt, follow the instructions in the task and ask questions on the mailing list.


## rosettacode.org ##

"Simple programming problems" solved in multiple prog languages

Michael Mol suggests:

```
> -> Rosetta Code, where simple programming problems
> -> are solved in as many as 79 programming languages.  While most of the
> -> tasks (a shade under 80%) already have Python solutions, there are a
> -> few that don't.  Even so, the tasks that already have Python solutions
> -> could be instructional.
Here's a list of all the pages that (as I write this) don't have
Python examples.  Currently, there are 25.  I don't know Python, but
here are my best guesses regarding difficulty:

Trivial
http://rosettacode.org/rosettacode/w/index.php?title=Bitwise_operations
http://rosettacode.org/rosettacode/w/index.php?title=Data_Representation_-_Controlling_Fields_in_a_Structure
http://rosettacode.org/rosettacode/w/index.php?title=File_Modification_Time
http://rosettacode.org/rosettacode/w/index.php?title=File_Rename
http://rosettacode.org/rosettacode/w/index.php?title=File_Size
http://rosettacode.org/rosettacode/w/index.php?title=Logical_operations

Easy
http://rosettacode.org/rosettacode/w/index.php?title=Binary_search
http://rosettacode.org/rosettacode/w/index.php?title=Doubly-Linked_List_%28element_insertion%29
http://rosettacode.org/rosettacode/w/index.php?title=Doubly-Linked_List_%28element%29
http://rosettacode.org/rosettacode/w/index.php?title=Flow_Control_Structures
http://rosettacode.org/rosettacode/w/index.php?title=MD5
http://rosettacode.org/rosettacode/w/index.php?title=Prime_numbers

Moderate
http://rosettacode.org/rosettacode/w/index.php?title=Object_Serialization
http://rosettacode.org/rosettacode/w/index.php?title=OpenGL
http://rosettacode.org/rosettacode/w/index.php?title=Parametric_Polymorphism
http://rosettacode.org/rosettacode/w/index.php?title=SQL-Based_Authentication

Hard
http://rosettacode.org/rosettacode/w/index.php?title=Distributed_program
http://rosettacode.org/rosettacode/w/index.php?title=Determine_if_Only_One_Instance_is_Running
http://rosettacode.org/rosettacode/w/index.php?title=Quine

Unknown
http://rosettacode.org/rosettacode/w/index.php?title=Data_Representation_-_Getting_the_Size
http://rosettacode.org/rosettacode/w/index.php?title=Data_Representation_-_Specifying_Minimum_Size
http://rosettacode.org/rosettacode/w/index.php?title=Defining_Primitive_Data_Types
http://rosettacode.org/rosettacode/w/index.php?title=HTTPS_request_with_authentication
http://rosettacode.org/rosettacode/w/index.php?title=Insertion_sort
http://rosettacode.org/rosettacode/w/index.php?title=Pattern_Matching
http://rosettacode.org/rosettacode/w/index.php?title=XML_and_XPath


```

## Port small and useful 3rd party packages to Py3K ##

Author: Titus Brown

We would need to pick a few packages that are simple, have good unit tests, and yet are useful.  simplejson is one nominee... we could solicit input from the community pretty easily on this, without saying why we're looking for such packages.

## Rewrite tests for the standard library that do not use unittest or doctest. ##

Author: bcannon

Python's standard library has been around for a long time.  It has grown and changed year after year.  But that doesn't mean someone has taken the time to rewrite and update all of the tests for everything in the standard library.

Some tests still exist that do not use the unittest or doctest modules.  Those two modules are the preferred way for tests to be written.  If would be helpful in terms of ease of maintenance and readability to update any and all tests to use either unittest or doctest.

### Tests that need updating ###

This list is in no way exhaustive!

  * test\_struct


## Sync docstrings with docs ##

Author: Georg Brandl

Sync up docstrings and written documentation (make sure the docstring contain all essential information from the docs, and the docs contain everything the docstring does) in library code

## Add code examples to the docs ##

Author: Georg Brandl

Add code examples to library documentation that's missing them. Should we select specific ones, or just say "pick $NUMBER"?

Comment by ti...@idyll.org, Nov 16, 2007

Some notes from comments on my blog solicitation, ivory.idyll.org/blog/nov-07/hidden-gems-in-stdlib.html

re (examples, esp groups & subs) xmrpclib (server/client example) datetime (examples?) ConfigParser? (exhaustive examples!) wsgiref (examples, more discussion)

unittest (examples) UserDict? (examples) logging (examples, docs rewrite) csv (examples pprint (indent, depth, width) SocketServer? itertools (doctests)

DB API examples for mysql, postgres, sqlite

struct urllib2 transfer from hidden guide??

glob?

traceback examples

bisect examples

operator (docs) mmap (docs)

xml.etree.ElementTree? - transfer docs from effbot

compiler docs (kumar) AST => Abstract Syntax Tree

http://docs.python.org/dev/library/undoc.html

> - multimedia stuff; videoreader - applesingle?

## Document undocumented C API functions ##

Author: Georg Brandl

There are quite a few C APIs undocumented, e.g. the `PySys_*` set of functions. Documenting them isn't too hard, you should understand C and a bit of the Python C API.

## have students prepare short tutorials like those at ShowMeDo.com ##

### Pros ###

  * The [YouTube](http://www.youtube.com) generation thinks user-generated video is cool.
  * People at all skills levels could take part (i.e., lower cost of entry than hacking the core library).
  * This project would attract people with skills in areas other than pure hacking (i.e., we wouldn't be preaching to the converted).
  * Students would be able to understand/appreciate/review other students' work.
  * People could contribute by doing an ABC-language version of someone else's XYZ-language contribution.
  * A "best of" show would make a great [PyCon](http://www.pycon.org/) event.

### Cons ###

  * Doesn't add new capabilities to Python, the standard library, or related tools.


Comment by ti...@idyll.org, Nov 19, 2007

> - checking out, configuring, and compiling Python26/30 on linux, win,

> or mac os x;

> - running the regression tests with code coverage - running pystone benchmarks

> - building a simple calculator module and writing unit tests for it

## Log file reporting and visualization ##

Author: Grig Gheorghiu

The goal of this mini-project is to replicate and possibly enhance the software available at <http://www.fudgie.org/>. Since this project is too big for one task, I propose splitting it in several tasklets:

  * Write a program that is able to retrieve log files from multiple servers via ssh
  * Choose a log file format (Apache Combined, Rails, IIS, Postfix/spamd/clamd, Nginx, Squid, PostgreSQL, PureFTPD, MySQL, TShark, qmail/vmpop3d) and write a parser for it, then save the relevant log data in a database of your choice (MySQL, PostgreSQL, SQLite)
  * Assuming you have all the relevant log data in a database, write a tool that shows reports/stats on that data
  * Assuming you have all the relevant log data in a database, write a tool that uses a graphics library to show the data in various ways
  * Write a visualization program using OpenGL that operates on a live log by parsing out its relevant data, then showing it in real time (no database)

## Miscellaneous notes from Titus ##

poorly organized ;)

[Reinteract](http://blog.fishsoup.net/2007/11/10/reinteract-better-interactive-python/) seems ripe for contribution/screencast.

Modules to focus on: [http://www.algorithm.co.il/blogs/index.php/programming/python/python-module-usage-statistics/
> Python module usage stats]

[NLTK](http://nltk.sf.net) has a great list of TODOs; might be a bit much for high school and younger, though.

pygame, pgu, and [svn://www.imitationpickles.org/pug/trunk pug] could all use help & they're pretty sexy.

Comments on these two posts can be mined for specific target modules for better docs, examples, tests:
http://ivory.idyll.org/blog/nov-07/hidden-gems-in-stdlib.html and
http://ivory.idyll.org/blog/nov-07/new-to-python-projects.html