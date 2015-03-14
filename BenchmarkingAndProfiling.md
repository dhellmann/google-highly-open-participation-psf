# Benchmarking and Profiling #

There are a few tasks that require you to either benchmark Python (by measuring its speed) or profile some Python source code (to figure out where code is taking too long).

## Benchmarking Python ##

You should use pybench, under `Tools/pybench/README` in the Python source tree, for information on how to benchmark the Python distribution.

## Profiling ##

Profiling seeks to measure the amount of time spent in various parts of the code.
Here's [a high-level overview](http://ivory.idyll.org/articles/advanced-swc/#measuring-and-increasing-performance) of some of the tools available for profiling.  We suggest starting with [cProfile](http://docs.python.org/lib/module-profile.html),
which is the officially supported Python profiler.

We know the profiling documentation is confusing; please go ahead and ask us questions if you run into trouble!