import logging
import time
from functools import wraps


# TODO: создать config, exceptions,
#  реализовать недостающие части,
#  затем удалить этот комментарий.
import my_config as config
from exceptions import RequestError

log = logging.getLogger(__name__)


def retry(
    max_attempts=5,
    timeout=3,
    factor_for_timeout=2,
    test_exceptions=(
        RequestError,
        ValueError,
        TimeoutError,
        ConnectionError,
        IOError,
        OSError,
    )
):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            attempt = 0
            current_timeout = timeout
            while attempt < max_attempts:
                attempt += 1
                print(f'Попытка {attempt} из {max_attempts}')
                try:
                    return func(*args, **kwargs)
                except test_exceptions as e:
                    logging.error(
                        "Ошибка при выполнении функции %s: %s. "
                        "Повторная попытка через %s секунд.",
                        func.__name__,
                        e,
                        current_timeout,
                    )
                    time.sleep(current_timeout)
                    current_timeout *= factor_for_timeout
            raise
        return wrapped
    return decorator


class CustomWeatherFetcher:
    def __init__(self):
        self._call_count = 0

    @retry
    def fetch_weather_or_raise_error(
        self,
        url: str,
        timeout: int,
        headers: dict[str, str] | None,
    ) -> dict[str, str | int]:
        """
        Функция, которая в зависимости от номера попытки
        либо выкидывает исключение, либо отрабатывает нормально.

        Такое поведение возможно только для демонстрации,
        перед новой демонстрацией необходимо сбрасывать счётчик.
        """
        self._call_count += 1

        log.debug(
                "Fetching data from %s with headers %s. Will take %ss",
                url, headers, timeout
            )
        time.sleep(timeout)
        if self._call_count == config.success_on_attempt:
            return {"temperature": 16, "rain-chance": 42, "sky": "clouds"}
        msg = f"failed to fetch data from {url} with headers {headers}"
        raise RequestError(msg)

    def reset_call_count(self):
        self._call_count = 0


weather_fetcher = CustomWeatherFetcher()


weather_fetcher.fetch_weather_or_raise_error(
    url=config.url,
    timeout=config.timeout,
    headers=config.headers,
)
