#!/usr/bin/env python

import os, string, sys
import xlwt, xlrd
from xlwt import Workbook

Head_list = ['dir','add','sub','total']

def is_num_by_except(num):
	try:
		int(num)
		return True
	except ValueError:
		return False

def open_write_xls(output_file):
	output_wbt = xlwt.Workbook(output_file)
	return output_wbt

def main(argv):
	if len(argv) !=4:
		print("argv number error")
		return

	local = os.getcwd()
	oldfile = argv[1]
	basebranch = argv[2]
	objbranch = argv[3]
	shcommand = "git log "+ basebranch + ".." + objbranch + " --pretty=tformat: --numstat"
	filelist = open(oldfile,'r')
	objfile = oldfile + ".xls"
	wbt = Workbook(encoding='utf-8')
	sheet = wbt.add_sheet("dirlines")
	i = 0
	j = 0
	for Head in Head_list:
		sheet.write(j,i,Head)
		i = i + 1
	for subdir in filelist:		
		j = j + 1
		subdir = subdir.strip("\n")
		os.chdir(subdir)
		os.system("git pull")
		os.system("git checkout " + basebranch)
		os.system("git checkout " + objbranch)
		retu = os.popen(shcommand)
		test = retu.read()
		print test
		add = 0
		sub = 0
		total = 0
		for line in test.splitlines():
			line = line.split()
			if len(line) == 3:
				if is_num_by_except(line[0]):
					add = add + int(line[0])
				if is_num_by_except(line[1]):
					sub = sub + int(line[1])
					total = total + int(line[0]) + int(line[1])
		sheet.write(j,0,subdir)
		sheet.write(j,1,add)
		sheet.write(j,2,sub)
		sheet.write(j,3,total)
		os.chdir(local)
	wbt.save(objfile)

if __name__ == '__main__':
	main(sys.argv)
