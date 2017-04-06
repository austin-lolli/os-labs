#!/usr/bin/python
############################################################################################
############################################################################################
##   ___                                               __                                 ##
##  |   \     _    _ _____ _______ _______ ___    _   |  |     ____  _     _     _______  ##
##  | |\ \   | |  | |  ___|__   __|__   __|   \  | |  |  |    /  _  | |   | |   |__   __| ##
##  | | \ \  | |  | | |___   | |     | |  | |\ \ | |  |  |    | | | | |   | |      | |    ##
##  | |__\ \ | |  | |___  |  | |     | |  | | \ \| |  |  |    | | | | |   | |      | |    ##
##  |  __   \| \__/ |___| |  | |   __| |__| |  \   |  |  |____| |_| | |___| |______| |__  ##
##  |_|   \ _\\____/|_____|  |_|  |_______|_|   \__|  |_______\_____|_____|_____|_______| ##
##                                                                   			  ##
##				    Santa Clara University                                ##                  
##					COEN 177 Lab 3                                    ##
##                                          LRU.py                                        ##
##                             Tested on Python 2.7.10 and 2.6.x                          ##
##                                                                                        ##
############################################################################################
############################################################################################

def update_recent(frames, x, val):
	y = len(frames)
	while(x < y):
		frames[x] = frames.get(x+1, -1)
		if(frames[x] == -1):
			break
		else:
			x = x + 1
	frames[x] = val

def new_entry(frames, x, val):		
	frames[x] = val

import sys

pageframe = {}			
pnum = 0			
requests = 0			
faults = 0			
data = [] 			# array of incoming page table requests 
pages = int(sys.argv[1])	# number of pages available, set by the user	
limit = pages + 1    		# set for a later loop
	
for line in sys.stdin:
        d = line.rstrip('\n')
        if(d.isdigit):
                data.append(d)

for i in range (0, len(data)):
#	if(data[i].isdigit()):					# ignores all nondigit entries by just skipping to next entry
		pnum = data[i]						# the current page number gets set
		requests = requests + 1					# incriment the request counter
		for j in range (0, limit): 				# limit allows us to check if j == pages, aka need a replacement
			entry = pageframe.get(j, -1)
			if(j == pages):
				update_recent(pageframe, 0, pnum)	# deletes oldest entry (pageframe[0]),pushes all entries down, puts incoming at the top
				faults = faults + 1			# page fault occurs here, incriment the fault counter
				break
			elif(entry == -1):			
				new_entry(pageframe, j, pnum)		# pageframe not yet full, put entry in first found blank spot
				faults = faults + 1
				break
			elif(entry == pnum):
				update_recent(pageframe, j, pnum)	# deletes current entry (duplicate), pushes all entries in pageframe down, puts incoming at top
				break
			else:						# the current pageframe space is not empty, at the limit or equal to the incoming one
				continue				# meaning its a taken entry and we should move to the next one
		
print "Total requests: %d" % requests
print "Total faults: %d" % faults

