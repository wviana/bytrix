# Bytrix

What I think would be I pythonic Bitrix api wrapper, but may also be an overengineered Bitrix api wrapper.

### How I intent it to be.

```python
>>> bitrix = Bitrix('https://crmdevyandeh.bitrix24.com.br/rest/<user_id>/<user_token>')
>>> bitrix.crm.deal.list()
>>> l[0]
{'ID': '67841',
  'TITLE': 'MASTER ASSOCIACAO DE AVALIACAO DE CONFORMIDADE',
  'TYPE_ID': None,
  'STAGE_ID': 'C2:EXECUTING',
  'PROBABILITY': None,
  'CURRENCY_ID': 'BRL',
  'OPPORTUNITY': '0.00',
  'IS_MANUAL_OPPORTUNITY': 'N',
  'TAX_VALUE': '0.00',
  'LEAD_ID': None,
  'COMPANY_ID': '64248',
  'CONTACT_ID': '19892',
  'QUOTE_ID': None,
  'BEGINDATE': '2020-08-19T03:00:00+03:00',
  'CLOSEDATE': '',
  'ASSIGNED_BY_ID': '12',
  'CREATED_BY_ID': '34',
  'MODIFY_BY_ID': '34',
  'DATE_CREATE': '2020-08-19T22:56:54+03:00',
  'DATE_MODIFY': '2020-08-19T22:57:35+03:00',
  'OPENED': 'N',
  'CLOSED': 'N',
  'COMMENTS': None,
  'ADDITIONAL_INFO': None,
  'LOCATION_ID': None,
  'CATEGORY_ID': '2',
  'STAGE_SEMANTIC_ID': 'P',
  'IS_NEW': 'N',
  'IS_RECURRING': 'N',
  'IS_RETURN_CUSTOMER': 'N',
  'IS_REPEATED_APPROACH': 'N',
  'SOURCE_ID': None,
  'SOURCE_DESCRIPTION': None,
  'ORIGINATOR_ID': None,
  'ORIGIN_ID': None,
  'UTM_SOURCE': None,
  'UTM_MEDIUM': None,
  'UTM_CAMPAIGN': None,
  'UTM_CONTENT': None,
  'UTM_TERM': None,
}
```

### What do we have till now:

- crm.company.add
- crm.company.delete
- crm.company.fields
- crm.company.get
- crm.company.list
- crm.company.update
- crm.company.userfield.
- crm.company.userfield.list
- crm.company.userfield.update
- crm.company.userfield.delete
- crm.company.contact.add
- crm.company.contact.delete
- crm.company.contact.fields
- crm.deal.add
- crm.deal.delete
- crm.deal.fields
- crm.deal.get
- crm.deal.list
- crm.deal.update
- crm.deal.userfield.
- crm.deal.userfield.list
- crm.deal.userfield.update
- crm.deal.userfield.delete
- crm.deal.contact.add
- crm.deal.contact.delete
- crm.deal.contact.fields
