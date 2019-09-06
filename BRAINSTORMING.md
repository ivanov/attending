

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

We should add version-dependent docstring?


# Maybe

1. Get the doc URL from PyPI API.

    In the top level object has the 'project_urls' key, and we could use the 'Documentation' attribute.

This is typically a link to ReadTheDocs, which would allow us download an html zip file

2. Download said zip file

3. Unzip the file in a cache directory 




# Other notes

The optional dependency installation via pip would require some PyPI integration and changes, probably via a PEP.

# needed for a release
- 3 things that need to work for someone to use it:
    1) get the docs
    2) view the docs
    3) "management" of docs
  
# TODO
- need some tests
## Need docs (ha)
- need documentation (what)
- how to

## Getting the docs
- iterate over modules (find all packages and get the docs for them)
- preferred method for getting docs for package:
    1. `__doc_url__`
    1. read the docs
    1. `pypi` project url for documentation
    
## Viewing the docs:
- constructing a url that is paste-able (browser open would be dope)
- strict: only open docs that you have on your drive
- permissive: shows docs that are not the exact version that you are using. 

## Management
- support `clean`

# Uses cases:
- airplane
- lockdown network (gov labs)
- expensive/inconsistent access
- privacy conscious individuals.
- easy/trust of docs, the packages describe where to get the docs so you don't succumb to out of date docs online