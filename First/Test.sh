#!/bin/bash
# editor: wangjun4
# times: 2017/03/04

echo ${BASH_ENV}

echo 'pwd'


for n in 0 1 2 3 4 5
do
	echo "BASH_VERSINF[$n] = ${BASH_VERINFO[$n]}"
done
