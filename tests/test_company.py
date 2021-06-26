import pytest
import copy
import json

from bytrix import Bitrix
import responses
from responses import POST

BASE_URL = 'https://anyurl.com/rest/34/token'

@pytest.fixture(scope='module')
def result():
    return { 'ID': '2000',
             'COMPANY_TYPE': '1',
             'TITLE': 'FREIRE INFORMATICA LTDA',
             'LOGO': None,
             'LEAD_ID': None,
             'HAS_PHONE': 'Y',
             'HAS_EMAIL': 'Y',
             'HAS_IMOL': 'N',
             'ASSIGNED_BY_ID': '34',
             'CREATED_BY_ID': '5',
             'MODIFY_BY_ID': '34',
             'BANKING_DETAILS': '',
             'INDUSTRY': None,
             'REVENUE': None,
             'CURRENCY_ID': 'BRL',
             'EMPLOYEES': None,
             'COMMENTS': '',
             'DATE_CREATE': '2019-10-03T21:44:37+03:00',
             'DATE_MODIFY': '2021-02-19T23:54:58+03:00',
             'OPENED': 'N',
             'IS_MY_COMPANY': 'N',
             'ORIGINATOR_ID': None,
             'ORIGIN_ID': None,
             'ORIGIN_VERSION': None,
             'ADDRESS': None,
             'ADDRESS_2': None,
             'ADDRESS_CITY': None,
             'ADDRESS_POSTAL_CODE': None,
             'ADDRESS_REGION': None,
             'ADDRESS_PROVINCE': None,
             'ADDRESS_COUNTRY': None,
             'ADDRESS_COUNTRY_CODE': None,
             'ADDRESS_LOC_ADDR_ID': None,
             'ADDRESS_LEGAL': None,
             'REG_ADDRESS': None,
             'REG_ADDRESS_2': None,
             'REG_ADDRESS_CITY': None,
             'REG_ADDRESS_POSTAL_CODE': None,
             'REG_ADDRESS_REGION': None,
             'REG_ADDRESS_PROVINCE': None,
             'REG_ADDRESS_COUNTRY': None,
             'REG_ADDRESS_COUNTRY_CODE': None,
             'REG_ADDRESS_LOC_ADDR_ID': None,
             'UTM_SOURCE': None,
             'UTM_MEDIUM': None,
             'UTM_CAMPAIGN': None,
             'UTM_CONTENT': None,
             'UTM_TERM': None,
             'UF_CRM_1596650821': '1740',
             'UF_CRM_1569949442': '0',
             'UF_CRM_1576867119326': '',
             'UF_CRM_1576869455': '1408',
             'UF_CRM_1579696479': 'Desenvolvimento de programas de computador sob encomenda',
             'UF_CRM_1579696507': '6201501',
             'UF_CRM_1580130444': '1996-05-20T03:00:00+04:00',
             'UF_CRM_1582720948': '',
             'UF_CRM_1590000307': '0',
             'UF_CRM_1591716074': [],
             'UF_CRM_1591812916': '',
             'UF_CRM_1591812976': False,
             'UF_CRM_1595423751': '',
             'UF_CRM_1595942763': '1857',
             'UF_CRM_1602102291': '1801',
             'UF_CRM_1603799176': '',
             'UF_CRM_1603799192': '',
             'UF_CRM_1605298884': '0',
             'UF_CRM_1605298942': '',
             'UF_CRM_1606327836': '2019-05-12T01:34:17',
             'UF_CRM_1606327928': 'ATIVA',
             'UF_CRM_5CE562A484354': [],
             'UF_CRM_1545329060': [],
             'UF_CRM_1545329036': [],
             'UF_CRM_1536843927': 'PITANGUEIRAS',
             'UF_CRM_1552067985': [],
             'UF_CRM_1536843708': '914',
             'UF_CRM_1536843846': '42701370',
             'UF_CRM_1547041575': '01.210.562/0001-22',
             'UF_CRM_1536843934': 'Lauro de Freitas',
             'UF_CRM_1536843913': 'EDIF TRADE MEDICAL SALA 314',
             'UF_CRM_5CE562A5AC0DC': [],
             'UF_CRM_1545329471': [],
             'UF_CRM_1545329487': [],
             'UF_CRM_1562956657': '',
             'UF_CRM_1545328796': [],
             'UF_CRM_1546947404': [],
             'UF_CRM_1545329105': '',
             'UF_CRM_1536843954': '',
             'UF_CRM_1566394829': '934',
             'UF_CRM_1536843878': 'R ITAGI',
             'UF_CRM_1536843431': 'FREIRE INFORMATICA LTDA',
             'UF_CRM_1536843893': '599',
             'UF_CRM_1551115419250': '',
             'UF_CRM_1536845665': '1034',
             'UF_CRM_1537447683': '0',
             'UF_CRM_1536843406': 'FREIRE INFORMATICA LTDA',
             'UF_CRM_1545328767': '',
             'UF_CRM_1554299502': [],
             'UF_CRM_1548181638': '1056',
             'UF_CRM_5CE562A5E217D': [],
             'UF_CRM_1566440357': '',
             'UF_CRM_1550252177': '0',
             'PHONE': [{'ID': '50644',
               'VALUE_TYPE': 'WORK',
               'VALUE': '+557130135403',
               'TYPE_ID': 'PHONE'}],
             'EMAIL': [{'ID': '50646',
               'VALUE_TYPE': 'WORK',
               'VALUE': 'comercial@wrstudio.com.br',
               'TYPE_ID': 'EMAIL'}]}

@pytest.fixture(scope='module')
def results(result):
    result2 = copy.copy(result)
    result2['id'] = '2500'
    return [result, result2]

@responses.activate
def test_company_add(result):
    responses.add(POST, f'{BASE_URL}/crm.company.add',
                  json={'result': {}, 'time': '1234'})

    fields = copy.copy(result)
    del fields['ID']
    b = Bitrix(BASE_URL)
    b.crm.company.add(fields=fields)
    request_body =  responses.calls[0].request.body
    request_body = json.loads(request_body)
    assert request_body == { 'fields': fields }


@responses.activate
def test_company_delete():
    responses.add(POST, f'{BASE_URL}/crm.company.delete',
                  json={'result': {}, 'time': '1234'})

    b = Bitrix(BASE_URL)
    result = b.crm.company.delete(ID='1234')
    request_body =  responses.calls[0].request.body
    request_body = json.loads(request_body)
    assert request_body == { 'ID': '1234' }


@responses.activate
def test_company_get(result):
    responses.add(POST, url=f'{BASE_URL}/crm.company.get', json={'result': result, 'time': '1234'})

    b = Bitrix(BASE_URL)
    response = b.crm.company.get(ID='1234')
    request_body =  responses.calls[0].request.body
    request_body = json.loads(request_body)
    assert request_body == { 'ID': '1234' }
    assert response.result == result
    assert response.time == '1234'


@responses.activate
def test_company_list(results):
    responses.add(POST, f'{BASE_URL}/crm.company.list', json={'result': results, 'time': '1234',
                                                              'total': 2})

    b = Bitrix(BASE_URL)
    bitrix_response = b.crm.company.list()
    assert bitrix_response.total == 2
    assert bitrix_response.result == results
    assert bitrix_response[0] == results[0]
    assert bitrix_response[1] == results[1]
    assert bitrix_response.time == '1234'

@responses.activate
def test_company_list_with_next(results):
    responses.add(POST, f'{BASE_URL}/crm.company.list', json={'result': results, 'time': '1234',
                                                              'next': 2, 'total': 6})

    b = Bitrix(BASE_URL)
    bitrix_response = b.crm.company.list()
    assert bitrix_response.total == 6
    assert len(bitrix_response) == 6

    assert bitrix_response[0] == results[0]
    assert bitrix_response[1] == results[1]
    assert bitrix_response.result == results # Till here results are the same

    assert bitrix_response[2] == results[0]
    assert bitrix_response[3] == results[1]
    assert bitrix_response.result != results
    assert len(bitrix_response.result) == 4 # Now the results was extended by next page results

    assert bitrix_response[4] == results[0]
    assert bitrix_response[5] == results[1]
    assert bitrix_response.result != results
    assert len(bitrix_response.result) == 6 # Now the results was extended by next page results

    assert bitrix_response.time == '1234'
    assert bitrix_response.next == 2

@responses.activate
def test_company_list_inter(results):
    responses.add(POST, f'{BASE_URL}/crm.company.list', json={'result': results, 'time': '1234',
                                                              'next': 2, 'total': 6})

    b = Bitrix(BASE_URL)
    bitrix_response = b.crm.company.list()
    assert bitrix_response.total == 6

    response_inter = iter(bitrix_response)
    assert next(response_inter) == results[0]
    assert next(response_inter) == results[1]
    assert bitrix_response.result == results # Till here results are the same

    assert next(response_inter) == results[0]
    assert next(response_inter) == results[1]
    assert bitrix_response.result != results
    assert len(bitrix_response.result) == 4 # Now the results was extended by next page results

    assert next(response_inter) == results[0]
    assert next(response_inter) == results[1]
    assert bitrix_response.result != results
    assert len(bitrix_response.result) == 6 # Now the results was extended by next page results

    assert bitrix_response.time == '1234'
    assert bitrix_response.next == 2

