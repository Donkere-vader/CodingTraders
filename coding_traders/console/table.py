

class Table:
    def __init__(self, table_title="", table_columns=[], minimum_rows=1):
        self.title = table_title
        self.table_columns = table_columns
        self.__entries = []
        self.minimum_rows = minimum_rows

    def add_entry(self, entry: dict):
        """ Adds an entry in the form of a dict in which the keys represent the column name """
        for column in self.table_columns:
            if column not in entry:
                entry[column] = ""

        self.__entries.append(entry)

    def remove_entry(self, **values):
        """ Removes and entry where all of the values specified by the ** are met """
        for e in self.__entries:
            found = True
            for key in values:
                if key not in e or e[key] != values[key]:
                    found = False
                    break
            if found:
                break

        self.__entries.remove(e)

    def __convert_value(self, value):
        if type(value) == int or type(value) == float:
            value = round(value, 2)

        return str(value)

    def __get_column_width(self, column):
        width = len(column) + 1
        for e in self.__entries:
            value = self.__convert_value(e[column])
            width = max(width, len(value) + 1)

        return width

    def __repr__(self):
        lines = []

        # columns
        column_row = ""
        column_widths = {}
        for column in self.table_columns:
            column_widths[column] = self.__get_column_width(column)
            column_row += column.ljust(column_widths[column]) + " "
        lines.append(column_row)

        # tabel title row (placeholder till end)
        lines.append("")

        # entries
        for idx, e in enumerate(self.__entries):
            entry_line = ""
            for column in self.table_columns:
                if type(e[column]) == int or type(e[column]) == float:
                    entry_line += self.__convert_value(e[column]).rjust(column_widths[column]) + " "
                else:
                    entry_line += self.__convert_value(e[column]).ljust(column_widths[column]) + " "
            lines.append(entry_line)

        for _ in range(self.minimum_rows - (idx + 1)):
            lines.append('~ ')

        # removing traling column sperator space
        lines = [line[:-1] for line in lines]

        max_line_length = 0
        for line in lines:
            max_line_length = max(max_line_length, len(line))

        # set table title/ seperat or
        lines[1] = f"[ {self.title} ] ".ljust(max_line_length, "-")

        return "\n".join(lines)

if __name__ == "__main__":
    # little example
    table = Table('stocks', ['Symb', 'amount', 'boughtval', 'curval'])

    entry = {
        "Symb": "DADA",
        "amount": 2,
        "boughtval": 3,
        "curval": 4
    }

    table.add_entry(entry)
    print(table)
