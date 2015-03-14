## Example code rules ##

Example code in the library documentation should follow these guidelines:

  * If it is a short snippet, the point it tries to make or the caveat it tries to highlight should be instantly clear.  If you need to include return values of function/method calls, writte it in the style of a Python interactive console session, see below.
  * If it is a longer piece of example code, it should contain all necessary imports and setup code, so that it can be copied into a file and run as a script without any further editing.
  * Do not hesitate to use comments in longer examples.
  * It must follow the [PEP 8](http://www.python.org/dev/peps/pep-0008) style rules.
  * It must, of course, be correct. If the snippet is not a complete Python script (e.g. it lacks imports etc.), write a script to make sure it runs correctly in an appropriate environment.

> Remember that you can use doctest if your snippet is written in console session style.

## Examples ##

Interactive console session style example:

```
   >>> it = iter('abc')
   >>> it
   <iterator object at 0x00A1DB50>
   >>> it.next()
   'a'
   >>> it.next()
   'b'
```

Do NOT write it in this way:
```
   it = iter('abc')
   it  # gives <iterator object at 0x00A1DB50>
   it.next() # gives 'a'
   it.next() # gives 'b'
```