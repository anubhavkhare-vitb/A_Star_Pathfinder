# A_Star_Pathfinder

**About the Project**

This project is a simple implementation of A*(A-star) heuristic search in form of a Pathfinding Algorithm using Python.

I worked on this after learning about A* in my AI/ML classes, where it was introduced as one of the most important and efficient search algorithms. I found it really interesting how it combines both cost and heuristic to find the shortest path, so I decided to implement it practically.

The program runs in the command line and allows the user to input a custom grid, along with start and goal positions. It then finds and displays the shortest path while avoiding obstacles.

*Features*

-->Implementation of A* algorithm from scratch.

-->Uses Manhattan Distance(Distance from nth node to goal).

-->Fully CLI-based (no need of GUI).

-->Accepts user-defined grid input.

-->Displays path in visual format.

*Requirements*

-->Python 3.x(any version works).

-->No external libraries required.

**How to Use**

1.Enter number of rows and columns.

2.Enter the grid row-by-row (give space between characters):

  -->Use 0 for free space.
  
  -->Use 1 for obstacles.
  
3.Enter start position(row and column)

4.Enter goal position in the similar fashion.

**Output**

-->The program will display the grid.

--> If a path exists, it will show:

     []The list of coordinates for the shortest path.
    
     []A visual representation of the path.

*Concept used*

This project is based on the A* search algorithm, which is widely used in Artificial Intelligence for pathfinding problems. Applications range from games, maps to robotics and much more.

**METHOD**

It uses:

       g(n): cost from start node to nth node(edge costs)
       
       h(n): estimated cost from nth node to goal
       
       f(n): g(n) + h(n)
       
This makes it both efficient and optimal.
