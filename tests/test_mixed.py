import pytest


@pytest.mark.mandatory
def test_http():
    from pystandards.http import HttpContentType, HttpMethod
    
    assert HttpContentType.APPLICATION_JSON.value == 'application/json'
    assert HttpContentType.APPLICATION_JSON.name == 'APPLICATION_JSON'
    assert HttpContentType.to_enum('application/json') == HttpContentType.APPLICATION_JSON

    assert HttpMethod.GET.value == 'GET'
    assert HttpMethod.GET.name == 'GET'
    assert HttpMethod.to_enum('POST') == HttpMethod.POST

@pytest.mark.mandatory
def test_lang():
    from pystandards.lang import LanguageISO639

    assert LanguageISO639.SPANISH.value == 'es'
    assert LanguageISO639.ENGLISH.name == 'ENGLISH'
    assert LanguageISO639.to_enum('it') == LanguageISO639.ITALIAN