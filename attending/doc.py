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
        webbrowser.open("file://" + str(self.base_path / self.name / self.version))

    def retire(self):
        shutil.rmtree(self.base_path / self.name / self.version)


class Module(metaclass=_Cached):

    def __init__(self, base_path: Path, name: str):
        self.base_path = base_path
        self.name = name

    def versions(self):
        return [Doc(self.base_path, self.name, version.name) for version in (self.base_path / self.name).iterdir() if
                version.is_dir()]

    def exists(self, version):
        candidate = self.base_path / self.name / version
        return candidate.is_dir() and os.listdir(candidate)

    def version(self, version):
        if self.exists(version):
            return Doc(self.base_path, self.name, version)
        raise KeyError

    def __len__(self):
        return len(self.versions())

    def remove(self):
        shutil.rmtree(self.base_path / self.name)

    def __delitem__(self, version):
        doc = self[version]
        doc.retire()

    def __contains__(self, version):
        return self.exists(version)

    def __getitem__(self, version):
        return self.version(version)

    def __str__(self):
        return self.name
