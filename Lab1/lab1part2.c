#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
	
int main(){
	int i = 15;     	 	// counter for number of times to create a process
	int parentFork = fork();	// intial fork, parent and first child
	int childFork = 0;
	waitpid(-1, NULL, 0);
	if(parentFork != 0){
		printf("I'm the PARENT with pid: %d \n", getpid()); // parent print
	}
	else if(parentFork == 0){ 			// allows child to go through
		while(i > 0 && childFork == 0){		// uses the child of the most recent fork to create the next fork, 1 creates 2, 2 makes 3, and so on
			childFork = fork();
			--i;
		}
		printf("I'm the CHILD with pid: %d and ppid: %d \n", getpid(), getppid()); // child print
		waitpid(-1, NULL, 0);
	}
	return 0;
}
// tested using gcc, each child process creates one new child process after the initial fork creating the first child until 16 children in total are created
