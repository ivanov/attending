from pathlib import Path
import webbrowser
import shutil
import os


class _Cached(type):

    def __init__(cls, name, bases, dct):
        setattr(cls, "_instance_cache", {})
        super().__init__(name, bases, dct)

    def __call__(cls, *args, **kwargs):
        if not len(kwargs):
            if args not in getattr(cls, "_instance_cache"):
                getattr(cls, "_instance_cache")[args] = super().__call__(*args, **kwargs)
            return getattr(cls, "_instance_cache")[args]
        return super().__call__(*args, **kwargs)


class Doc(metaclass=_Cached):

    def __init__(self, base_path: Path, name: str, version: str):
        self.base_path = base_path
        self.name = name
        self.version = version

    def diagnose(self):
        webbrowser.open("file://" +str(self.base_path / self.name / self.version))

    def retire(self):
        shutil.rmtree(self.base_path / self.name / self.version)


class Module(metaclass=_Cached):

    def __init__(self, base_path: Path, name: str):
        self.base_path = base_path
        self.name = name

    def versions(self):
        return [Doc(self.base_path, self.name, version.name) for version in (self.base_path / self.name).iterdir() if
                version.is_dir()]

    def __len__(self):
        return len(self.versions())

    def _retire(self):
        shutil.rmtree(self.base_path / self.name)

    def __delitem__(self, module):
        doc = self[module]
        doc.retire()

    def __contains__(self, module):
        candidate = self.base_path / self.name / module.__version__
        return candidate.is_dir() and len(os.listdir(str(candidate)))

    def __getitem__(self, module):
        if module in self:
            return Doc(self.base_path, self.name, module.__version__)
        raise KeyError()  # TODO give this a message

    def __str__(self):
        return self.name
