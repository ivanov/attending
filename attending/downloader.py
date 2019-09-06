import urllib.request as request

from pathlib import Path

from .mimetypes import get_mapping, get_extractor, get_filename


def unpack_docs(working_directory: Path, file: Path):
    extractor = get_extractor(''.join(file.suffixes))
    if extractor:
        extractor(working_directory, file)


def write_to_file(base_path, module_name, version, url):
    ## Spoof headers to prevent 403: https://medium.com/@speedforcerun/python-crawler-http-error-403-forbidden-1623ae9ba0f
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    with request.urlopen(request.Request(url=url, headers=headers)) as connection:
        if connection.status == 200:
            if not get_filename(connection):
                file_extension = get_mapping(connection.getheader('Content-Type'))
                target = base_path / module_name / version / Path(f"{module_name}.{file_extension}")
            else:
                target = base_path / module_name / version / get_filename(connection)
            with open(target, "wb") as f:
                f.write(connection.read())
            unpack_docs(base_path / module_name / version, target)
        elif 300 <= connection.status and connection.status < 400:
            write_to_file(base_path, module_name, version, connection.getheader("Location"))
        else:
            raise LookupError(f"Failed to fetch docs at {url}, http status: {connection.status}")
