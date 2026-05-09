from pystandards.enum import BaseEnum as Enum


class HttpContentType(Enum):
    """
    The `content_type` field that could come in the
    response of a http request we make.
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


class HttpMethod(Enum):
    """
    The methods that are supported in the Http
    requests que make.
    """

    # Standard methods
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
    HEAD = 'HEAD'
    OPTIONS = 'OPTIONS'
    TRACE = 'TRACE'
    CONNECT = 'CONNECT'

    # WebDAV methods
    PROPFIND = 'PROPFIND'
    PROPPATCH = 'PROPPATCH'
    MKCOL = 'MKCOL'
    COPY = 'COPY'
    MOVE = 'MOVE'
    LOCK = 'LOCK'
    UNLOCK = 'UNLOCK'

    # Versioning / Delta encoding
    VERSION_CONTROL = 'VERSION-CONTROL'
    REPORT = 'REPORT'
    CHECKOUT = 'CHECKOUT'
    CHECKIN = 'CHECKIN'
    UNCHECKOUT = 'UNCHECKOUT'
    MKWORKSPACE = 'MKWORKSPACE'
    UPDATE = 'UPDATE'
    LABEL = 'LABEL'
    MERGE = 'MERGE'
    BASELINE_CONTROL = 'BASELINE-CONTROL'
    MKACTIVITY = 'MKACTIVITY'

    # UPnP
    NOTIFY = 'NOTIFY'
    SUBSCRIBE = 'SUBSCRIBE'
    UNSUBSCRIBE = 'UNSUBSCRIBE'

    # RFC 5789
    SEARCH = 'SEARCH'

    # CalDAV
    MKCALENDAR = 'MKCALENDAR'

    # RFC 2068
    LINK = 'LINK'
    UNLINK = 'UNLINK'

    # Icecast / unofficial
    SOURCE = 'SOURCE'