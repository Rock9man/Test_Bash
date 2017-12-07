function add_patch()
{

if [ $# -ne 4 ];then
	echo "addpatch.sh , args error!"
	echo "eg: add_patch androidN_dir androidO_dir androidN MerbokO"
	exit 1
fi

if [ -z $1 ];then
	echo "running error! args 1 in none"
	exit 1
else
	local project_dir_one=$1
fi

if [ -z $2 ];then
	echo "running error! args 2 in none"
	exit 1
else
	local project_dir_two=$2
fi

if [ -z $3 ];then
	echo "running error! args 3 in none"
	exit 1
else
	local base_branch=$3
fi

if [ -z $4 ];then
	echo "running error! args 4 in none"
	exit 1
else
	local object_branch=$4
fi

if [ ! -d $project_dir_one ];then
	echo "error! $project_dir_one isn't exit!"
	exit 1
fi

if [ ! -d $project_dir_two ];then
	echo "error! $project_dir_two isn't exit!"
	exit 1
fi
dir=`pwd`

cd $project_dir_one

git pull

git checkout $object_branch

git checkout $base_branch

git format-patch -M $object_branch -o patch

cd $dir

cd $project_dir_two

git pull

git checkout $object_branch

git am --abort

git am $project_dir_one/patch/*.patch


cd $project_dir_one

git clean -fdx

cd $dir

}
