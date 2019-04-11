#!/bin/bash

function git_push() {
	remote="ssh://gerrit.iauto.com:29418/Src/renesas/android/$1"
	echo $remote
	git remote add iremote $remote
#	git checkout -b renesas/android-8.1.0_r41
	git push iremote -o skip-validation HEAD:renesas/android-8.1.0_r41
#	git init
#	git add --all
#	git commit -m "[PF] init add RENESAS BSP 07E file"
#	git branch -D iAuto_Android_POC
#	git checkout iAuto_Android_POC
#	git cherry-pick Leepi_MTK_RC3

#	git push aosp HEAD:refs/for/iAuto_Android_POC
}
function read_dir(){
	cd $1
	for file in `cat git_new.git`
	do
		cd $file
		git_push $file 
		cd -
	done
}

read_dir $1
