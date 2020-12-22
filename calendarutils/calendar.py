from calendarutils import get_current_day, get_calendar_string
from calendarutils.row import Row


class Calendar():

    def __init__(self):
        self.day = get_current_day()
        self.calendar_string = get_calendar_string()
        self.rows = self.get_rows_from_calendar()
        self.mark()

    def get_rows_from_calendar(self):
        return list(map(lambda x: Row(x[1], x[0]),
            enumerate(self.calendar_string.split('\n'))))

    def get_formatted_row_based_on_day(self):
        return list(filter(
            lambda x: x is not None,
            map(lambda x: x.format(self.day), self.rows)
        )).pop()

    def replace_row(self, row):
        self.rows[row.row_number] = row

    def mark(self):
        self.replace_row(self.get_formatted_row_based_on_day())

    def update(self):
        self.__init__()
        
    def __str__(self):
        return '\n'.join([str(row) for row in self.rows])