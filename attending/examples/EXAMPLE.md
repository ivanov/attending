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
>>> from attending.examples import abc
>>> attending.contains(abc)
False
>>> attending.fetch(abc)
<attending.doc.Doc object at 0x104656fd0>
>>> attending.attending_doc(abc)
<attending.doc.Doc object at 0x104656fd0>
>>> attending.contains(abc)
True
```

What do we have? 
```bash
John@Puma-concolor ~ $ tree .attending/
└── attending.examples.abc
    └── 1.2.3
        └── abc.html

1 directories, 1 file
```

How do I read the docs?
```python
>>> import attending
>>> from attending.examples import abc
>>>
>>> attending.contains(abc)
True
>>> attending.attending_doc(abc).diagnose()
```

How do I clean up old docs?
```python
>>> import attending
>>> from attending.examples import abc
>>> attending.contains(abc)
True
>>> attending.attending_doc(abc).retire()
>>> attending.attending_doc(abc)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/John/attending/attending/library.py", line 88, in attending_doc
    return lib.get_edition(module.__name__, version)
  File "/Users/John/attending/attending/library.py", line 79, in get_edition
    raise KeyError
KeyError
```
