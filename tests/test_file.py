import pytest


@pytest.mark.mandatory
def test_file():
    from pystandards.file import FileExtension, TextFileExtension, ImageFileExtension, VideoFileExtension, AudioFileExtension, SubtitleFileExtension, get_extension

    assert FileExtension.TXT.value == 'txt'
    assert FileExtension.PDF.name == 'PDF'
    assert FileExtension.to_enum(FileExtension.WAV, False) == FileExtension.WAV
    assert FileExtension.to_enum('wav', False) == FileExtension.WAV
    assert FileExtension.to_enum('wav', True) == FileExtension.WAV
    assert FileExtension.to_enum('.wav', True) == FileExtension.WAV
    assert FileExtension.try_to_enum('.wav', False, None) == None
    assert FileExtension.try_to_enum('.wav', True, None) == FileExtension.WAV
    assert FileExtension.is_filename_valid('example.pdf') is True
    assert FileExtension.is_filename_valid('example.itdoesntexist') is False
    assert FileExtension.PDF.get_filename().endswith('.pdf')

    assert TextFileExtension.XML.value == 'xml'
    assert TextFileExtension.XML.name == 'XML'
    assert TextFileExtension.to_enum(TextFileExtension.HTML, False) == TextFileExtension.HTML
    assert TextFileExtension.to_enum('html', False) == TextFileExtension.HTML
    assert TextFileExtension.to_enum('html', True) == TextFileExtension.HTML
    assert TextFileExtension.to_enum('.html', True) == TextFileExtension.HTML
    assert TextFileExtension.try_to_enum('.html', False, None) == None
    assert TextFileExtension.try_to_enum('.html', True, None) == TextFileExtension.HTML
    assert TextFileExtension.is_filename_valid('example.txt') is True
    assert TextFileExtension.is_filename_valid('example.itdoesntexist') is False
    assert TextFileExtension.TXT.get_filename().endswith('.txt')

    assert ImageFileExtension.JPG.value == 'jpg'
    assert ImageFileExtension.JPG.name == 'JPG'
    assert ImageFileExtension.to_enum(ImageFileExtension.BMP, False) == ImageFileExtension.BMP
    assert ImageFileExtension.to_enum('bmp', False) == ImageFileExtension.BMP
    assert ImageFileExtension.to_enum('bmp', True) == ImageFileExtension.BMP
    assert ImageFileExtension.to_enum('.bmp', True) == ImageFileExtension.BMP
    assert ImageFileExtension.try_to_enum('.bmp', False, None) == None
    assert ImageFileExtension.try_to_enum('.bmp', True, None) == ImageFileExtension.BMP
    assert ImageFileExtension.is_filename_valid('example.bmp') is True
    assert ImageFileExtension.is_filename_valid('example.itdoesntexist') is False
    assert ImageFileExtension.BMP.get_filename().endswith('.bmp')

    assert VideoFileExtension.MP4.value == 'mp4'
    assert VideoFileExtension.MP4.name == 'MP4'
    assert VideoFileExtension.to_enum(VideoFileExtension.MOV, False) == VideoFileExtension.MOV
    assert VideoFileExtension.to_enum('mov', False) == VideoFileExtension.MOV
    assert VideoFileExtension.to_enum('mov', True) == VideoFileExtension.MOV
    assert VideoFileExtension.to_enum('.mov', True) == VideoFileExtension.MOV
    assert VideoFileExtension.try_to_enum('.mov', False, None) == None
    assert VideoFileExtension.try_to_enum('.mov', True, None) == VideoFileExtension.MOV
    assert VideoFileExtension.is_filename_valid('example.mov') is True
    assert VideoFileExtension.is_filename_valid('example.itdoesntexist') is False
    assert VideoFileExtension.MOV.get_filename().endswith('.mov')

    assert AudioFileExtension.MP3.value == 'mp3'
    assert AudioFileExtension.MP3.name == 'MP3'
    assert AudioFileExtension.to_enum(AudioFileExtension.WAV, False) == AudioFileExtension.WAV
    assert AudioFileExtension.to_enum('wav', False) == AudioFileExtension.WAV
    assert AudioFileExtension.to_enum('wav', True) == AudioFileExtension.WAV
    assert AudioFileExtension.to_enum('.wav', True) == AudioFileExtension.WAV
    assert AudioFileExtension.try_to_enum('.wav', False, None) == None
    assert AudioFileExtension.try_to_enum('.wav', True, None) == AudioFileExtension.WAV
    assert AudioFileExtension.is_filename_valid('example.wav') is True
    assert AudioFileExtension.is_filename_valid('example.itdoesntexist') is False
    assert AudioFileExtension.MP3.get_filename().endswith('.mp3')

    assert SubtitleFileExtension.SRT.value == 'srt'
    assert SubtitleFileExtension.SRT.name == 'SRT'
    assert SubtitleFileExtension.to_enum(SubtitleFileExtension.JSON3, False) == SubtitleFileExtension.JSON3
    assert SubtitleFileExtension.to_enum('json3', False) == SubtitleFileExtension.JSON3
    assert SubtitleFileExtension.to_enum('json3', True) == SubtitleFileExtension.JSON3
    assert SubtitleFileExtension.to_enum('.json3', True) == SubtitleFileExtension.JSON3
    assert SubtitleFileExtension.try_to_enum('.json3', False, None) == None
    assert SubtitleFileExtension.try_to_enum('.json3', True, None) == SubtitleFileExtension.JSON3
    assert SubtitleFileExtension.is_filename_valid('example.json3') is True
    assert SubtitleFileExtension.is_filename_valid('example.itdoesntexist') is False
    assert SubtitleFileExtension.SRT.get_filename().endswith('.srt')

    assert get_extension('wav') == AudioFileExtension.WAV
    assert get_extension('.wav') == AudioFileExtension.WAV
    assert get_extension('mov') == VideoFileExtension.MOV
    assert get_extension('.mov') == VideoFileExtension.MOV
    assert get_extension('bmp') == ImageFileExtension.BMP
    assert get_extension('.bmp') == ImageFileExtension.BMP
    assert get_extension('txt') == TextFileExtension.TXT
    assert get_extension('.txt') == TextFileExtension.TXT
    assert get_extension('srt') == SubtitleFileExtension.SRT
    assert get_extension('.srt') == SubtitleFileExtension.SRT


@pytest.mark.mandatory
def test_file_extension_from_mime_type():
    from pystandards.file import FileExtension
    from pystandards.http.mime_type import HttpMimeType
    from tests.utils import assert_pytest_raises_exception

    assert FileExtension.from_http_mime_type(HttpMimeType.AUDIO_WAV) == FileExtension.WAV
    assert FileExtension.from_http_mime_type('audio/wav') == FileExtension.WAV
    assert_pytest_raises_exception(
        function = lambda: FileExtension.from_http_mime_type('audio/invented'),
        exception_message = "'audio/invented' is not a valid HttpMimeType"
    )