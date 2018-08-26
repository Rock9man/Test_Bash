#!/usr/bin/env python

import xlwt, xlrd

from xlutils.copy import copy

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')

sheet.write(0,1,'test 1')
sheet.write(1,1,'test 1')
wbk.save('test1.xls')

wbk1 = xlrd.open_workbook('test1.xls')
table = wbk1.sheets()[0]
print table.nrows
print table.ncols


wbks = copy(wbk1)
sheet = wbk.get_sheet('sheet 1')

sheet.write(2,1,'test 1')
sheet.write(3,1,'test 1')

wbk.save('test1.xls')
wbk1 = xlrd.open_workbook('test1.xls')
table = wbk1.sheets()[0]
print table.nrows
print table.ncols
