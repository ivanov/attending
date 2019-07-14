from attending.doc import _Cached, Doc, Module
from pathlib import Path
import os
import pytest
import shutil


@pytest.fixture
def module_fixture():
    base_path = Path(os.path.dirname(os.path.abspath(__file__))) / "test_dir"
    module_name = "test"
    yield base_path, module_name
    if base_path.exists():
        shutil.rmtree(base_path)


def test_object_cache():
    class Cached(metaclass=_Cached):
        def __init__(self, *args, **kwargs):
            pass

    assert id(Cached(None)) == id(Cached(None))

    assert id(Cached(data=[])) != id(Cached(data=[]))


def test_doc_removal(module_fixture):
    base_path, name = module_fixture
    version = "0.0.0"
    path = base_path / name / version
    path.mkdir(parents=True)
    assert path.exists()
    Doc(base_path, "test", "0.0.0").retire()
    assert base_path.exists()
    assert not path.exists()


def test_module_create_and_removal(module_fixture):
    base_path, name = module_fixture
    version = "0.0.0"
    module = Module(base_path, name)

    # assert no directory or doc
    assert not (base_path / name).exists()
    assert not module.exists(version)

    # create directory and doc
    version_path = base_path / name / version
    version_path.mkdir(parents=True)
    assert not module.exists(version)
    (version_path / "file1").touch()

    # assert doc exists
    assert module.exists(version)

    # remove doc and test
    module.remove()
    assert not (base_path / name).exists()


