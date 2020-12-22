from calendarutils.add_pie import add_pie_to_string
import pytest


@pytest.mark.parametrize("value", [
    "apple",
    "pear",
    "banana",
    "berry"
])
def test_add_pie(value):
    result = add_pie_to_string(value)
    assert '-pie' in result