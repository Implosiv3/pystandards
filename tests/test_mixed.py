import pytest


@pytest.mark.mandatory
def test_mandatory():
    from pystandards.http import HttpContentType, HttpMethod
    
    assert HttpContentType.APPLICATION_JSON.value == 'application/json'
    assert HttpContentType.APPLICATION_JSON.name == 'APPLICATION_JSON'
    assert HttpContentType.to_enum('application/json') == HttpContentType.APPLICATION_JSON

    assert HttpMethod.GET.value == 'GET'
    assert HttpMethod.GET.name == 'GET'
    assert HttpMethod.to_enum('POST') == HttpMethod.POST