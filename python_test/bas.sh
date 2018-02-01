#!/usr/bin/bash
python scp_test.py /home/wangjun4/project1/test/bashdir/python_test scp_test.py
if [ $? == 1 ];then
	echo "python return is 1"
else
	exit 3
	echo "python return not is 1"
fi
