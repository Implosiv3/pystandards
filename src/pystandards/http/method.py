from pystandards.enum import BaseEnumStr as Enum


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