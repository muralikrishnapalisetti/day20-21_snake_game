# Snake Game – Day 20 & 21 of My 100 Days of Code Journey

This project is a fun milestone in my 100DaysOfCode challenge.
I recreated the classic Snake Game using Python and the built-in Turtle graphics module. 
It's a nostalgic throwback to the legendary Nokia 3310 days, but built with modern programming concepts.
The entire game was built over two focused days, with each part teaching me something new about Object-Oriented Programming and interactive graphics in Python.


## What I Built

### Day 20 – Building the Core Snake Functionality
- ✔️ Designed the initial snake using 3 square segments
- ✔️ Got the snake to move forward smoothly on its own
- ✔️ Connected keyboard controls to steer the snake using arrow keys

### Day 21 – Making It a Real Game
- ✔️ Added food that randomly appears and disappears when eaten
- ✔️ Increased the snake’s length and updated the score when food is eaten
- ✔️ Implemented collision with the wall (which ends the game)
- ✔️ Added logic to detect when the snake runs into itself (also ends the game)



## Concepts and Skills I Practiced

- **Object-Oriented Programming (OOP):**  
  Broke down the game into manageable parts using classes like `Snake`, `Food`, and `Scoreboard`.

- **Turtle Module:**  
  Used Python’s Turtle module to draw graphics and update visuals in real time.

- **Real-Time Input Handling:**  
  Mapped the arrow keys to control snake direction using `onkey()` and `listen()`.

- **Collision Detection:**  
  Calculated distances between objects to detect interactions with food, walls, and the snake’s own body.

- **Game Loop Logic:**  
  Created a loop that runs the game continuously and stops when a losing condition is met.


## How to Play the Game

1. Run the `main.py` file.
2. Use the arrow keys to control the direction of the snake:
   - Up Arrow → Move Up  
   - Down Arrow → Move Down  
   - Left Arrow → Move Left  
   - Right Arrow → Move Right
3. Try to collect as much food as possible.
4. Avoid crashing into the walls or into yourself—if you do, it’s game over!


## Why I Loved This Project

This game brought back some great memories from childhood. 
But more than that, it taught me how to turn logic into visuals, write clean OOP code, and handle real-time interaction in Python.
I learned how to structure a game from scratch and deal with continuous state changes—skills that are useful in many areas of programming.


