# pygame

My first Pygame project. The objective of this maze is to move the slice of cake with the arrow keys to the nyancat without touching the maze walls. 
Additionally, I wanted the game to look simple and straightforward but in practice was very difficult to win. I did this by creating "speed traps" throughout the maze. These speed traps are the same color as the background (to make them invisible to the user). The speed traps increase the amount of pixels the sprite moves with each arrowkey event.


Here's an image of the normal game screen, the speed traps are hidden to the user
![alt text](https://github.com/stevenberk/pygame/blob/master/images/mazeHiddenSpeedTraps.jpg)

This is an image of the game screen with the speed traps made visible, whenever the user moves the slice of cake over a speed trap, the "speed" of the arrow keys increases by one(number of pixels moved per second the arrow key is pressed, simulating an increase in arrowkey sensitivity). This only occurs once per speed trap, no additional increases in speed will occur if the user sits on the speed trap or crosses the same speed trap multiple times.
![alt text](https://github.com/stevenberk/pygame/blob/master/images/mazeWithSpeedTraps.jpg)

