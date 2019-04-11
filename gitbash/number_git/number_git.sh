#!/bin/bash

function git_push() {
#	git log --root --author=$1 --pretty=tformat: --numstat | gawk '{ add += $1 ; subs += $2 ; loc += $1 + $2 } END { printf "%s %s %s\n",add,subs,loc }'
	git log origin/Leepi_MTK_E2_Back..origin/leepi/master --author=$1 --pretty=tformat: --numstat | gawk '{ add += $1 ; subs += $2 ; loc += $1 + $2 } END { printf "%s %s %s\n",add,subs,loc }'
}
function read_dir(){
	cd $1
	for dirfile in `cat git_new.git`
	do
		cp auther_new.git $dirfile
		cd $dirfile
		pwd
		git pull
		for auther in `cat auther_new.git`
		do
			git_push $auther
		done
		rm auther_new.git
		cd -
	done
}

read_dir $1
