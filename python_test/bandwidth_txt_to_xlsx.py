#!/usr/bin/env python

import os, string, sys

datamap={}

keys = ['0:','1:','2:','3:','4:','5:','6:','7:','bandwidth']

def write_file(outdata):
	global datamap
#	print(datamap)
	for key in keys:
		values = list(datamap[key])
		print(max(values))
		print(sum(values)/len(values))
		print(values)

def read_file(inputdata):
	f = file(inputdata)
	text = f.readlines()
	f.close()
	return text

def functions(inputdata):
	global datamap
	if "MB/s" in inputdata:
		if "Total bandwidth" in inputdata:
			datamap.setdefault("bandwidth",[]).append(int(inputdata.split()[3]))
		elif "Port" in inputdata:
			datamap.setdefault(str(inputdata.split()[1]),[]).append(int(inputdata.split()[2]))
			datamap.setdefault(str(inputdata.split()[5]),[]).append(int(inputdata.split()[6]))

def main(argv):
	if len(argv) != 5:
		print("argv number error ")
	global datamap
	inputs =argv[1]
	outputs = argv[2]
	options = argv[3:]
	text = read_file(inputs)
	for line in text:
		functions(line)
	write_file(datamap)

if __name__ == '__main__':
	main(sys.argv)
