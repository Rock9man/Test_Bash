#!/bin/bash

#作为用例，调用这个脚本至少需要10个参数，比如：
#./scriptname 1 2 3 4 5 6 7 8 9 10
MAINPARAMS=10

echo

echo "The name of this script is \"$0\"."
# 添加./是表示当前目录
echo "The name of this script is \"'basename $0'\"."
# 去掉路径名，剩下文件名，（参见‘basename’）

echo

if [ -n "$1" ]				#测试变量被引用
then
	echo "parameter #1 is $1"		#需要引用才能够转义“#”
fi

if [ -n "$2" ]
then
	echo "Parameter #2 is $2"
fi


