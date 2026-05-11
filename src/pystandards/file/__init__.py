from pystandards.file.utils import is_filename_valid_for_file_extension
from pystandards.enum import BaseEnumStr as Enum
from typing import Union

import random
import string


class _FileExtensionMixin:
    """
    *For internal use only*

    Mixin class to implement some common
    functionality in the different file
    classes.
    """

    @property
    def dotted(
        self
    ) -> str:
        """
        The extension, in lower case, but with the dot at the
        begining. Examples:
        - `FileExtension.PDF` -> `.pdf`
        - `FileExtension.WAV` -> `.wav`
        - `ImageFileExtension.BMP` -> `.bmp`
        - `ImageFileExtension.PNG` -> `.png`
        - `VideoFileExtension.MOV` -> `.mov`
        - `VideoFileExtension.MP4` -> `.mp4`
        - `AudioFileExtension.WAV` -> `.wav`
        - `AudioFileExtension.MP3` -> `.mp3`
        - `FileExtension.TXT` -> `.txt`
        - `FileExtension.XML` -> `.xml`
        - `SubtitleFileExtension.SRT` -> `.srt`
        - `SubtitleFileExtension.JSON3` -> `.json3`
        """
        return f'.{self.value}'
    
    @classmethod
    def to_enum(
        cls,
        value: any,
        do_accept_dot: bool = True
    ) -> 'TextFileExtension':
        """
        Convert a raw value into a valid enum member, raising
        an exception if there is no item with that value or
        as name or value.

        This method will accept the dot at the begining
        of the file extension if the `do_accept_dot`
        variable is `True`.

        Comparison is case-insensitive and checks:

        - enum.value
        - enum.name
        """
        if isinstance(value, cls):
            return value
        
        if isinstance(value, str):
            value = (
                value.replace('.', '')
                if do_accept_dot else
                value
            )

        return super().to_enum(value)
    
    @classmethod
    def try_to_enum(
        cls,
        value: any,
        do_accept_dot: bool = True,
        default: Union[any, None] = None
    ):
        """
        Try to parse the `value` provided as the Enum,
        returning the `default` if not possible because
        there is no `Enum` item with that value.
        
        This method will accept the dot at the begining
        of the file extension if the `do_accept_dot`
        variable is `True`.
        """
        try:
            return cls.to_enum(
                value = value,
                do_accept_dot = do_accept_dot
            )
        except:
            return default
        
    @classmethod
    def is_filename_valid(
        cls,
        filename: str
    ):
        """
        Check if the `filename` provided is valid for this
        `FileExtension` class.
        """
        return is_filename_valid_for_file_extension(
            filename = filename,
            file_extension_enum_class = cls
        )
    
    def get_filename(
        self,
        filename: Union[str, None] = None
    ) -> str:
        """
        Get the `filename` provided with this file extension
        or a random one if `filename` is `None` or an empty
        string.
        """
        if (
            isinstance(filename, str) and
            not filename.strip()
        ):
            filename = None

        filename = (
            ''.join(random.choices(string.ascii_letters + string.digits, k = 10))
            if filename is None else
            filename
        )

        return f'{filename}{self.dotted}'


class FileExtension(_FileExtensionMixin, Enum):
    """
    Enum class to encapsulate all the file
    extensions that we are able to handle.

    These extensions values don't include the
    dot and are in lower case.
    """

    # IMAGE
    PNG = 'png'
    """
    Portable Network Graphics
    """
    JPEG = 'jpeg'
    """
    Joint Photographic Experts Group
    """
    JPG = 'jpg'
    """
    Joint Photographic Experts Group
    """
    WEBP = 'webp'
    """
    Web Picture
    """
    BMP = 'bmp'
    """
    Bitmap Image File
    """
    GIF = 'gif'
    """
    Graphics Interchange Format
    """
    TIFF = 'tiff'
    """
    Tagged Image File
    """
    PSD = 'psd'
    """
    Photoshop Document
    """
    PDF = 'pdf'
    """
    Portable Document Format
    """
    DOC = 'doc'
    """
    Microsoft Word document old format.
    """
    DOCX = 'docx'
    """
    Microsoft Word document new format.
    """
    EPS = 'eps'
    """
    Encapsulated Postcript
    """
    AI = 'ai'
    """
    Adobe ILlustrator Document
    """
    INDD = 'indd'
    """
    Adobe Indesign Document
    """
    RAW = 'raw'
    """
    Raw Image Formats
    """
    CDR = 'cdr'
    """
    Corel Draw
    """
    # AUDIO
    WAV = 'wav'
    """
    Waveform Audio
    """
    MP3 = 'mp3'
    """
    MPEG Audio Layer 3.
    """
    M4A = 'm4a'
    """
    MPEG-4 Audio
    """
    FLAC = 'flac'
    """
    Free Lossless Audio Codec.
    """
    WMA = 'wma'
    """
    Windows Media Audio
    """
    AAC = 'aac'
    """
    Advanced Audio Coding
    """
    CD = 'cd'
    """
    Compact Disc.
    """
    OGG = 'ogg'
    """
    Ogg Vorbis.
    """
    AIF = 'aif'
    """
    Audio Interchange File Format.
    """
    # VIDEO
    MOV = 'mov'
    """
    Apple video
    """
    MP4 = 'mp4'
    """
    MPEG-4
    """
    WEBM = 'webm'
    """
    Developed by Google, subgroup of the open and standard Matroska Video Container (MKV)
    """
    AVI = 'avi'
    """
    Audio Video Interleave
    """
    WMV = 'wmv'
    """
    Windows Media Video
    """
    AVCHD = 'avchd'
    """
    Advanced Video Coding High Definition
    """
    FVL = 'flv'
    """
    Flash Video
    """
    # SUBTITLES
    SRT = 'srt'
    """
    Srt subtitle file extension.

    This is the format:
    1
    00:00:00,000 --> 00:00:02,500
    Welcome to the Example Subtitle File!

    """
    JSON3 = 'json3'
    """
    Json3 subtitle file extension
    """
    SRV1 = 'srv1'
    """
    Srv1 subtitle file extension
    """
    SRV2 = 'srv2'
    """
    Srv2 subtitle file extension
    """
    SRV3 = 'srv3'
    """
    Srv3 subtitle file extension
    """
    TTML = 'ttml'
    """
    Ttml subtitle file extension
    """
    VTT = 'vtt'
    """
    Vtt subtitle file extension
    """
    # TEXT
    TXT = 'txt'
    """
    Txt text file extension
    """
    CSV = 'csv'
    """
    Csv text file extension
    """
    JSON = 'json'
    """
    Json text file extension
    """
    XML = 'xml'
    """
    Xml text file extension
    """
    HTML = 'html'
    """
    Html text file extension
    """
    MD = 'md'
    """
    Md text file extension
    """
    LOG = 'log'
    """
    Log text file extension
    """
    INI = 'ini'
    """
    Ini text file extension
    """
    YAML = 'yaml'
    """
    Yaml text file extension
    """
    YML = 'yml'
    """
    Yml text file extension
    """
    
    
class ImageFileExtension(_FileExtensionMixin, Enum):
    """
    Enum class to encapsulate all existing image file
    extensions.

    These extensions values don't include the
    dot and are in lower case.
    """
    
    PNG = FileExtension.PNG.value
    """
    Portable Network Graphics
    """
    JPEG = FileExtension.JPEG.value
    """
    Joint Photographic Experts Group
    """
    JPG = FileExtension.JPG.value
    """
    Joint Photographic Experts Group
    """
    WEBP = FileExtension.WEBP.value
    """
    Web Picture
    """
    BMP = FileExtension.BMP.value
    """
    Bitmap Image File
    """
    GIF = FileExtension.GIF.value
    """
    Graphics Interchange Format
    """
    TIFF = FileExtension.TIFF.value
    """
    Tagged Image File
    """
    PSD = FileExtension.PSD.value
    """
    Photoshop Document
    """
    PDF = FileExtension.PDF.value
    """
    Portable Document Format
    """
    EPS = FileExtension.EPS.value
    """
    Encapsulated Postcript
    """
    AI = FileExtension.AI.value
    """
    Adobe Illustrator Document
    """
    INDD = FileExtension.INDD.value
    """
    Adobe Indesign Document
    """
    RAW = FileExtension.RAW.value
    """
    Raw Image Formats
    """
    CDR = FileExtension.CDR.value
    """
    Corel Draw
    """
    # TODO: Add more
    

class AudioFileExtension(_FileExtensionMixin, Enum):
    """
    Enum class to encapsulate all existing audio file
    extensions.

    These extensions values don't include the
    dot and are in lower case.
    """

    WAV = FileExtension.WAV.value
    """
    Waveform Audio
    """
    MP3 = FileExtension.MP3.value
    """
    MPEG Audio Layer 3.
    """
    M4A = FileExtension.M4A.value
    """
    MPEG-4 Audio
    """
    FLAC = FileExtension.FLAC.value
    """
    Free Lossless Audio Codec.
    """
    WMA = FileExtension.WMA.value
    """
    Windows Media Audio
    """
    AAC = FileExtension.AAC.value
    """
    Advanced Audio Coding
    """
    WEBM = FileExtension.WEBM.value
    """
    Web Media.
    """
    CD = FileExtension.CD.value
    """
    Compact Disc.
    """
    OGG = FileExtension.OGG.value
    """
    Ogg Vorbis.
    """
    AIF = FileExtension.AIF.value
    """
    Audio Interchange File Format.
    """


class VideoFileExtension(_FileExtensionMixin, Enum):
    """
    Enum class to encapsulate all existing video file
    extensions.

    These extensions values don't include the
    dot and are in lower case.
    """

    MOV = FileExtension.MOV.value
    """
    Apple video
    """
    MP4 = FileExtension.MP4.value
    """
    MPEG-4
    """
    WEBM = FileExtension.WEBM.value
    """
    Developed by Google, subgroup of the open and standard Matroska Video Container (MKV)
    """
    AVI = FileExtension.AVI.value
    """
    Audio Video Interleave
    """
    WMV = FileExtension.WMV.value
    """
    Windows Media Video
    """
    AVCHD = FileExtension.AVCHD.value
    """
    Advanced Video Coding High Definition
    """
    FVL = FileExtension.FVL.value
    """
    Flash Video
    """
    # TODO: Add more


class SubtitleFileExtension(_FileExtensionMixin, Enum):
    """
    Enum class to encapsulate all existing subtitle
    file extensions.

    These extensions values don't include the
    dot and are in lower case.
    """

    SRT = FileExtension.SRT.value
    """
    Srt subtitle file extension.

    This is the format:
    1
    00:00:00,000 --> 00:00:02,500
    Welcome to the Example Subtitle File!

    """
    JSON3 = FileExtension.JSON3.value
    """
    Json3 subtitle file extension
    """
    SRV1 = FileExtension.SRV1.value
    """
    Srv1 subtitle file extension
    """
    SRV2 = FileExtension.SRV2.value
    """
    Srv2 subtitle file extension
    """
    SRV3 = FileExtension.SRV3.value
    """
    Srv3 subtitle file extension
    """
    TTML = FileExtension.TTML.value
    """
    Ttml subtitle file extension
    """
    VTT = FileExtension.VTT.value
    """
    Vtt subtitle file extension
    """
    

class TextFileExtension(_FileExtensionMixin, Enum):
    """
    Enum class to encapsulate all existing text
    file extensions.

    These extensions values don't include the
    dot and are in lower case.
    """

    TXT = FileExtension.TXT.value
    """
    Txt subtitle file extension
    """
    JSON = FileExtension.JSON.value
    """
    Json text file extension
    """
    XML = FileExtension.XML.value
    """
    Xml text file extension
    """
    HTML = FileExtension.HTML.value
    """
    Html text file extension
    """
    MD = FileExtension.MD.value
    """
    Md text file extension
    """
    LOG = FileExtension.LOG.value
    """
    Log text file extension
    """
    INI = FileExtension.INI.value
    """
    Ini text file extension
    """
    YAML = FileExtension.YAML.value
    """
    Yaml text file extension
    """
    YML = FileExtension.YML.value
    """
    Yml text file extension
    """

# TODO: Associate 'FileType' with extensions