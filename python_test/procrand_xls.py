#!/usr/bin/env python

import os, string, sys
import xlrd, xlwt
from xlutils.copy import copy

key_value = {}

reload(sys)
sys.setdefaultencoding('utf-8')

heads = ['totle', 'Android', 'gaode', 'kuwo', 'xinwen', 'gupiao','tianqi','ximalaya', 'weixin', 'iAuto', 'auther']

def set_key_value(key):
	global key_value
	print "This \"" + str(key) + "\" not in key value list\n\n"
	print("Please select key %s value type :" % key )
	for number in range(1,len(heads)):
		print("%d : %s" % (number, heads[number]))
	value = input("number:")
	key_value.setdefault(str(key),[]).append(str(heads[value]))

def save_key_value(key_value_sheet):
	global key_value
	keys = key_value.keys()
	keys.sort()
	key_value = map(key_value.get, keys)
	for number in range(0,len(key_value)):
		print str(key_value[number])
#		key_value_sheet.write( number,0,str(key_value[number][0]))


def function_line(line):
	global key_value


def main(argv):
	input_file = argv[1]
	sheets = int(argv[2])
	sheetend = int(argv[3])
	wbt = xlrd.open_workbook(input_file)
	newwbt = copy(wbt)

	sheet2 = wbt.sheets()[-1]
	lines1 = sheet2.col_values(0, start_rowx=0, end_rowx=None)
	lines2 = sheet2.col_values(1, start_rowx=0, end_rowx=None)
	i = 0
	for line in lines1:
		key_value.setdefault(str(line),[]).append(str(lines2[i]))
		i = i + 1
	for sheetnum in range(sheets,sheetend):
		sheet = wbt.sheets()[sheetnum]
		lines = sheet.col_values(0, start_rowx=0, end_rowx=None)
		newsheet = newwbt.get_sheet(sheetnum)
		i = 0
		j = 0
		sumlist=[0,0,0,0,0,0,0,0,0,0]
		maxlist=[0,0,0,0,0,0,0,0,0,0]
		totlelist=[0,0,0,0,0,0,0,0,0,0]
		for k in range(0,10):
			newsheet.write( 1 + k, 0, heads[k])
		for line in lines:
			data = line.split()
			if "cmdline" not in line:
				if len(data) == 6 :
					newsheet.write(15 + i,int(j+0),int(data[3][:-1]))
					newsheet.write(15 + i,int(j+1),data[5])
					if key_value.get(data[5]) is None:
						set_key_value(data[5])
					newsheet.write(15 + i,int(j+2),key_value.get(data[5])[0])
					sumlist[0] = int(sumlist[0]) + int(data[3][:-1])
					if key_value.get(data[5])[0] in "Android":
						sumlist[1] = int(sumlist[1]) + int(data[3][:-1])
					elif key_value.get(data[5])[0] in "gaode":
						sumlist[2] = int(sumlist[2]) + int(data[3][:-1])
					elif key_value.get(data[5])[0] in "kuwo":
						sumlist[3] = int(sumlist[3]) + int(data[3][:-1])
					elif key_value.get(data[5])[0] in "xinwen":
						sumlist[4] = int(sumlist[4]) + int(data[3][:-1])
					elif key_value.get(data[5])[0] in "gupiao":
						sumlist[5] = int(sumlist[5]) + int(data[3][:-1])
					elif key_value.get(data[5])[0] in "tianqi":
						sumlist[6] = int(sumlist[6]) + int(data[3][:-1])
					elif key_value.get(data[5])[0] in "ximalaya":
						sumlist[7] = int(sumlist[7]) + int(data[3][:-1])
					elif key_value.get(data[5])[0] in "weixin":
						sumlist[8] = int(sumlist[8]) + int(data[3][:-1])
					elif key_value.get(data[5])[0] in "iAuto":
						sumlist[9] = int(sumlist[9]) + int(data[3][:-1])
					i = i + 1
				elif "TOTAL" in line:
					for k in range(0,10):
						newsheet.write( 1 + k, j/3+1, sumlist[k])
					for k in range(0,10):
						totlelist[k] = sumlist[k] + totlelist[k]
						if maxlist[k] < sumlist[k]:
							maxlist[k] = sumlist[k]
						sumlist[k] = 0
					i = 0
					j = j + 3
		newsheet.write( 0, 21, 'average')
		newsheet.write( 0, 22, 'max')
		for k in range(0,10):
			number = j /3
			newsheet.write( 1 + k, 21, totlelist[k]/number)
			newsheet.write( 1 + k, 22, maxlist[k])
	newmapsheet = newwbt.get_sheet(-1)
	save_key_value(newmapsheet)
	newwbt.save(input_file)


if __name__ == '__main__':
	main(sys.argv)
