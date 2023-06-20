import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formatted_data, encode_bill_info

def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert  len(data) == 2

def test_get_last_values(test_data):
    data = get_last_values(test_data, 3)
    assert [x['date'] for x in data] == ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364", "2019-04-04T23:20:05.206878",]

def test_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['        26.08.2019 Перевод организации\n' '        Maestro 159683** **** 5199 -> Счет ** 9589 \n''        31957.58руб.', '        03.07.2019 Перевод '
                                                                                                                                           'организации\n' 
                                                                                                                                       '        MasterCard 715830** **** 6758 -> '
                                                                                                                                       'Счет ** 5560 \n''        8221.37USD',
                    '        04.04.2019 Перевод со счета на счет\n        Счет ** 8542 -> Счет ** 4188 \n        79114.93USD']

@pytest.mark.parametrize("test_input,expected", [
    ("Счет 64686473678894779589 ", "Счет ** 9589 "),
    ("MasterCard 7158300734726758 ", "MasterCard 715830** **** 6758 ")
])
def test_ecode_bill_info(test_input, expected):
    assert encode_bill_info(test_input) == expected