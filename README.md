# car-navigation
This program uses value iteration (MDPs) to have autonomous cars go from a start position to an end position in a grid with minimal money spent.

## Problem Description:
1- Autonomous cars navigating throughout a grid
2- Cars can move north, south, east, or west
3- There will be some obstacles such as building and road closures (given as input to the program). 
4- If a car crashes into an obstacle, the car has to pay $100.
5- A car spends $1 for gas for every move.
6- The cars will start from a given parking lot, and will end at another parking lot.
7- When a car arrives at a destination parking lot, it will receive $100 reward.
8- Cars have a faulty turning mechanism, so they have a chance of going in a direction other than the one suggested by the model. They will go in the correct direction 70% of the time (10% in each other direction, including along borders).

## Input file:
The file input.txt is formatted as follows:
First line: strictly positive 32-bit integer s, size of grid [grid is a square of size sxs]
Second line: strictly positive 32-bit integer n, number of cars
Third line: strictly positive 32-bit integer o, number of obstacles
Next o lines: 32-bit integer x, 32-bit integer y, denoting the location of obstacles
Next n lines: 32-bit integer x, 32-bit integer y, denoting the start location of each car
Next n lines: 32-bit integer x, 32-bit integer y, denoting the terminal location of each car

## Output file:
The file output.txt is formatted as follows:
n lines: 32-bit integer, denoting the mean money earned in simulation for each car, integer result of floor operation

## Goal:
To make the most money over time with the greatest likelihood.
