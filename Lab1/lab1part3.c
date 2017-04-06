#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int menageAFork(); // a function in which a parent process creates two children processes using fork on only the parent
int clusterFork(); // a function in which a parent process creates three children processes using fork on only the parent

int main(){
	int first = menageAFork();		 // initial process creates two children
	int second, third, fourth;		 // variables for future forks to store returns to
	waitpid(-1, NULL, 0);			 // CHILD TOTAL: 2
	if(first == 2){   			 // chooses the second child of the first fork
		second = menageAFork(); 	 // that process creates two more children
	}					 // CHILD TOTAL: 4
	waitpid(-1, NULL, 0);
	if(second == 2){			 // chooses the second child of the most recent fork
		third = clusterFork();		 // that process creates three more children 
	}					 // CHILD TOTAL: 7
	waitpid(-1, NULL, 0);
	if(third == 2){				 // chooses the third child of the most recent fork
		fourth = clusterFork();  	 // that process creates 3 more children
	} 					 // CHILD TOTAL: 10
	waitpid(-1, NULL, 0);
	if(fourth > 1 && fourth < 5){ 		 // cluster fork children return 2, 3, and 4, this allows all children from the last cluster to pass
		clusterFork();	
		waitpid(-1, NULL, 0);		 // all children(3) from the last fork create 3 more children
	}					 // CHILD TOTAL: 19
	waitpid(-1, NULL, 0);
}

// Tested by running through gcc compiler, since every creating process and child process prints its PID and PPID, just counted to make sure
// there were 19 processes. The no more than 3 no less than 2 criteria for parent processes was also confimred through this test, and 
// should be apparent through the menageAFork and clusterFork functions, in which a parent process creates 2 or 3 children respectively



int menageAFork(){
	int a = fork();		 // initial fork and return stored to distinguish parent from child
	if(a != 0){ 		 // makes sure only the parent process will create future children   
		int b = fork();  // parent process forks again, creating a second child
		if(b != 0){      
			printf("Parent with PID: %d \n", getpid()); // creating process states its a parent
			waitpid(-1, NULL, 0);
			return 1;
		}
		else{
			printf("Child with PID: %d and PPID: %d \n", getpid(), getppid()); // second child 
			return 2;
		}
		waitpid(-1, NULL, 0);
	}
	else{
		printf("Child with PID: %d and PPID: %d \n", getpid(), getppid()); // first child
		return 3;
	}
}

int clusterFork(){
	int a = fork();          // initial fork and return stored to distinguish parent from child 
        if(a != 0){ 		 // makes sure only the parent process will create future children
                int b = fork();  // parent process forks, first child 1 does not
                if(b != 0){      // makes sure parent forks but child 2 does not
			int c = fork();  	// parent forks to create child 3
			if(c != 0){
                        	printf("Parent with PID: %d \n", getpid()); // creating process states its a parent 
				waitpid(-1, NULL, 0);
                        	return 1;
			}
			else{
				printf("Child with PID: %d and PPID: %d \n", getpid(), getppid()); // third child
				waitpid(-1, NULL, 0);
                        	return 2;	
			}
		}
                else{
                        printf("Child with PID: %d and PPID: %d \n", getpid(), getppid()); // second child
                	waitpid(-1, NULL, 0);
                        return 3;
                }
        }
        else{
                printf("Child with PID: %d and PPID: %d \n", getpid(), getppid()); // first child
		waitpid(-1, NULL, 0);
                return 4;
        }
}
