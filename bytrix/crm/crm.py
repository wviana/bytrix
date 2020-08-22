from .deal import Deal
from .company import Company

class Crm:
    def __init__(self, url):
        self.deal = Deal(url)
        self.company = Company(url)
