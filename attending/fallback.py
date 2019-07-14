"""The code in this module is used when a patient module does not have
`__doc_url__`, or that `__doc_url__` has failed to resolve.
"""

import json
from urllib.request import urlopen


# By default this'll be pypi.org, but can be package index mirror, or an
# internal package index.
API_BASE_URL = "https://pypi.org"
API_JSON_ENDPOINT = API_BASE_URL + "/pypi/{}/json"

class FetchError(RuntimeError):
    pass

def fetch_error(resp):
    return FetchError("Attending failed to fetch ", resp.url,
            ". Got HTTP error code ", resp.code)

def get_json(project):
    "Fetch the PyPI JSON data for a particular project"

    resp = urlopen(API_JSON_ENDPOINT.format(project))
    if resp.code != 200:
        raise fetch_error(resp)

    return json.load(resp)

def get_doc_url(project):
    data = get_json(project)
    return data["info"]["project_urls"].get("Documentation")


