

# Documenting via copilot

Examples for small everyday operations that can be performed via copilot.


## 01. Class without docstrings or comments

Task: Supply docstrings to a undocumented python class. 

Solution(s):
    - mark code (in markdown) -> open "Chat: Open Quick Chat" or via STRG + I --> prompt /doc --> accept / deny suggestion.


```py
from statics.GAMS5APIStatics import GAMS5APIStatics
from urllib3 import make_headers, request
import logging

class IntegrationService:
    auth: tuple | None = None
    host: str
    API_BASE_PATH: str

    def __init__(self, host: str, auth: tuple | None = None) -> None:
        self.host = host
        self.auth = auth
        self.API_BASE_PATH = f"{host}{GAMS5APIStatics.API_ROOT}"

    
    def integrate_all(self, project_abbr: str):
        url = f"{self.API_BASE_PATH}/integration/projects/{project_abbr}/objects"
        r = request("POST", url, headers= make_headers(basic_auth=f'{self.auth[0]}:{self.auth[1]}') if self.auth else None, redirect=False, timeout=10)

        if r.status >= 400:
            msg = f"Failed to integrate all objects for project {project_abbr}. POST request against {url}. Status: {r.status}. Response: {r.json()}"
            logging.error(msg)
            raise ConnectionError(msg)
        else:
            logging.info(f"Successfully integrated all digital objects for project {project_abbr}.")


    def disintegrate_all(self, project_abbr: str):
        url = f"{self.API_BASE_PATH}/integration/projects/{project_abbr}/objects"
        r = request("DELETE", url, headers= make_headers(basic_auth=f'{self.auth[0]}:{self.auth[1]}') if self.auth else None, redirect=False, timeout=10)

        if r.status >= 400:
            msg = f"Failed to disintegrate all objects for project {project_abbr}. POST request against {url}. Status: {r.status}."
            logging.error(msg)
            logging.error(f"Response: {r.json()}")
            raise ConnectionError(msg)
        else:
            logging.info(f"Successfully disintegrated all digital objects for project {project_abbr}.")

```