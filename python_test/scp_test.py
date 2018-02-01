#!/usr/bin/env python

import socket
import os
import sys

def main(input_argv):
	LocalFileAddr=input_argv[1]
	print ("input_argv[1] is %s" % input_argv[1])
	LocalFileName=input_argv[2]
	print ("input_argv[2] is %s" % input_argv[2])
        ret=os.system('scp %s/%s addSha1@172.26.186.17:~' % (LocalFileAddr, LocalFileName))
        os.system('echo `sha1sum %s/%s`' % (LocalFileAddr, LocalFileName))
	print ("log scp local to remote ret is : %d" % ret)
        os.system('sync')


if __name__ == '__main__':
	main(sys.argv)
	sys.exit(0)
