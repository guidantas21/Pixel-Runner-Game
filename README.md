# Pixel Runner Verison 1.0: Simple game using Pygame

## THIS DOCUMENTATION IS NOT COMPLETE YET

## Project Overview
1. Concept
    - Pixel Runner is a game which the player needs to dodge the obstacles to stay alive, the longer the player stays alive, the higher his score, very similar to the Google dinossaur game. The main goal of this project is to exercise the implementation of basic concepts of object-oriented programming, such as inheritance, this way I build all the game based on classes, there's a class for the level, player, obstacles and for the game logic.

2. Technology
    - All the game was built in Python, using Pygame, this amazing module is great for building 2D games. The performance is not quite the best (for simple games it doesn't really matter), in constrast the practicality is great, easy syntax and many features that can make the building process very programmer friendly and joyful.

3. Implementation
    - Level
        - This game only has one level, which has background surface and a ground surface (surface = image).
        - The level also stores some position information to indicate the hight of the ground and where the player and obstacles should spawn and the background music.

    - Player
        - Sprite Class
            - It's a class that inherits from the Pygame Sprite class, providing some prebuilt functionalities for sprites
            - A sprite has a image (surface that changes coording to the animation state) and rect (kinda like a hit box).

        - Gravity
            - If the player is not in the ground, the gravity increases by 1 and the player y postion increases by the gravity value in each frame, making the player fall back to the ground.

        - Movement
            - To simualte a jump, player's gravity = -20, then in each frame it's incresed by 1, this way the player jump speed will slow down until until gravity reaches 0, after that the player starts to fall until it reaches the ground.

        - Animation
            - The player has 2 animation states: walking and jumping
                - Jump animation: If the player jumping, the sprite image = image of player jumping
                - Walk animation: If the player is not jumping, is walking, so while the player is walking, the sprite image toggles between two walking surfaces (stored in the frames array) 

    - Obstacle
        - Sprite Class
            - It's a class that inherits from the Pygame Sprite class, providing some prebuilt functionalities for sprites
            - A sprite has a image (surface that changes coording to the animation state) and rect (kinda like a hit box)

        - Types of Obstacle
            - Snail and Fly -> both have their own surfaces and rects

        - Movement
            - The Obstacle moves in only one direction, so in each frame the x position is subtracted by the speed (making the obstacle go foward <-) until it is not visible (in this case the obstacle is deleted) 

        - Animation
            - The Obstacle is constantly switching between two surfaces (stored in the frames array), giving an impression of movement 

    - Game
        - This part of the code is related to the pygame setup, the game logic and and most of the graph rendering

        - User events
            - Obstacle spawn timer: Every 1500ms, one obstcale is spawned

        - Spawn obstacles
            - Add a new Obstacle object to the obstacle sprite group
            - 66% snail Obstacle and 33% fly Obstacle

        - Game state
            - While user is playing the game, the game is active
            - if the player dies the game is no longer active, until the user starts a new game

        - Event loop
            - Checks if the user quit the game
            - If the game is active, check if the obstacle timer was triggered
            - If the game is not active, check if the the SPACE key was pressed (start new game) 

        - Check sprite collision
            - Return True if the player sprite collided in any obstacle of the obstacle sprute group

        - Player score
            - The score is basically how much time the player survives
            - Score: 48 = 4,8 seconds

        - Draw elements
            - When game is active
                - Display the level, the player, the obstacles and the score counter
            - When game is not active
                - Display the game intro
                    - Game title, game image and the message to start running
                - Display game over 
                    - Game over message, game image, final score


4. New features ideas
    - Comming soon...

## How to run the game
1. Install the [Python Interpreter](https://www.python.org/downloads/)
2. Install the Pygame Library
    - Command: ```pip install pygame```
3. Download the source code
4. Execute the main.py file
    - Command: ```python main.py```

## How to play Pixel Runner
1. Press the SPACE key to start the game
2. Press the SPACE key to make the player jump to dodge the snails and flies, if you ccollide into these obstacles it's game over
3. Press the SPACE key to try again

## References
- This project is my version of an amazing tutorial that taught me the basics of pygame, link bellow:
>https://www.youtube.com/watch?v=AY9MnQ4x3zk

- [Pygame Documentation](https://www.pygame.org/docs/) 

