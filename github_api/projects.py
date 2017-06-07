import settings
from . import columns
from . import cards
from . import voting
from . import issues

from requests import HTTPError


def create_project(api, urn, title, body):
    path = "/repos/{urn}/projects".format(urn=urn)
    data = {
            "name": title,
            "body": body
    }
    resp = api("POST", path, json=data)
    return resp


# TODO: Implement more functionality and commands
