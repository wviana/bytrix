from .crm import Crm

class Bitrix:
    def __init__(self, url):
        self.crm = Crm(url)

