import pytest


@pytest.mark.mandatory
def test_http():
    from pystandards.http.mime_type import HttpMimeType
    from pystandards.http.method import HttpMethod
    
    assert HttpMimeType.APPLICATION_JSON.value == 'application/json'
    assert HttpMimeType.APPLICATION_JSON.name == 'APPLICATION_JSON'
    assert HttpMimeType.to_enum('application/json') == HttpMimeType.APPLICATION_JSON

    assert HttpMethod.GET.value == 'GET'
    assert HttpMethod.GET.name == 'GET'
    assert HttpMethod.to_enum('POST') == HttpMethod.POST


@pytest.mark.mandatory
def test_mime_type_from_file_extension():
    from pystandards.file import FileExtension, AudioFileExtension
    from pystandards.http.mime_type import HttpMimeType
    from tests.utils import assert_pytest_raises_exception

    assert HttpMimeType.from_file_extension(FileExtension.WAV) == HttpMimeType.AUDIO_WAV
    assert HttpMimeType.from_file_extension(AudioFileExtension.WAV) == HttpMimeType.AUDIO_WAV
    assert HttpMimeType.from_file_extension('wav') == HttpMimeType.AUDIO_WAV
    assert_pytest_raises_exception(
        function = lambda: HttpMimeType.from_file_extension('.wav'),
        exception_message = "'.wav' is not a valid FileExtension"
    )
