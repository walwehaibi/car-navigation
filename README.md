# car-navigation
Use value iteration (MDPs) to have a car go from start position to end position with minimal money lost.

Problem Description:
1- Autonomous cars to navigate throughout a grid
2- cars can move North, South, East, or West
3- There will be some obstacles (given prior). If a car crashes into a building or road closure, car has to pay $100.
4- A car spends $1 for gas each time it moves.
5- The cars will start from a given parking lot, and will end at another parking lot.
6- When a car arrives at a destination parking lot, car will receive $100.
7- Cars have a faulty turning mechanism, so they have a chance of going in a direction other than the one suggested by your model. They will go in the correct direction 70% of the time (10% in each other direction, including along borders).

Goal:  to make the most money over time with the greatest likelihood.
