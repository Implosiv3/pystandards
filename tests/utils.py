import pytest


def assert_pytest_raises_exception(
    function,
    exception_message: str = ''
):
    """
    Assert that the `function` provided, that must
    be a lambda function, raises an exception with
    the `exception_message` given (if given).
    """
    with pytest.raises(
        ValueError,
        match = exception_message,
    ):
        function()

    assert True