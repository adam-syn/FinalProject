# Proposal

## What will (likely) be the title of your project?

Doodle Jump Simulator

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

This project will recreate the popular mobile game Doodle Jump, where players control a character that jumps from platform to platform while avoiding obstacles and enemies.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

Doodle Jump Simulator will replicate the mechanics of the classic mobile game in a 2D environment. 
The player will control a character that automatically jumps from platform to platform, and the goal is to achieve the highest possible score without falling off the screen or being hit by enemies.
The game will feature dynamic platform generation, where platforms appear at different heights and distances, some of which may disappear after being landed on. There will also be various power-ups like springs or jetpacks to aid the player. The enemies will include flying monsters that move along the screen, adding a challenge. Players will have the option to adjust difficulty, including changing platform speed, enemy behavior, and the frequency of power-ups. A scoring system, along with game-over and restart mechanisms, will be included. 
The game will be developed using a 2D graphics engine like Pygame, and it will be playable as a standalone desktop application.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

TODO, if applicable

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

TODO, if applicable

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

A functional version of Doodle Jump where the player can control the character, jump between platforms, and avoid obstacles, with basic scoring and game-over mechanics in place.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

A more complete version of Doodle Jump with multiple platform types, a variety of enemies with basic AI, a scoring system, and customizable difficulty levels for platform speed and enemy frequency.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

An advanced version of Doodle Jump with fluid animations, diverse enemy behaviors, power-ups, optimized gameplay mechanics, a high-score leaderboard, and smooth sound effects integrated into the game.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

The first step will be learning how to develop a basic 2D platformer using Pygame, focusing on handling user input for character movement and platform generation. Key tasks include implementing gravity, 
character jumping mechanics, and collision detection with platforms and obstacles. Additionally, I will need to research how to generate random platforms and control their speed, as well as how to design enemies 
that move and interact with the player. If collaborating, one teammate could focus on developing the platform and character mechanics, while another could handle the AI and enemy behaviors. Another teammate might focus on integrating sound effects, animations, and implementing the scoring and high-score system.

PROGRESS REPORT

  # Status Report

#### Your name

Adam Khan

#### Your section leader's name

Adam Khan

#### Project title

Doodle Jump Simulator

***

Short answers for the below questions suffice. If you want to alter your plan for your project (and obtain approval for the same), be sure to email your section leader directly!

#### What have you done for your project so far?

I have made significant progress on the Doodle Jump game. So far, I have implemented the following features:
The player character (Doodle) is fully functional and can jump from platform to platform.
The game includes random platform generation, with platforms appearing at varying heights and distances.
I’ve added basic physics for gravity and player jumping mechanics.
The game has collision detection, ensuring the player bounces off the platforms correctly.

#### What have you not done for your project yet?

I still need to finalize the visual design and UI elements, including the game over screen, pause menu, and restart functionality.
I plan to add power-ups (such as speed boosts) and different platform types (moving platforms, etc.) to enhance the gameplay.
I need to implement a high-score tracking system that saves and displays the highest score.
Some additional polish and optimization are needed to smooth out the player’s controls.

#### What problems, if any, have you encountered?

One challenge I faced was getting the physics to feel natural. Fine-tuning the jump and gravity mechanics took some time.
There were a few issues with platform collision detection where the player would sometimes overlap or pass through platforms. This required some adjustments to the hit detection logic.
