import codecs
from typing import Optional
from urllib.request import urlopen, Request


def data_uri_from_bytes(*, data: bytes, mime_type: str) -> str:
    """Return a base-64 data URI for bytes"""
    base64 = codecs.encode(data, "base64").decode("utf-8").replace("\n", "")
    return f"data:{mime_type};base64,{base64}"


def data_uri_from_url(url: str, *, mime_type: Optional[str] = None) -> str:
    """Return base-64 data URI for an image at a given URL.
    If not passed, the content type is determined from the response header
    if present, otherwise, jpeg is assumed.

    Raises:
        HTTPError: If the request fails
    """
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urlopen(request_site) as response:
        data = response.read()
    mime_type = mime_type or response.headers["Content-Type"] or "image/jpeg"
    assert mime_type is not None
    return data_uri_from_bytes(data=data, mime_type=mime_type)


def data_uri_from_file(path: str, *, mime_type: Optional[str] = None) -> str:
    """Return base-64 data URI for an image at a given file path.
    If not passed, the content type is determined from the file extension
    if present, otherwise, jpeg is assumed.
    """
    with open(path, "rb") as file:
        data = file.read()
    if mime_type is None:
        mime_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".svg": "image/svg+xml",
        }
        mime_type = mime_types.get(path[path.rfind(".") :].lower(), "image/svg+xml")
    assert mime_type is not None
    return data_uri_from_bytes(data=data, mime_type=mime_type)
