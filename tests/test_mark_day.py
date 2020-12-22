from calendarutils import Calendar
import pytest
import mock
from mock import patch
from unittest.mock import Mock

def get_calendar():
    return Calendar()

@pytest.mark.parametrize("calendar", [get_calendar()])
def test_get_rows_from_calendar(calendar):
    rows = calendar.get_rows_from_calendar()

    assert isinstance(rows, list)
    assert len(rows) > 0

@pytest.mark.parametrize("calendar", [get_calendar()])
def test_update_calls_init(calendar):
    calendar.__init__ = Mock(return_value=True)
    calendar.update()

    assert calendar.__init__.called

@pytest.mark.parametrize("calendar", [get_calendar()])
def test_calendar_to_string(calendar):
    as_string = str(calendar)
    assert isinstance(as_string, str)
    assert len(as_string) > 0