from enum import Enum
from typing import Any
from urllib.parse import urljoin

import requests
from requests import Response


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class HttpClient:
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key
        self._base_url = "https://api.usemotion.com"
        self._api_version = "v1"

    def call_api(
        self,
        method: HttpMethod,
        path: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Response:
        """
        Call the Motion API
        """
        path = path[1:] if path.startswith("/") else path
        url = urljoin(self._base_url, f"/{self._api_version}/{path}")
        return requests.request(
            method=method.value,
            url=url,
            json=data,
            params=params,
            headers={"X-API-Key": self._api_key},
        )
