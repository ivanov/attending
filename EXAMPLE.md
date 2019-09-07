# Attending: The Docs in!
Attending allows packages to self describe documentation through  the `__version__` and `__doc_url__` module attributes. 

Attending has two example projects, `foobar` and `fizbuz`. This guide will show how to consume docs from these example
projects. 

## The lay of the land
Attending stores docs in the `~/.attending` directory by default. The `Library` is configurable to store docs in other
locations as well. 

How to get the docs:
```python
>>> import attending
>>> import foobar
>>> attending.contains(foobar)
False
>>> attending.fetch(foobar)
<attending.doc.Doc object at 0x104656fd0>
>>> attending.attending_doc(foobar)
<attending.doc.Doc object at 0x104656fd0>
>>> attending.contains(foobar)
True
```

What do we have? 
```bash
John@Puma-concolor ~ $ tree .attending/
.attending/
└── foobar
    └── 1.0.0
        └── ipython.pdf

2 directories, 1 file
```

How do I read the docs?
```python
>>> import attending
>>> import foobar
>>>
>>> attending.contains(foobar)
True
>>> attending.attending_doc(foobar).diagnose()
```

How do I clean up old docs?
```python
>>> import attending
>>> import foobar
>>> attending.contains(foobar)
True
>>> attending.attending_doc(foobar).retire()
>>> attending.attending_doc(foobar)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/John/attending/attending/library.py", line 88, in attending_doc
    return lib.get_edition(module.__name__, version)
  File "/Users/John/attending/attending/library.py", line 79, in get_edition
    raise KeyError
KeyError
```
