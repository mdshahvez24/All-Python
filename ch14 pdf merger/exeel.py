##   Excel workbook is  created

import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx')
workbook.close()


## workbook created with hello
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

## passing hellow in A1 column
worksheet.write('A1', 'Hello world')
worksheet.write('A2', 'Hello girl')
worksheet.write(3, 0, 123)
workbook.close()


