#!/bin/bash
# timeout_read.sh
# time:2017年 03月 04日 星期六 19:50:19 CST
# editor: wangjun

TMOUT=3			# 提示输入时间为三秒.\

echo "What is your favorate song?"
echo "Quickly now,you only have $TMOUT seconds to answer!"
read song

if [ -z "$song" ]
then
	song="(no answer)"
	# 默认输出
fi

echo "Your favorite song is $song."

exit 0
