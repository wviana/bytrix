from .helpers import BitrixApiMixin, bitrix_method

class Translator:
    def __init__(self, language, userfields):
        self._translator = {}
        for uf in userfields:
            key = uf['FIELD_NAME']
            self._translator[key] = uf['EDIT_FORM_LABEL'][language]

    def decode(self, to_translate: dict):
        return self._translate(to_translate, dictionay=self._translator)

    def encode(self, to_encode: dict):
        encoder = {v: k for k, v in self._translator.items()}
        return self._translate(to_encode, dictionay=encoder)

    def _translate(self, to_translate, dictionay):
        translated = {}
        for old_key, value in to_translate.items():
            new_key = dictionay[old_key] if old_key in dictionay else old_key
            translated[new_key] = value
        return translated


class UserField(BitrixApiMixin):
    def __init__(self, url, package):
        super().__init__(url)
        self.package = f'{package}.userfield'

    @bitrix_method
    def add(self, method, **params):
        return self._call_method(method, params)

    @bitrix_method
    def list(self, method, **params):
        return self._call_method(method, params)

    @bitrix_method
    def update(self, method, **params):
        return self._call_method(method, params)

    @bitrix_method
    def delete(self, method, **params):
        return self._call_method(method, params)

    @bitrix_method
    def get(self, method, **params):
        return self._call_method(method, params)

    def translator(self, language):
        userfields = self.list().result
        userfields = map(lambda x: self.get(ID=x['ID']).result, userfields)
        return Translator(language, userfields)


class Contact(BitrixApiMixin):
    def __init__(self, url, package):
        super().__init__(url)
        self.package = f'{package}.contact'

    @bitrix_method
    def add(self, method, **params):
        return self._call_method(method, params)

    @bitrix_method
    def delete(self, method, **params):
        return self._call_method(method, params)

    @bitrix_method
    def fields(self, method, **params):
        return self._call_method(method, params)
