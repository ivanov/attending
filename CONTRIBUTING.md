# Contributing

🏥 We're glad you want to help!

## Goals of the project

*  *Stay lightweight*: depend on as much of the standard library as possible; minimize external dependencies.
* *Self-serving*: `attending` should manage its own docs; add in a bootstrap option.
* *Share a cache*: Multiple environments can use the same files.

## Get the code

1. Fork this repository.
2. `git clone` the forked repository, and `cd` to it.
3. Get the development libraries with `pip install -r requirements-dev.txt`

## Testing your changes

Run `tox`.

[P.S. Read more about tox here](https://tox.readthedocs.io/en/latest/).

Or, you can run `python -m pytest`.

## Pull requests

Please add a description, and link to a ticket!

Tests will automatically run with Azure. They have to pass before Pull Requests will be accepted.
