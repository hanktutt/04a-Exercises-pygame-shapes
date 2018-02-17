#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first two lines for you as an example


'''
import sys, pygame	# imports the sys and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

screen_size = (800,600) #It creates a variable for the window size of our program using a tuple
FPS = 60 #We create a variable Frames per Second that has a set number of 60

def main(): #We are creating a new function called main
	pygame.init() #a new command that initizalize all imported pygame modules
	screen = pygame.display.set_mode(screen_size) #a variable that sets the pygame screen to be our previouis variable screen_size
	clock = pygame.time.Clock()# create a variable clock that keeps track of the framerate of our pygame

	while True:#we create an infinite loop until it is set to False
		clock.tick(FPS)#This command keeps our cpu from running faster than the FPS we set earlier of 60.
		screen.fill((0,0,0))#This will fill the screen black

		for event in pygame.event.get():#create a set numbered loop for an event in PyGame
			if event.type == pygame.QUIT:#an if statement that says if the event is QUIT
				pygame.quit()#quit pygame if the event is QUIT
				sys.exit(0)#exit the system if the event is QUIT

		pygame.display.flip()#this will do something to your computers memory cauing it to print random colors in the pixels

if __name__ == '__main__':#the _name_ is a built in variable in python, and we sre setting it equivilant to our main function
	main()#this will run the main function