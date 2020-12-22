def format_day(piece, day, i):
    if piece == day:
        formatted_day = f'({piece})'
        return ' ' + formatted_day
    else:
        if i > 0:
            return ' ' + str(piece)
        else:
            return str(piece)


class Row():

    def __init__(self, row_string, row_number):
        self.row_string = row_string
        self.formatted_row = ''
        self.row_number = row_number

    def __str__(self):
        return self.get_formatted_string()

    def get_formatted_string(self):
        return self.formatted_row if len(self.formatted_row) > 0 else self.row_string

    def format(self, day):
        digit_pieces =\
            list(map(
                int,
                filter(lambda x: x.isdigit(), self.row_string.strip().split(' '))
            ))
        formatted_pieces = list(map(
            lambda x: format_day(x[1], day, x[0]), enumerate(digit_pieces)
        ))
        if day in digit_pieces:
            print("It is happening!")
            self.formatted_row = ''.join(formatted_pieces)
            return self
        return None