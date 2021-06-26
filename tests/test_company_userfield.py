from bytrix import Bitrix
import pytest
import responses
import copy
import json
from responses import POST

BASE_URL = 'https://anyurl.com/rest/34/token'

@pytest.fixture
def results():
    return [{ 'ID': '1354',
              'ENTITY_ID': 'CRM_COMPANY',
              'FIELD_NAME': 'UF_CRM_1596650821',
              'USER_TYPE_ID': 'enumeration',
              'XML_ID': None,
              'SORT': '2',
              'MULTIPLE': 'N',
              'MANDATORY': 'Y',
              'SHOW_FILTER': 'N',
              'SHOW_IN_LIST': 'N',
              'EDIT_IN_LIST': 'Y',
              'IS_SEARCHABLE': 'N',
              'SETTINGS': {'DISPLAY': 'LIST',
               'LIST_HEIGHT': 1,
               'CAPTION_NO_VALUE': '',
               'SHOW_NO_VALUE': 'Y'},
              'LIST': [{'ID': '1738', 'SORT': '100', 'VALUE': 'B2B', 'DEF': 'N'},
               {'ID': '1740', 'SORT': '200', 'VALUE': 'BITRIX', 'DEF': 'N'},
               {'ID': '1742', 'SORT': '300', 'VALUE': 'Portal ERP', 'DEF': 'N'},
               {'ID': '1744', 'SORT': '400', 'VALUE': 'Cadastro Web', 'DEF': 'N'},
               {'ID': '1746', 'SORT': '500', 'VALUE': 'Portal Institucional', 'DEF': 'N'},
               {'ID': '1773', 'SORT': '600', 'VALUE': 'Carga Backoffice', 'DEF': 'N'}]},
             {'ID': '500',
              'ENTITY_ID': 'CRM_COMPANY',
              'FIELD_NAME': 'UF_CRM_1569949442',
              'USER_TYPE_ID': 'boolean',
              'XML_ID': None,
              'SORT': '100',
              'MULTIPLE': 'N',
              'MANDATORY': 'N',
              'SHOW_FILTER': 'N',
              'SHOW_IN_LIST': 'N',
              'EDIT_IN_LIST': 'Y',
              'IS_SEARCHABLE': 'N',
              'SETTINGS': {'DEFAULT_VALUE': 0,
               'DISPLAY': 'CHECKBOX',
               'LABEL': [None, None],
               'LABEL_CHECKBOX': 'Erro'}}]

@pytest.fixture
def result_id_1354():
    return {  'ID': '1354',
              'ENTITY_ID': 'CRM_COMPANY',
              'FIELD_NAME': 'UF_CRM_1596650821',
              'USER_TYPE_ID': 'enumeration',
              'XML_ID': None,
              'SORT': '2',
              'MULTIPLE': 'N',
              'MANDATORY': 'Y',
              'SHOW_FILTER': 'N',
              'SHOW_IN_LIST': 'N',
              'EDIT_IN_LIST': 'Y',
              'IS_SEARCHABLE': 'N',
              'SETTINGS': {'DISPLAY': 'LIST',
               'LIST_HEIGHT': 1,
               'CAPTION_NO_VALUE': '',
               'SHOW_NO_VALUE': 'Y'},
              'EDIT_FORM_LABEL': {'br': 'Origem da Empresa',
               'de': 'Origem da Empresa',
               'en': 'Origem da Empresa',
               'fr': 'Origem da Empresa',
               'hi': 'Origem da Empresa',
               'id': 'Origem da Empresa',
               'it': 'Origem da Empresa',
               'ja': 'Origem da Empresa',
               'la': 'Origem da Empresa',
               'ms': 'Origem da Empresa',
               'pl': 'Origem da Empresa',
               'ru': 'Origem da Empresa',
               'sc': 'Origem da Empresa',
               'tc': 'Origem da Empresa',
               'th': 'Origem da Empresa',
               'tr': 'Origem da Empresa',
               'ua': 'Origem da Empresa',
               'vn': 'Origem da Empresa'},
              'LIST_COLUMN_LABEL': {'br': 'Origem da Empresa',
               'de': 'Origem da Empresa',
               'en': 'Origem da Empresa',
               'fr': 'Origem da Empresa',
               'hi': 'Origem da Empresa',
               'id': 'Origem da Empresa',
               'it': 'Origem da Empresa',
               'ja': 'Origem da Empresa',
               'la': 'Origem da Empresa',
               'ms': 'Origem da Empresa',
               'pl': 'Origem da Empresa',
               'ru': 'Origem da Empresa',
               'sc': 'Origem da Empresa',
               'tc': 'Origem da Empresa',
               'th': 'Origem da Empresa',
               'tr': 'Origem da Empresa',
               'ua': 'Origem da Empresa',
               'vn': 'Origem da Empresa'},
              'LIST_FILTER_LABEL': {'br': 'Origem da Empresa',
               'de': 'Origem da Empresa',
               'en': 'Origem da Empresa',
               'fr': 'Origem da Empresa',
               'hi': 'Origem da Empresa',
               'id': 'Origem da Empresa',
               'it': 'Origem da Empresa',
               'ja': 'Origem da Empresa',
               'la': 'Origem da Empresa',
               'ms': 'Origem da Empresa',
               'pl': 'Origem da Empresa',
               'ru': 'Origem da Empresa',
               'sc': 'Origem da Empresa',
               'tc': 'Origem da Empresa',
               'th': 'Origem da Empresa',
               'tr': 'Origem da Empresa',
               'ua': 'Origem da Empresa',
               'vn': 'Origem da Empresa'},
              'ERROR_MESSAGE': {'br': None,
               'de': None,
               'en': None,
               'fr': None,
               'hi': None,
               'id': None,
               'it': None,
               'ja': None,
               'la': None,
               'ms': None,
               'pl': None,
               'ru': None,
               'sc': None,
               'tc': None,
               'th': None,
               'tr': None,
               'ua': None,
               'vn': None},
              'HELP_MESSAGE': {'br': None,
               'de': None,
               'en': None,
               'fr': None,
               'hi': None,
               'id': None,
               'it': None,
               'ja': None,
               'la': None,
               'ms': None,
               'pl': None,
               'ru': None,
               'sc': None,
               'tc': None,
               'th': None,
               'tr': None,
               'ua': None,
               'vn': None},
              'LIST': [{'ID': '1738', 'SORT': '100', 'VALUE': 'B2B', 'DEF': 'N'},
               {'ID': '1740', 'SORT': '200', 'VALUE': 'BITRIX', 'DEF': 'N'},
               {'ID': '1742', 'SORT': '300', 'VALUE': 'Portal ERP', 'DEF': 'N'},
               {'ID': '1744', 'SORT': '400', 'VALUE': 'Cadastro Web', 'DEF': 'N'},
               {'ID': '1746', 'SORT': '500', 'VALUE': 'Portal Institucional', 'DEF': 'N'},
               {'ID': '1773', 'SORT': '600', 'VALUE': 'Carga Backoffice', 'DEF': 'N'}]}


@responses.activate
def test_company_userfield_add(result_id_1354):
    responses.add(POST, f'{BASE_URL}/crm.company.userfield.add',
                  json={'result': {'ID': '1234'}, 'time': '1234'})

    fields = copy.copy(result_id_1354)
    del fields['ID']
    b = Bitrix(BASE_URL)
    b.crm.company.userfield.add(fields=fields)
    request_body =  responses.calls[0].request.body
    request_body = json.loads(request_body)
    assert request_body == { 'fields': fields }


@responses.activate
def test_company_userfield_get(result_id_1354):
    responses.add(POST, f'{BASE_URL}/crm.company.userfield.get',
                  json={'result': result_id_1354, 'time': '1234', 'total': 2})

    b = Bitrix(BASE_URL)
    l = b.crm.company.userfield.get(ID='1354')
    assert l.result == result_id_1354
    assert responses.calls[0].request.body == b'{"ID": "1354"}'


@responses.activate
def test_company_userfield_list(results):
    responses.add(POST, f'{BASE_URL}/crm.company.userfield.list',
                  json={'result': results, 'time': '1234', 'total': 2})

    b = Bitrix(BASE_URL)
    l = b.crm.company.userfield.list()
    assert l.result == results
    assert responses.calls[0].request.body == b'{}'

@responses.activate
def test_company_userfield_translator_decode(results, result_id_1354):
    single_results = results[0:1]

    responses.add(POST, f'{BASE_URL}/crm.company.userfield.list',
                  json={'result': single_results, 'time': '1234', 'total': 2})

    responses.add(POST, f'{BASE_URL}/crm.company.userfield.get',
                  json={'result': result_id_1354, 'time': '1234', 'total': 2})

    b = Bitrix(BASE_URL)
    translator = b.crm.company.userfield.translator('br')

    to_translate = {'UF_CRM_1596650821': 'Bitrix', 'Campo Normal': 'Teste'}

    decoded = translator.decode(to_translate)
    assert decoded == {'Origem da Empresa': 'Bitrix', 'Campo Normal': 'Teste'}


@responses.activate
def test_company_userfield_translator_encode(results, result_id_1354):
    single_results = results[0:1]

    responses.add(POST, f'{BASE_URL}/crm.company.userfield.list',
                  json={'result': single_results, 'time': '1234', 'total': 2})

    responses.add(POST, f'{BASE_URL}/crm.company.userfield.get',
                  json={'result': result_id_1354, 'time': '1234', 'total': 2})

    b = Bitrix(BASE_URL)
    translator = b.crm.company.userfield.translator('br')

    to_encode = {'Origem da Empresa': 'Bitrix', 'Campo Normal': 'Teste'}

    encoded = translator.encode(to_encode)
    assert encoded == {'UF_CRM_1596650821': 'Bitrix', 'Campo Normal': 'Teste'}



