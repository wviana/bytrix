import inspect
import reprlib
from collections import namedtuple
from typing import Dict, Any

import requests


def bitrix_method(func):
    def inner(self, *args, **kwarg):
        package = self.package if hasattr(self, 'package') else inspect.getmodule(func).__package__
        package = package.replace('bytrix.', '')
        method = '.'.join([package, func.__name__])
        return func(self, *args, method, **kwarg)

    return inner


class BitrixResponse:
    def __init__(self, raw_response, next_request):
        self._repr = f'BitrixResponse({reprlib.repr(raw_response)})'
        self.result = raw_response['result']
        self.time = raw_response['time']
        self._raw_response = raw_response

        if next_request:
            self._next_request = next_request

        if 'next' in raw_response:
            self.next = raw_response['next']

        if 'total' in raw_response:
            self.total = raw_response['total']

    def __repr__(self):
        return self._repr

    def __len__(self):
        return self.total or len(self.result)

    def __getitem__(self, key):
        stop = key.stop if isinstance(key, slice) else key
        while self.total > stop >= len(self.result):
            self._fetch_next_page()

        return self.result[key]

    def __iter__(self):
        yield from iter(self.result)

        if self._next_request:
            while len(self.result) < self.total:
                begin = len(self.result)
                self._fetch_next_page()
                yield from iter(self.result[begin:])

    def _fetch_next_page(self):
        next_items = self._next_request(self.next)
        self.result.extend(next_items.result)
        self.next = next_items.next


class BitrixApiMixin:
    def __init__(self, url):
        self._url = url

    def _call_method(self, method: str, params: Dict[Any, Any]) -> BitrixResponse:
        request_url = '/'.join([self._url, method])
        response = requests.post(request_url, json=params)
        response.raise_for_status()
        body = response.json()

        if 'next' in body:
            def next_request(start):
                next_params = {**params, 'start':start}
                return self._call_method(method, next_params)
        else:
            next_request = None

        return BitrixResponse(body, next_request)
