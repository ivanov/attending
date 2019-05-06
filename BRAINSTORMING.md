

# Supported installation modes

Via installation optional dependency

```
$  pip install package_name[docs]
```


Via a discover mechanism that looks at all importable modules, checks their `__doc_url__`

```
>>> import attending
>>> attending.get_the_docs()
```


As a runnable package that allows you to start viewing the docs

```
$ python -m attending
```


# Philosophical pillar

Stay light weight: depend on as much of the standard library as possible,
minimal external dependencies.


Version-dependent docstring


# Maybe

1. Get the doc URL from PyPI API.

    In the top level object has the 'project_urls' key, and we could use the 'Documentation' attribute.

This is typically a link to ReadTheDocs, which would allow us download an html zip file

2. Download said zip file

3. Unzip the file in a cache directory 




# Other notes

The optional dependency installation via pip would require some PyPI integration and changes, probably via a PEP.
