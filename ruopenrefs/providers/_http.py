import logging

import requests

from .. import VERSION_STR
from ..exceptions import ConnectionError, ApiCallError

LOG = logging.getLogger(__name__)


class OpenRefsResponse:
    """Обёртка над ответом requests."""

    def __init__(self, response: requests.Response):
        """
        :param response:
        """
        self._response = response


class HttpConnector:
    """Реализует обращение к ресурсам по средствам http(s)."""

    def __init__(self, *, timeout=None):
        self._timeout = timeout or 10

    def _request(self, url: str, method: str = 'get', **kwargs):
        timeout = self._timeout

        method = getattr(requests, method)

        LOG.debug('URL: %s', url)

        def do_request():

            request_kwargs = {
                'headers': {
                    'User-agent': 'ruopenrefs/%s' % VERSION_STR,
                },
                'timeout': timeout,
                'verify': False,
            }
            request_kwargs.update(kwargs)

            try:
                response = method(url, **request_kwargs)  # type: requests.Response

            except requests.ReadTimeout:
                raise ConnectionError('Request timed out.') from None

            except requests.ConnectionError:
                raise ConnectionError('Unable to connect to %s.' % url)

            try:
                response.raise_for_status()

            except requests.HTTPError:
                msg = response.content
                status_code = response.status_code
                LOG.debug('API call error, code [%s]:\n%s', status_code, msg)
                raise ApiCallError(msg, status_code)

            return response

        return OpenRefsResponse(response=do_request())

    request = _request
