# Attending: The Docs in!
Attending allows packages to self describe documentation through  the `__version__` and `__doc_url__` module attributes. 

Attending has two example projects, `foobar` and `fizbuz`. This guid will show how to consumes docs from these example 
projects. 

## The lay of the land
Attending stores docs in the `~/.attending` directory by default. The `Library` is configurable to store docs in other
locations as well. 

How to get the docs:
```python
>>> import attending
>>> import foobar
>>>
>>> from attending import Library
>>>
>>> library = Library()
>>>
>>> foobar in library
False
>>>
>>> library.fetch(boobar)
<attending.doc.Doc object at 0x100fb8d68>
>>> foobar in library
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
>>> from attending import Library
>>> library = Library()
>>> foobar in library
True
>>> library[foobar].diagnose()
```

How do I clean up old docs?
```python
>>> import attending
>>> import foobar
>>>
>>> from attending import Library
>>> library = Library()
>>> foobar in library
True
>>> del library[foobar] # or library.retire(foobar)
```