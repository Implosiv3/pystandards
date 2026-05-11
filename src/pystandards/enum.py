from enum import Enum
from typing import Union, Any


class BaseEnum(Enum):
    """
    Custom Enum class that is able to autodetect
    and parse values based on its `name` and/or
    its `value`.
    """

    @classmethod
    def names(
        cls
    ) -> list[str]:
        """
        A list containing all the names that are registered
        in this `BaseEnum` class.
        """
        return [
            x.name
            for x in cls
        ]

    @classmethod
    def values(
        cls
    ) -> list[any]:
        """
        A list containing all the values that are registered
        in this `BaseEnum` class.
        """
        return [
            x.value
            for x in cls
        ]
    
    @classmethod
    def all(
        cls
    ) -> list['BaseEnum']:
        """
        A list containing all the items of this `BaseEnum`
        class.
        """
        return [
            x
            for x in cls
        ]
    
    @classmethod
    def default(
        cls
    ) -> 'BaseEnum':
        """
        Get the default value, which is always the first one.
        """
        return cls[0]
    
    @classmethod
    def _normalized_map(
        cls
    ):
        """
        *For internal use only*

        Internal cache to make it faster when the list
        of items is big.
        """

        if not hasattr(cls, '__normalized_map'):
            mapping = {}

            for item in cls:
                mapping[item.name.lower()] = item
                mapping[str(item.value).strip().lower()] = item
            cls.__normalized_map = mapping

        return cls.__normalized_map

    @classmethod
    def to_enum(
        cls,
        value: any
    ):
        """
        Convert a raw value into a valid enum member,
        raising an exception if there is no item with
        that `value` or as name or value.

        Comparison is case-insensitive and checks:
        - enum.value
        - enum.name
        """
        if isinstance(value, cls):
            return value

        normalized = str(value).strip().lower()

        try:
            return cls._normalized_map()[normalized]

        except KeyError:
            raise ValueError(
                f'{value!r} is not a valid {cls.__name__}'
            ) from None
    
    @classmethod
    def try_to_enum(
        cls,
        value: any,
        default: Union[any, None] = None
    ):
        """
        Try to parse the `value` provided as the Enum,
        returning the `default` if not possible because
        there is no `Enum` item with that value.
        """
        try:
            return cls.to_enum(value)
        except:
            return default
        
    @classmethod
    def is_valid(
        cls,
        name_or_value: Union[str, Any],
        do_ignore_case: bool = True
    ) -> bool:
        """
        Check if the `name_or_value` provided is a valid
        name or a valid value for this `BaseEnum` class,
        ignoring case for the name if the `do_ignore_case`
        parameter is `True`.
        """
        return (
            cls.is_valid_name(
                name = name_or_value,
                do_ignore_case = do_ignore_case
            )
            or
            cls.is_valid_value(
                value = name_or_value
            )
        )
        
    @classmethod
    def is_valid_name(
        cls,
        name: str,
        do_ignore_case: bool = False
    ) -> bool:
        """
        Check if the `name` provided is a valid `name` for
        this `BaseEnum` class, ignoring case if the 
        `do_ignore_case` parameter is `True`.
        """
        if not isinstance(name, str):
            return False

        names = cls.__members__.keys()

        if do_ignore_case:
            name = name.lower()

            return any(
                enum_name.lower() == name
                for enum_name in names
            )

        return name in names
    
    @classmethod
    def is_valid_value(
        cls,
        value: Any,
    ) -> bool:
        """
        Check if the `value` provided is a valid value for this
        `BaseEnum` class.
        """
        try:
            if _get_enum_from_value(
                value = value,
                enum = cls
            ):
                return True
            
            return False
        except Exception:
            return False
        

def _get_enum_from_value(
    value: Any,
    enum: type[BaseEnum]
) -> Union[BaseEnum, None]:
    """
    *For internal use only*

    Return the enum member matching the provided `value`
    if existing, or `None` if not.

    Supports:
    - direct enum values
    - lists of values
    - lists of enum instances
    """
    members = enum.all()

    if not members:
        return None

    first_value = members[0].value

    # Standard enum values
    if not isinstance(first_value, list):
        try:
            return enum(value)
        except ValueError:
            return None

    # List-based enum values
    is_list_of_enums = (
        first_value
        and
        isinstance(first_value[0], Enum)
    )

    for member in members:
        if is_list_of_enums:
            for item in member.value:
                if value in (
                    item,
                    item.value,
                    item.name
                ):
                    return member

        else:
            if value in member.value:
                return member

    return None