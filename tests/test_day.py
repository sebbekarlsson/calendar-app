from calendarutils.day import get_current_day


def test_get_current_day_works_as_expected():
    day = get_current_day()

    assert day is not None


def test_get_current_day_is_int():
    day = get_current_day()

    assert isinstance(day, int)