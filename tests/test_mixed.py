import pytest


@pytest.mark.mandatory
def test_base_enum():
    from pystandards.enum import BaseEnumStr, _get_enum_from_value

    class Color(BaseEnumStr):
        RED = 'red'
        BLUE = 'blue'

    class Aliases(BaseEnumStr):
        YES = ['yes', 'y', '1']
        NO = ['no', 'n', '0']

    class Permission(BaseEnumStr):
        READ = 'read'
        WRITE = 'write'

    # TODO: This is not actually a Str
    class Roles(BaseEnumStr):
        USER = [Permission.READ]
        ADMIN = [Permission.READ, Permission.WRITE]

    class EmptyEnum(BaseEnumStr):
        pass

    # Item variables
    assert Color.all() == [Color.RED, Color.BLUE]
    assert Color.names() == ['RED', 'BLUE']
    assert Color.values() == ['red', 'blue']

    # Is valid name
    assert Color.is_valid_name('RED')
    assert not Color.is_valid_name('INVALID')

    # Is valid name (ignore_case=True)
    assert Color.is_valid_name('red', do_ignore_case = True)
    assert Color.is_valid_name('ReD', do_ignore_case = True)

    # Getting enum from values
    assert _get_enum_from_value('red', Color) == Color.RED
    assert _get_enum_from_value('invalid', Color) is None
    assert _get_enum_from_value('y', Aliases) == Aliases.YES
    assert _get_enum_from_value(Permission.WRITE, Roles) == Roles.ADMIN
    assert _get_enum_from_value('WRITE', Roles) == Roles.ADMIN
    assert _get_enum_from_value('write', Roles) == Roles.ADMIN

    # Items
    assert Color.all() == [Color.RED, Color.BLUE]
    assert Color.names() == ['RED', 'BLUE']
    assert Color.values() == ['red', 'blue']

    # Empty BaseEnum
    assert EmptyEnum.all() == []
    assert EmptyEnum.names() == []
    assert EmptyEnum.values() == []
    assert _get_enum_from_value('anything', EmptyEnum) is None
    assert not EmptyEnum.is_valid_name('ANYTHING')

    # Special cases
    assert _get_enum_from_value(None, Color) is None
    assert not Color.is_valid_name(None)
    assert not Color.is_valid_name(123)
    assert not Color.is_valid_name([])
    assert not Color.is_valid_name({})
    assert not Color.is_valid_name('red')
    assert not Color.is_valid_name('ReD')
    assert Color.is_valid_name(
        'ReD',
        do_ignore_case = True
    )

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


@pytest.mark.mandatory
def test_ffmpeg():
    from pystandards.ffmpeg import FfmpegVideoCodec, FfmpegAudioCodec

    assert FfmpegVideoCodec.PRORES.value == 'prores'
    assert FfmpegVideoCodec.PRORES.name == 'PRORES'
    assert FfmpegVideoCodec.to_enum('tiff') == FfmpegVideoCodec.TIFF

    assert FfmpegAudioCodec.AAC.value == 'aac'
    assert FfmpegAudioCodec.AAC.name == 'AAC'
    assert FfmpegAudioCodec.to_enum('pcm_s8') == FfmpegAudioCodec.PCM_S8