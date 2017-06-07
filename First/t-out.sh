#!/bin/bash
# t-out.sh
# editor : wangjun
# time:2017年 03月 06日 星期一 09:28:04 CST

# 从"syngin seven" 的建议中得到灵感。

TIMELIMIT=4			# 4秒

read -t $TIMELIMIT variable <&1
#
# 在这儿，Bash 1.x and 2.x 需要"<&1",
# 但是Bash 3.x则不需要.

echo

if [ -z "$variable" ]	#值为NULL？
then
	echo "Timed out, variable still unset."
else
	echo "variable = $variable"
fi

exit 0
