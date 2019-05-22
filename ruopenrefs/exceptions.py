

class OpenRefsClientException(Exception):
    """Базовое исключение приложения."""


class ConnectionError(OpenRefsClientException):
    """Ошибка, связанная с невозможностью подключения к серверу поставщика данных."""


class ApiCallError(OpenRefsClientException):
    """Ошибка при обрашении к ручке API поставщика данных."""

    def __init__(self, message, status_code):
        super(ApiCallError, self).__init__(message)

        self.status_code = int(status_code)
