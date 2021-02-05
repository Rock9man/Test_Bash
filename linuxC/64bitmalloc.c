#include<stdio.h>
#include<stdlib.h>

void* t64bytemalloc(int number){
	char* resp = NULL;
	char* ptr = (char *)malloc(number+64 + 4);
	unsigned long tempnum= ptr;
	resp = ptr + (68-tempnum%64);
	unsigned int* tmpbase = (int*)(resp-4);
	*tmpbase = ptr;
	printf("ptr = %p\n",ptr);
	printf("*tmpbase = %p\t tmpbase = %p\n",*tmpbase,tmpbase);
	printf("resp = %p\n",resp);
	printf("(resp-4) = %p \t *(resp-4)= %p\n",(resp-4),*(resp-4));
	free(ptr);
	return resp;
}

void t64bytefree(char* ptr){
	if(ptr != NULL)
		printf("ptr = %p",*(ptr-4));
		free(*(ptr-4));
}

int main()
{
	int num;
	char * ptr = NULL;
	while(1){
		printf("Plase input 64bit malloc test numberi(0 = exit):");
		if(num == 0)
			break;
		scanf("%d",&num);
		ptr = t64bytemalloc(num);
		//printf("ptr addr is %p \n",ptr);
		//t64bytefree(ptr);
		ptr = NULL;
	}
	return 0;
}

