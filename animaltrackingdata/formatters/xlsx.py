from logging import Formatter
import xlsxwriter
from .formatter import Formatter

class XLSXFormatter(Formatter):

    def __init__(self, path):
        self.path = path

    def writeJSON(self, data):
        workbook = xlsxwriter.Workbook(self.path, {'constant_memory': True})
        worksheet = workbook.add_worksheet()

        firstrow = [*data[0]]
        row = 0
        col = 0

        for coldata in firstrow:
            worksheet.write(row, col, coldata)
            col += 1

        row += 1

        for rowdata in data:
            col = 0

            for item in rowdata.values():
                worksheet.write(row, col, item)
                col += 1
        
            row += 1
        
        workbook.close()

    def writeScroll(self, data):
        workbook = xlsxwriter.Workbook(self.path, {'constant_memory': True})
        worksheet = workbook.add_worksheet()
        row = 0

        for rowdata in data.get_positions():
            col = 0

            for item in rowdata:
                worksheet.write(row, col, item)
                col += 1
        
            row += 1
        
        workbook.close()

