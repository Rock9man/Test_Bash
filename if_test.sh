#!/bin/bash

# 小技巧：
# 如果你不能确定一个特定条件该如何判断，
#+ 那么就使用if-test结构

echo

echo "Testing \"0\""
if [ 0 ]	#zero
then
	echo "0 is true."
else
	echo "0 is false."
fi		#0 为真

echo

echo  "Testing \"1\""
if [ 1 ]	# one
then 
	echo "1 is true."
else
	echo "1 is false."
fi 		# 1 为真

echo

echo "Testing \"-1\""
if [ -1 ]	# 负1
then
	echo " -1 is ture."
else
	echo " -1 is false."
fi		# -1 为真

echo

echo "Testing \"NULL\""
if [ ]		# NULL (空状态）
then
	echo "NULL is true."
else
	echo "NULL is false."
fi		# NULL 为假。

echo

echo "Testing \"xyz\""
if [ xyz ]	# 字符串
then
	echo "Random string is true."
else
	echo "Random string is false."
fi 		# 随便的字符串
