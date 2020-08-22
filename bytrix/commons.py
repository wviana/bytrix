from .helpers import BitrixApiMixin, bitrix_method

class UserField(BitrixApiMixin):
    def __init__(self, url, package):
        super().__init__(url)
        self.package = f'{package}.userfield'

    @bitrix_method
    def list(self, method, **params):
        return self.call_method(method, params)

    @bitrix_method
    def update(self, method, **params):
        return self.call_method(method, params)

    @bitrix_method
    def delete(self, method, **params):
        return self.call_method(method, params)

class Contact(BitrixApiMixin):
    def __init(self, url, package):
        super().__init__(url)
        self.package = f'{package}.contact'

    @bitrix_method
    def add(self, method, **params):
        return self.call_method(method, params)

    @bitrix_method
    def delete(self, method, **params):
        return self.call_method(method, params)

    @bitrix_method
    def fields(self, method, **params):
        return self.call_method(method, params)
