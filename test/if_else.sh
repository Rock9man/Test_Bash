#!/bin/bash

scp ttttt wj@172.26.189.85:~
if [ $? -eq 0 ];then
	echo "succeed"
else
	echo "faild"
fi
