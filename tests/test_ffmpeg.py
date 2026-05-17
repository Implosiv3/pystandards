import pytest


@pytest.mark.mandatory
def test_ffmpeg():
    from pystandards.ffmpeg import FfmpegVideoCodec, FfmpegAudioCodec

    assert FfmpegVideoCodec.PRORES.value == 'prores'
    assert FfmpegVideoCodec.PRORES.name == 'PRORES'
    assert FfmpegVideoCodec.to_enum('tiff') == FfmpegVideoCodec.TIFF

    assert FfmpegAudioCodec.AAC.value == 'aac'
    assert FfmpegAudioCodec.AAC.name == 'AAC'
    assert FfmpegAudioCodec.to_enum('pcm_s8') == FfmpegAudioCodec.PCM_S8