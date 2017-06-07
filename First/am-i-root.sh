#!/bin/bash
# am-i-root.sh
# editor: wangjun
# time: 2017年 03月 06日 星期一 09:38:23 CST

ROOT_UID=0			#Root的$UID为0

if [ "$UID" -eq "$ROOT_UID" ]		#真正的“root”才能经得住考验
then
	echo "You are root."
else
	echo "You are just an ordinary user (but mom loves you just the same)."
fi

echo "#######################################################"

ROOTUSER_ROOT=root

username=`id -nu`			# 或者... username='whoami'
if [ "$username" = "$ROOTUSER_ROOT" ]
then
	echo "Rooty,toot,toot. you are root."
else
	echo "You are just a regular fella."
fi
exit 0
