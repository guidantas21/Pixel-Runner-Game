# Pixel Runner Verison 1.0: Simple game using Pygame

## Project Overview
1. Concept
    - Pixel Runner is a game which the player needs to dodge the obstacles to stay alive, the longer the player stays alive, the higher his score, very similar to the Google dinossaur game. The main goal of this project is to exercise the implementation of basic concepts of object-oriented programming, such as inheritance, this way I build all the game based on classes, there's a class for the level, player, obstacles and for the game logic.

2. Technology
    - All the game was built in Python, using Pygame, this amazing module is great for building 2D games. The performance is not quite the best (for simple games it doesn't really matter), in constrast the practicality is great, easy syntax and many features that can make the building process very programmer friendly and joyful.

3. Implememtation
    - Level
        - This game only has one level, which has background surface and a ground surface (surface = image)
        - The level also stores some position information to indicate the hight of the ground and where the player and obstacles should spawn and the background music

    - Player
        - Sprite Class
            - It's a class that inherits from the Pygame Sprite class, providing some prebuilt functionalities for sprites
            - A sprite has a image (surface that changes coording to the animation state) and rect (kinda like a hit box)
        - Gravity
            - To simulate gravity, every frame the y position of the pl
        - Movement
            - Jump
        - Animation
            - Walking animation
                - There is a list of images of the player walking
                - 
        - Update

    - Obstacle
        - Sprite Class
            - It's a class that inherits from the Pygame Sprite class, providing some prebuilt functionalities for sprites
            - A sprite has a image (surface that changes coording to the animation state) and rect (kinda like a hit box)
        - Types of Obstacle
            - Fly
            - Snail
        - Movement
        - Animation 
        - Update

    - Game
        - 


4. New features ideas

## How to run the game
1. Install the [Python Interpreter](https://www.python.org/downloads/)
2. Install the Pygame Library
    - Command: ```pip install pygame```

## How to play Pixel Runner
1. Press the SPACE key to start the game
2. Press the SPACE key to make the player jump to dodge the snails and flies, if you ccollide into these obstacles it's game over
3. Press the SPACE key to try again

## References
- This project is my version of an amazing tutorial that taught me the basics of pygame, link bellow:
>https://www.youtube.com/watch?v=AY9MnQ4x3zk

- [Pygame Documentation](https://www.pygame.org/docs/) 

