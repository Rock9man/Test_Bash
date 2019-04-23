#include <unistd.h>
#include <stdio.h>

#define OBJ_FILE "/proc/stat"
int main()
{

	char chars[2048];
	FILE* fp = fopen(OBJ_FILE,"r");
	for( int i = 0; i < 4; i++)
	{
		fgets(chars,2048,fp);
		printf("%s", chars);
		fgets(chars,2048,fp);
		printf("%s", chars);
		fgets(chars,2048,fp);
		printf("%s", chars);
		fgets(chars,2048,fp);
		printf("%s\n", chars);
		fseek(fp,0L,SEEK_SET);
		FILE* fp1 = fopen(OBJ_FILE,"r");
		fgets(chars,2048,fp1);
		printf("%s\n**************\n", chars);
	}

	return 0;
}
