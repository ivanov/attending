import csv
from pathlib import Path
import os


def load_index(file: Path):
    project_index = {}
    assert file.is_file()
    with open(str(file), 'r') as index:
        index_reader = csv.reader(index)
        for row in index_reader:
            project_index[row[0]] = row[2]
            project_index[row[1]] = row[2]
    return project_index


def load_attending_index():
    location = Path(os.path.dirname(os.path.abspath(__file__))) / "index.csv"
    return load_index(location)
