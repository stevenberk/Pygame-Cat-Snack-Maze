# pygame

The objective of this maze is to move the slice of cake with the arrow keys to the nyancat without touching the maze walls. The game looks simple and straightforward but in practice, but it is very difficult to win. There are invisible "speed traps" throughout the maze. These speed traps are the same color as the background (to make them invisible to the user). The speed traps increase the amount of pixels the sprite moves with each arrowkey event.


Here's an image of the normal game screen, the speed traps are hidden to the user
![alt text](https://github.com/stevenberk/pygame/blob/master/images/mazeHiddenSpeedTraps.jpg)

This is an image of the game screen with the speed traps made visible, whenever the user moves the slice of cake over a speed trap, the "speed" of the arrow keys increases by one(number of pixels moved per second the arrow key is pressed, simulating an increase in arrowkey sensitivity). This only occurs once per speed trap, no additional increases in speed will occur if the user sits on the speed trap or crosses the same speed trap multiple times. The series of speed traps in the gap at the bottom of the maze will increase the speed of the slice of cake to the point where it is nearly impossible to control.
![alt text](https://github.com/stevenberk/pygame/blob/master/images/mazeWithSpeedTraps.jpg)

