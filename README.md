# Battleships

Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
The objective is to sink enemy ships by guessing their location on a board.

---
## How to play

The goal of the game is to sink all of the enemy ships hidden on the board

This simple iteration of the game simply prints 10 ships on the board for you to find and sink.

The player inputs a location on the board that they want to shoot, for example C6.

When all 10 enemy ships have been sunk you are victorious.

---

## Features

### Current Features

-__Random Board__-

- Creates a Board of the set size.

- 10 ships are randomly hidden on the board

- Each "square" on the board is represented by a letter and number to make indexing easy.
  
-__Input Checking__-

- The game makes sure you enter a correct position to shoot and makes sure the format of the guess is correct.

- The game prints a message alerting you to if you've hit, missed, or if you tried to shoot the same location twice.


### Possible Future Features

-__Score System__-

- A system that keeps track of player guesses could be implemented. Maybe with set amount of guesses before the player loses the game.
  
-__Computer Opponent__-

- A Versus mode could be implemented where the player and computer have a board each and take turns trying to sink the other's ships.

-__Scaleable Grid__-

- Option for the player to define the size of the board themselves upon game launch, with adjusted number of ships and ship sizes.

---

## Testing

- The project has been tested multiple times both locally and in the Code Institue Heroku Terminal functioning properly.
- The project has been able to handle any invalid inputs that have been thrown at it.
  
### Validator Testing

- Passed through the [Code Institute PEP8 linter](https://pep8ci.herokuapp.com/) without any problems.

### Bugs/Unresolved Issues

- Game didnt correctly count sunk ships on one test run in the local terminal. However as I could not find a way to reproduce it and all tests since have worked properly I have left this as a possibly unresolved issue.

---

## Deployment

- The site was deployed using Heroku. The steps to deploy are:
  - Fork or clone repository
  - Create a Heroku app
  - Set buildbacks to Python and NodeJS
  - Link Heroku app repository
  - Deploy

The live site can be found at: <https://ci--battleships-pp3-7cb38352ff86.herokuapp.com/>

---

## Credits

- [This Youtube Tutorial](https://www.youtube.com/watch?v=MgJBgnsDcF0&ab_channel=CSStudents) was heavily referenced in the creating of this project, and almost all of the project's code originates from here with some re-writes to fit own variables or where a simpler way to write the code was found.
- Code Institute for the deployment terminal