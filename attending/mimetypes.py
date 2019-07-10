from pathlib import Path
from zipfile import ZipFile
from urllib.parse import urlparse
from http.client import HTTPResponse


def extract_zip(doc_location: Path, file: Path):
    ZipFile(file).extractall(path=doc_location)
    file.unlink()


def get_mapping(mime_type):
    return {
        "application/pdf": "pdf",
        "application/zip": "zip",
        "text/html": "html",
        "text/plain": "txt"
    }.get(mime_type, "txt")


def get_extractor(file_extension):
    post_directives = {
        ".zip": extract_zip
    }
    if file_extension in post_directives:
        return post_directives[file_extension]


def get_filename(connection: HTTPResponse):
    content_disposition = connection.getheader('Content-Disposition')
    if content_disposition is not None:
        # !!!! I have yet to find a server that returns this for a file download. I have not been able to test this on
        # a proper response. I have made mock responses to test this.
        # Based off of https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition
        dispositions = content_disposition.strip().split("; ")
        for disposition in dispositions:
            if "=" in disposition:
                key, value = disposition.split("=")
                if key == 'filename':
                    return value
    # Will return '' if the path is '/path/to/something
    return Path(urlparse(connection.geturl()).path).name
