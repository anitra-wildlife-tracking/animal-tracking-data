import csv
from .formatter import Formatter

class CSVFormatter(Formatter):

    def __init__(self, path):
        self.path = path

    def writeJSON(self, data):
        with open(self.path, 'w') as file:
            writer = csv.writer(file, dialect='excel', lineterminator='\n')
            writer.writerow([*data[0]])

            for row in data:
                values = row.values()

                writer.writerow(
                    [str(s).replace('\n', '\\n') if s != None else '' for s in values]
                )

    def writeScroll(self, scroll):
        with open(self.path, 'w') as file:
            writer = csv.writer(file, dialect='excel', lineterminator='\n')

            for row in scroll.get_positions():
                if row != None:
                    writer.writerow(
                        [str(s).replace('\n', '\\n') if s != None else '' for s in row]
                    )
    

