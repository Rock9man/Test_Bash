#!/bin/bash

function git_commit() {
	git pull
	git status
	git add --all
	git commit -m '[Title] delete other lunch

[Module] lunch
[Type] modify
[Content]
	1) rename vendorsetup.sh to vendorsetup.sh.tmp
	2) iredmine number:506715'

	git show -1
	git pull
	git status
}

function git_push() {
	git show -1
	git push origin HEAD:refs/for/iautoandroid/master
}
function read_dir(){
	cd $1
	for file in `find -name vendorsetup.sh.tmp`
	do
		subdir=${file%/*}
		cd $subdir
		echo `pwd`
	#	git_commit
		git_push 
		cd -
		echo `pwd`
	done
}

read_dir $1
