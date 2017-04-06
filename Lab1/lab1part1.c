#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h> 

int main (){ 
	char userInput[25];
	printf("To terminate, type 'exit' otherwise enter a basic command to continue: ");
	scanf("%s", userInput); // prompts user and then awaits their input

	if(strcmp(userInput, "exit") != 0){ // makes sure the user did not request to exit
		int pid = fork(); 	    // fork occurs and return value stored in pid
		if(pid  == 0){		    // child process code
			system(userInput);  // child process runs the user input command
		}
		else{			    // parent process code
			waitpid( pid, NULL, 0);
			system(userInput);  // parent process runs the user input command
		}	
		return 0;
	}
	else{
		exit(0);
	}
}
// tested using gcc compiler, entered the 'ls' command and it was executed twice, once by the parent and once by the child
