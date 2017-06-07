#!/bin/bash
# timeout.sh

# editor: wangjun
# time:2017年 03月 04日 星期六 15:25:08 CST

INTERVAL=5

timedout_read() {
	timeout=$1
	varname=$2
	old_tty_settings='stty -g'
	stty -icanon min 0 time ${timeout}0
	eval read $varname		# 或只读$varname变量
	stty "$old_tty_settings"
}

echo;
echo -n "What's your name? Quick!"
timedout_read $INTERVAL wangjun

echo

if [ ! -z "$your_name"]
then
	echo "Your name is $your_name."
else
	echo "Timed out."
fi

echo

exit 0
