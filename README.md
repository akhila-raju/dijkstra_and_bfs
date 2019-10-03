# PolyAI Take Home Assignment

# Question 1
### My approach
Dijkstra's algorithm finds the shortest path between nodes in a graph. We can find the shortest path between Earth and Zearth through representing the coordinates of the stations, Earth, and Zearth as a graph. Out of the paths visited, the minimum distance is returned.

### Solution
The solution can be found in question1.py.

### Complexity
The time and space complexity of Dijkstra's algorithm is O(E log V). The complexity of then going through the paths returned by Dijkstra's to find the minimum path is O(number of paths). The total time complexity is O(E log V + number of paths). This is the best time complexity we can get.

# Question 2

### My approach
First, the matrix is built using the given dimensions. On this matrix, the count of pizzerias that have visited each block is maintained. When the count for a block is modified, the max visits seen so far is also kept in check. For each of the pizzerias, a breadth first search starts from their X and Y coordinates, and then move until the max distance is hit for the pizzeria's delivery guy. Once breadth first search traversal for all of the pizzerias has completed, the max number of visits is returned.

### Solution
The solution can be found in question2.py.

### Complexity
The complexity of breadth first search is O(V + E).

## How To Run

To run the example test cases, use the command python question1.py and python question2.py.
