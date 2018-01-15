#!/bin/bash

function git_push() {
	git add --all
	git commit -m "[biuld][wangjun4] vendorsetup.sh to vendorsetup.sh.tmp " 
	git push MerbokO HEAD
}
function read_dir(){
	cd $1
	for file in `find -name vendorsetup.sh.tmp`
	do
		subdir=${file%/*}
		cd $subdir
		echo `pwd`
		git_push 
		cd -
		echo `pwd`
	done
}

read_dir $1
