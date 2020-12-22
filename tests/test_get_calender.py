from calendarutils import get_calendar_string


def test_calendar_is_string():
    contents = get_calendar_string()

    assert isinstance(contents, str)