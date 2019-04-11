#!/usr/bin/env python

import os, string, sys


def main(argv):
	if len(argv) !=2:
		print("argv number error")
		return
	rootdir = argv[1]
	for root, dirs, files in os.walk(rootdir):
		print("%s %d" % (root,os.path.getsize(root)))
		for file in files:
			path = os.path.join(root,file)
			if os.path.islink(path):
				print("%s %d" % (path,7))
			else:
				print("%s %d" % (path,os.path.getsize(path)))

if __name__ == '__main__':
	main(sys.argv)
