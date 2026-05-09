from enum import Enum
from typing import Union


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