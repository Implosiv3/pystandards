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