from pystandards.file import AudioFileExtension, VideoFileExtension, ImageFileExtension, TextFileExtension, FileExtension, file_extensions
from pystandards.enum import BaseEnumStr as Enum
from typing import Union


class HttpMimeType(Enum):
    """
    The `content_type` field that could come in the
    response of a http request we make, also known
    as `MIME type`.
    """

    # JSON
    APPLICATION_JSON = 'application/json'
    APPLICATION_LD_JSON = 'application/ld+json'
    APPLICATION_PROBLEM_JSON = 'application/problem+json'

    # Text
    TEXT_PLAIN = 'text/plain'
    TEXT_HTML = 'text/html'
    TEXT_CSS = 'text/css'
    TEXT_CSV = 'text/csv'
    TEXT_XML = 'text/xml'
    TEXT_EVENT_STREAM = 'text/event-stream'
    TEXT_JAVASCRIPT = 'text/javascript'

    # XML / Markup
    APPLICATION_XML = 'application/xml'
    APPLICATION_XHTML_XML = 'application/xhtml+xml'

    # JavaScript
    APPLICATION_JAVASCRIPT = 'application/javascript'

    # Binary / Generic files
    APPLICATION_OCTET_STREAM = 'application/octet-stream'
    APPLICATION_PDF = 'application/pdf'
    APPLICATION_ZIP = 'application/zip'
    APPLICATION_GZIP = 'application/gzip'
    APPLICATION_X_TAR = 'application/x-tar'

    # Forms
    MULTIPART_FORM_DATA = 'multipart/form-data'
    APPLICATION_X_WWW_FORM_URLENCODED = (
        'application/x-www-form-urlencoded'
    )

    # Streaming
    APPLICATION_NDJSON = 'application/x-ndjson'

    # SQL
    APPLICATION_SQL = 'application/sql'

    # Images
    IMAGE_JPEG = 'image/jpeg'
    IMAGE_PNG = 'image/png'
    IMAGE_WEBP = 'image/webp'
    IMAGE_GIF = 'image/gif'
    IMAGE_SVG_XML = 'image/svg+xml'
    IMAGE_BMP = 'image/bmp'
    IMAGE_X_ICON = 'image/x-icon'

    # Video
    VIDEO_MP4 = 'video/mp4'
    VIDEO_WEBM = 'video/webm'
    VIDEO_QUICKTIME = 'video/quicktime'
    VIDEO_X_MSVIDEO = 'video/x-msvideo'

    # Audio
    AUDIO_WAV = 'audio/wav'
    AUDIO_MPEG = 'audio/mpeg'
    AUDIO_OGG = 'audio/ogg'
    AUDIO_WEBM = 'audio/webm'
    AUDIO_FLAC = 'audio/flac'

    # Fonts
    FONT_WOFF = 'font/woff'
    FONT_WOFF2 = 'font/woff2'


    @classmethod
    def from_file_extension(
        cls,
        file_extension: Union[FileExtension, str]
    ) -> Union['HttpMimeType', None]:
        """
        Get the `HttpMimeType` that is associated to
        the `file_extension` provided. It can be None
        if the file extension is not registered.

        The `file_extension`, if string, must be just
        the extension in lowercase and including not
        the dot.

        Valid `file_extension` values:
        - `FileExtension.WAV`
        - `AudioFileExtension.WAV`
        - `"wav"`

        Invalid `file_extension` values:
        - `".wav"`
        - `"file.wav"`
        """
        if isinstance(file_extension, file_extensions):
            file_extension = FileExtension.to_enum(
                value = file_extension.value,
                do_accept_dot = False
            )
        elif isinstance(file_extension, str):
            file_extension = FileExtension.to_enum(
                value = file_extension,
                do_accept_dot = False
            )
        else:
            raise Exception('The "extension" provided is not a valid instance nor a string.')
        
        return FILE_EXTENSION_TO_HTTP_MIME_TYPE.get(file_extension, None)



HTTP_MIME_TYPE_TO_FILE_EXTENSION = {
    HttpMimeType.IMAGE_JPEG: FileExtension.JPEG,
    HttpMimeType.IMAGE_PNG: FileExtension.PNG,
    HttpMimeType.IMAGE_WEBP: FileExtension.WEBP,
    HttpMimeType.IMAGE_GIF: FileExtension.GIF,
    HttpMimeType.VIDEO_MP4: FileExtension.MP4,
    HttpMimeType.VIDEO_WEBM: FileExtension.WEBM,
    HttpMimeType.VIDEO_X_MSVIDEO: FileExtension.AVI,
    HttpMimeType.AUDIO_MPEG: FileExtension.MP3,
    HttpMimeType.AUDIO_WAV: FileExtension.WAV,
    HttpMimeType.AUDIO_OGG: FileExtension.OGG,
    HttpMimeType.AUDIO_FLAC: FileExtension.FLAC,
    HttpMimeType.APPLICATION_JSON: FileExtension.JSON,
    HttpMimeType.TEXT_PLAIN: FileExtension.TXT,
    HttpMimeType.TEXT_HTML: FileExtension.HTML,
    HttpMimeType.TEXT_CSS: FileExtension.CSS,
    HttpMimeType.TEXT_CSV: FileExtension.CSV,
    HttpMimeType.APPLICATION_PDF: FileExtension.PDF,
    HttpMimeType.APPLICATION_ZIP: FileExtension.ZIP,
}
"""
Dict to map the `HttpMimeType` to its
corresponding file extension Enum class.

This is very useful when we want to choose
the filename of a file that we are getting
from some url hat includes its content
type.
"""

FILE_EXTENSION_TO_HTTP_MIME_TYPE = {
    # JSON
    FileExtension.JSON: HttpMimeType.APPLICATION_JSON,

    # Text
    FileExtension.TXT: HttpMimeType.TEXT_PLAIN,
    FileExtension.HTML: HttpMimeType.TEXT_HTML,
    FileExtension.HTM: HttpMimeType.TEXT_HTML,
    FileExtension.CSS: HttpMimeType.TEXT_CSS,
    FileExtension.CSV: HttpMimeType.TEXT_CSV,
    FileExtension.XML: HttpMimeType.TEXT_XML,
    FileExtension.JS: HttpMimeType.APPLICATION_JAVASCRIPT,

    # Documents
    FileExtension.PDF: HttpMimeType.APPLICATION_PDF,

    # Archives
    FileExtension.ZIP: HttpMimeType.APPLICATION_ZIP,
    FileExtension.GZ: HttpMimeType.APPLICATION_GZIP,
    FileExtension.TAR: HttpMimeType.APPLICATION_X_TAR,

    # Images
    FileExtension.JPG: HttpMimeType.IMAGE_JPEG,
    FileExtension.JPEG: HttpMimeType.IMAGE_JPEG,
    FileExtension.PNG: HttpMimeType.IMAGE_PNG,
    FileExtension.WEBP: HttpMimeType.IMAGE_WEBP,
    FileExtension.GIF: HttpMimeType.IMAGE_GIF,
    FileExtension.SVG: HttpMimeType.IMAGE_SVG_XML,
    FileExtension.BMP: HttpMimeType.IMAGE_BMP,
    FileExtension.ICO: HttpMimeType.IMAGE_X_ICON,

    # Video
    FileExtension.MP4: HttpMimeType.VIDEO_MP4,
    FileExtension.WEBM: HttpMimeType.VIDEO_WEBM,
    FileExtension.MOV: HttpMimeType.VIDEO_QUICKTIME,
    FileExtension.AVI: HttpMimeType.VIDEO_X_MSVIDEO,

    # Audio
    FileExtension.WAV: HttpMimeType.AUDIO_WAV,
    FileExtension.MP3: HttpMimeType.AUDIO_MPEG,
    FileExtension.OGG: HttpMimeType.AUDIO_OGG,
    FileExtension.FLAC: HttpMimeType.AUDIO_FLAC,

    # Fonts
    FileExtension.WOFF: HttpMimeType.FONT_WOFF,
    FileExtension.WOFF2: HttpMimeType.FONT_WOFF2,
}
"""
Dict to map the `FileExtension` to its
corresponding mime type Enum class.

The file extension is expected to include
not the dot and be in lowercase.

This is very useful when we want to detect
the mime type from a file extension.
"""