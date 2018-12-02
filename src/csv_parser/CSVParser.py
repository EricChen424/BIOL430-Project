from csv_parser.CSV import CSV

class CSVParser:
    def __init__(self):
        pass

    def _get_next_line(self, file):
        line = file.readline()
        if len(line) > 0 and line[len(line) - 1] == '\n':
            return line[0:len(line)-1]
        else:
            return line

    def parse_csv(self, path, has_headers=True):
        file = open(path, 'r')
        line = self._get_next_line(file)

        if has_headers:
            headers = line.split(",")
            line = self._get_next_line(file)
        else:
            headers = []

        data = []
        while line:
            row = line.split(",")
            data.append(row)
            line = self._get_next_line(file)

        csv = CSV(headers, data)
        return csv


