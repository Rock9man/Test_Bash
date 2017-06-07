#!/bin/bash
#@ Author: wangjun

function help()
{
    echo "##########################################################"
    echo "Please input bash Selectfile_String.sh filename findstring"
    echo "##########################################################"
}
if [ $# -ne 2 ];then
    help
    exit 1
fi
FileName=$1
FindString=$2
echo "$FileName"
cat $FileName | while read LINE
do
echo "$LINE" | grep -q "$FindString"
if [ $? -eq 0 ];then
    echo "$LINE" >> new$FileName
fi
done

