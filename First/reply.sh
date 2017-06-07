#!/bin/bash
# reply.sh
# editor: wangjun
# time :2017年 03月 04日 星期六 16:08:54 CST

# REPLY 是一个read命令的默认变量

echo
echo -n "What is your favorite vegetable?"
read

echo "Your favorite vegetable is $REPLY."
# 如果没有变量提供切仅在这种情况，REPLY保存“read”命令上次读到的值
#

echo 
echo -n "What is favorite fruit?"
read fruit
echo "Your favorite fruit is $fruit."
echo "but..."
echo "Value of \$REPLY is still $REPLY."

echo

exit 0
