#!/bin/bash
# timed-input.sh
# editor: wangjun
# time:2017年 03月 04日 星期六 19:59:22 CST

TIMELIMIT=3		#在这里边设置成三秒，但可以设置成其他值。

PrintAnswer()
{
	if [ "$answer" = TIMEOUT ]
	then
		echo $answer
	else
		echo "Your favorite veggie is $answer"
		kill $!		#不需要后台运行的TimerOn函数了，杀掉它
					# $!变量是上一个在后台运行的作业进程的PID
	fi
}

TimerOn()
{
	sleep $TIMELIMIT && kill -s 14 $$ &
	# 等3秒，然后给脚本发送sigalarm信号.
}

Int14Vector()
{
	answer="TIMEOUT"
	PrintAnswer
	exit 14
}

trap Int14Vector 14 	# 设置定时中断（14）能暗中给定时间限制

echo " What is your favorite vegetable "

TimerOn
read answer
PrintAnswer

