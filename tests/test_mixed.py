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


@pytest.mark.mandatory
def test_file():
    from pystandards.file import FileExtension, TextFileExtension, ImageFileExtension, VideoFileExtension, AudioFileExtension, SubtitleFileExtension

    assert FileExtension.TXT.value == 'txt'
    assert FileExtension.PDF.name == 'PDF'
    assert FileExtension.to_enum('wav', False) == FileExtension.WAV
    assert FileExtension.to_enum('wav', True) == FileExtension.WAV
    assert FileExtension.to_enum('.wav', True) == FileExtension.WAV
    assert FileExtension.try_to_enum('.wav', False, None) == None
    assert FileExtension.try_to_enum('.wav', True, None) == FileExtension.WAV

    assert TextFileExtension.XML.value == 'xml'
    assert TextFileExtension.XML.name == 'XML'
    assert TextFileExtension.to_enum('html', False) == TextFileExtension.HTML
    assert TextFileExtension.to_enum('html', True) == TextFileExtension.HTML
    assert TextFileExtension.to_enum('.html', True) == TextFileExtension.HTML
    assert TextFileExtension.try_to_enum('.html', False, None) == None
    assert TextFileExtension.try_to_enum('.html', True, None) == TextFileExtension.HTML

    assert ImageFileExtension.JPG.value == 'jpg'
    assert ImageFileExtension.JPG.name == 'JPG'
    assert ImageFileExtension.to_enum('bmp', False) == ImageFileExtension.BMP
    assert ImageFileExtension.to_enum('bmp', True) == ImageFileExtension.BMP
    assert ImageFileExtension.to_enum('.bmp', True) == ImageFileExtension.BMP
    assert ImageFileExtension.try_to_enum('.bmp', False, None) == None
    assert ImageFileExtension.try_to_enum('.bmp', True, None) == ImageFileExtension.BMP

    assert VideoFileExtension.MP4.value == 'mp4'
    assert VideoFileExtension.MP4.name == 'MP4'
    assert VideoFileExtension.to_enum('mov', False) == VideoFileExtension.MOV
    assert VideoFileExtension.to_enum('mov', True) == VideoFileExtension.MOV
    assert VideoFileExtension.to_enum('.mov', True) == VideoFileExtension.MOV
    assert VideoFileExtension.try_to_enum('.mov', False, None) == None
    assert VideoFileExtension.try_to_enum('.mov', True, None) == VideoFileExtension.MOV

    assert AudioFileExtension.MP3.value == 'mp3'
    assert AudioFileExtension.MP3.name == 'MP3'
    assert AudioFileExtension.to_enum('wav', False) == AudioFileExtension.WAV
    assert AudioFileExtension.to_enum('wav', True) == AudioFileExtension.WAV
    assert AudioFileExtension.to_enum('.wav', True) == AudioFileExtension.WAV
    assert AudioFileExtension.try_to_enum('.wav', False, None) == None
    assert AudioFileExtension.try_to_enum('.wav', True, None) == AudioFileExtension.WAV

    assert SubtitleFileExtension.SRT.value == 'srt'
    assert SubtitleFileExtension.SRT.name == 'SRT'
    assert SubtitleFileExtension.to_enum('json3', False) == SubtitleFileExtension.JSON3
    assert SubtitleFileExtension.to_enum('json3', True) == SubtitleFileExtension.JSON3
    assert SubtitleFileExtension.to_enum('.json3', True) == SubtitleFileExtension.JSON3
    assert SubtitleFileExtension.try_to_enum('.json3', False, None) == None
    assert SubtitleFileExtension.try_to_enum('.json3', True, None) == SubtitleFileExtension.JSON3


@pytest.mark.mandatory
def test_ffmpeg():
    from pystandards.ffmpeg import FfmpegVideoCodec, FfmpegAudioCodec

    assert FfmpegVideoCodec.PRORES.value == 'prores'
    assert FfmpegVideoCodec.PRORES.name == 'PRORES'
    assert FfmpegVideoCodec.to_enum('tiff') == FfmpegVideoCodec.TIFF

    assert FfmpegAudioCodec.AAC.value == 'aac'
    assert FfmpegAudioCodec.AAC.name == 'AAC'
    assert FfmpegAudioCodec.to_enum('pcm_s8') == FfmpegAudioCodec.PCM_S8