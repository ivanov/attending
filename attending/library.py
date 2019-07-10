from pathlib import Path
from functools import wraps

from .downloader import write_to_file
from .doc import Module


def can_monitor(module):
    return hasattr(module, "__doc_url__") and hasattr(module, "__version__")


def _requires_valid_module(f):
    @wraps(f)
    def __(library, module, *args, **kwargs):
        if not can_monitor(module):
            raise ValueError()  # TODO give better message
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
