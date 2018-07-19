#!/bin/bash

function git_push() {
#	git checkout Leepi_MTK_RC3
#	git branch -D iAuto_Android_POC
#	git checkout iAuto_Android_POC
#	git cherry-pick Leepi_MTK_RC3

	git push aosp HEAD:refs/for/iAuto_Android_POC
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
