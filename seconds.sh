#!/bin/bash
# seconds.sh
# 脚本运行多长时间了
# time :2017年 03月 04日 星期六 19:34:42 CST
# editor: wangjun4

TIME_LIMIT=10
INTERVAL=1

echo
echo "Hit Control-C to exit before $TIME_LIMIT seconds。"
echo

while [ "$SECONDS" -le "$TIME_LIMIT" ]
do
	if [ "$SECONDS" -eq 1 ]
	then
		units=second
	else
		units=seconds
	fi

	echo "This script has been running $SECONDS $units."
	# 	在一个缓慢或者负担过重的机器上，
	#	脚本可能偶尔会跳过一个计数，
	sleep $INTERVAL
done

echo -e "\a" # Beep!(BB声)

exit 0
