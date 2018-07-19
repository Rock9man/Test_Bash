#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
	pid_t pid;

	pid = fork();

	if (pid < 0)
	{
		printf("fork failed!\n");
		exit(1);
	}

	if (pid == 0) {
		printf("This is the child, child pid = %d\n",getpid());
		pid = fork();
		if (pid < 0)
		{
			printf("fork failed!\n");
			exit(1);
		}
		if (pid == 0){
			printf("This is the childA, child pid = %d\n",getpid());
		}else{
	
			
			printf("This is the childB, child pid = %d\n",getpid());
		}
		sleep(15);
	} else {
		
		printf("This is the parent, child pid = %d, parent pid = %d\n", pid, getpid());	
		sleep(15);
	}

	return 0;
}