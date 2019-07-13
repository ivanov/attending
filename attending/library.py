import pkg_resources
from pathlib import Path
from functools import wraps

from .downloader import write_to_file
from .doc import Module

MONITOR_ERROR="""'{0}' needs both __doc_url__  and __version__ defined. It has
{0}.__doc_url__ = {1}
{0}.__version__ = {2}
"""

def can_monitor(module):
    return hasattr(module, "__doc_url__") and hasattr(module, "__version__")

def cannot_monitor(module):
    msg = MONITOR_ERROR.format(module.__name__,
            getattr(module, "__doc_url__", None),
            getattr(module, "__version__", None))

    return ValueError(msg)

def _requires_valid_module(f):
    @wraps(f)
    def __(library, module, *args, **kwargs):
        if not can_monitor(module):
            # TODO fallback here
            raise cannot_monitor(module)
        return f(library, module, *args, **kwargs)

    return __


class Library:
    def __init__(self, home=Path().home()):
        self.location = home / Path(".attending")
        if not self.location.exists():
            self.location.mkdir(parents=True)

        self.docs = {module.name: Module(self.location, module.name) for module in self.location.iterdir() if
                     module.is_dir()}

    @_requires_valid_module
    def fetch(self, module):
        if module not in self:
            self._add_project(module)
        return self[module]

    def _add_project(self, module):
        destination = self.location / module.__name__ / module.__version__
        if destination.exists():
            raise FileExistsError(f"{destination}")
        destination.mkdir(parents=True)
        write_to_file(self.location, module.__name__, module.__version__, module.__doc_url__)
        self.docs[module.__name__] = Module(self.location, module.__name__)

    @_requires_valid_module
    def __delitem__(self, module):
        doc = self[module]
        if not len(self.docs[module.__name__]):
            del self.docs[module.__name__]
        doc.retire()

    @_requires_valid_module
    def retire(self, module):
        del self[module]

    def __repr__(self):
        return str(self.docs)

    @_requires_valid_module
    def __contains__(self, module):
        return module.__name__ in self.docs and module in self.docs[module.__name__]

    @_requires_valid_module
    def __getitem__(self, module):
        return self.docs[module.__name__][module]


def fetch(module, version=None):
    """
    A convenience top-level function for fetching docs

    Parameters
    ----------
    module : string or module
        The module whose docs we want to pull up
    version: string, optional
        The version for `module`, will fall-back to latest, if not specified.
    """
    from types import ModuleType
    if isinstance(module, ModuleType):
        return fetch_via_module(module, version)
    else:
        return fetch_via_name(module, version)


def fetch_via_module(module, version=None):
    """
    Fetch the docs for a given imported module

    Parameters
    ----------
    module : module
        The module whose docs we want to pull up
    version: string, optional
        The version for `module`, will fall-back to current, if not specified.
    """
    lib = Library()
    mod_name = module.__name__

    if version is None:
        # First, let's try
        version = getattr(module, '__version__', None)

    if version is None:
        # Couldn't get __version__ from module
        # We can either:
        # 1. Assume it's the latest from PyPI
        # 2. Use pkg_resources to get it
        #
        # Let's do 2, for now
        version = pkg_resources.working_set.by_key[mod_name].version

    destination = lib.location / mod_name / version
    destination.mkdir(parents=True)
    if hasattr(module, "__doc_url__"):
        write_to_file(lib.location, mod_name, version, module.__doc_url__)
    else:
        #try our fall back
        raise NotImplementedError("TODO: fetch using fallback from PyPI")
    lib.docs[module.__name__] = Module(self.location, module.__name__)

def fetch_via_name(module, version=None):
    """
    Fetch the docs for a given imported module

    Parameters
    ----------
    module : string
        The module whose docs we want to pull up
    version: string, optional
        The version for `module`, will fall-back to current, if not specified.
    """
    lib = Library()
    #TODO: try to import the module and use fetch_via_module
    if version is None:
        if module in pkg_resources.working_set.by_key:
            version = pkg_resources.working_set.by_key[mod_name].version
        else:
            raise NotImplementedError("TODO: fetch version from PyPI")
    destination = lib.location / module / version
    destination.mkdir(parents=True)
    raise NotImplementedError("TODO: fetch using fallback from PyPI")
    lib.docs[module.__name__] = Module(self.location, module.__name__)
