#!/usr/bin/env python

import os, string, sys
import xlwt, xlrd
from xlutils.copy import copy

datamap={}
cputotal=0


Head_list = ['name','max','min','average']

cpuinfo_list = [ 0,0 ]

keys = ['CPU0:','CPU1:','CPU2:','0:','1:','2:','3:','4:','5:','6:','7:','bandwidth','CPUfreq0','CPUfreq1','CPUfreq2','CPUTOTAL','CPU3:','CPU4:','CPU5:','CPUfreq3','CPUfreq4','CPUfreq5']

def open_write_xls(output_file):
	output_wbk = xlwt.Workbook(output_file)
	return output_wbk

def open_read_xls(input_file):
	input_wbk = xlrd.open_workbook(input_file)
	return input_wbk

def write_sheet(sheet):
	j = 1
	i = 0
	for head in Head_list:
		sheet.write(0,i,head)
		i = i + 1
	for key in keys:
		values = list(datamap[key])
		lens = len(values)
		sheet.write(j,0,key)
		sheet.write(j,1,max(values))
		sheet.write(j,2,min(values))
		sheet.write(j,3,sum(values)/lens)
		i = 0
		while ( i < lens ):
			num = 4 + i
			sheet.write(j,num,values[i])
			i = i + 1
		j = j + 1

def functions(inputdata):
	global datamap
	global cpuinfo_list
	global cputotal
	if "MB/s" in inputdata:
		if "Total bandwidth" in inputdata:
			datamap.setdefault("bandwidth",[]).append(int(inputdata.split()[3]))
		elif "Port" in inputdata:
			datamap.setdefault(str(inputdata.split()[1]),[]).append(int(inputdata.split()[2]))
			datamap.setdefault(str(inputdata.split()[5]),[]).append(int(inputdata.split()[6]))
	elif "idle" in inputdata:
		datamap.setdefault(str(inputdata.split()[0]),[]).append((100-float(inputdata.split()[7][:-1])))
		if "CPU0" in inputdata:
			cputotal=0
			cputotal=100-float(inputdata.split()[7][:-1])
		elif "CPU1" in inputdata:
			cputotal=cputotal + (100-float(inputdata.split()[7][:-1]))
		elif "CPU2" in inputdata:
			cputotal=cputotal + (100-float(inputdata.split()[7][:-1]))
		elif "CPU3" in inputdata:
			cputotal=cputotal + (100-float(inputdata.split()[7][:-1]))
		elif "CPU4" in inputdata:
			cputotal=cputotal + (100-float(inputdata.split()[7][:-1]))
		elif "CPU5" in inputdata:
			cputotal=cputotal + (100-float(inputdata.split()[7][:-1]))
			print cputotal
			datamap.setdefault('CPUTOTAL',[]).append((cputotal/6))
	elif "max and min" in inputdata:
		cpuinfo_list = [ 0,0 ]
	elif "CPU 0 info" in inputdata:
		cpuinfo_list = [ 0,16 ]
	elif "CPU 1 info" in inputdata:
		cpuinfo_list = [ 1,16 ]
	elif "CPU 2 info" in inputdata:
		cpuinfo_list = [ 2,16 ]
	elif "CPU 3 info" in inputdata:
		cpuinfo_list = [ 3,16 ]
	elif "CPU 4 info" in inputdata:
		cpuinfo_list = [ 4,16 ]
	elif "CPU 5 info" in inputdata:
		cpuinfo_list = [ 5,16 ]
	elif cpuinfo_list[1] > 0:
		if cpuinfo_list[1]%4 == 3:
			print inputdata
			datamap.setdefault("CPUfreq"+str(cpuinfo_list[0]),[]).append(int(inputdata[:-5]))
		cpuinfo_list[1] = cpuinfo_list[1] - 1

def main(argv):
	if len(argv) != 4:
		print("argv number error ")
		return
	global datamap
	input_file =argv[1]
	data = open_read_xls(input_file)
	newdata = copy(data)
	start = int(argv[2])
	end = int(argv[3])
	while( start <= end ):
		datamap = {}
		print start
		old_sheet = data.sheets()[start]
		new_sheet = newdata.get_sheet(start)
		lines = old_sheet.col_values(0, start_rowx=0, end_rowx=None)
		for line in lines:
			functions(str(line))
		write_sheet(new_sheet)
		start = start + 1
	newdata.save(input_file)

if __name__ == '__main__':
	main(sys.argv)
