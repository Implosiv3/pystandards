import pytest


@pytest.mark.mandatory
def test_lang():
    from pystandards.lang import LanguageISO639

    assert LanguageISO639.SPANISH.value == 'es'
    assert LanguageISO639.ENGLISH.name == 'ENGLISH'
    assert LanguageISO639.to_enum('it') == LanguageISO639.ITALIAN