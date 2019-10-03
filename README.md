# PolyAI Take Home Assignment

# Question 1
### My approach
Dijkstra's algorithm finds the shortest path between nodes in a graph. We can find the shortest path between Earth and Zearth through representing the coordinates of the stations, Earth, and Zearth as a graph. Out of the paths visited, the minimum distance is returned.

### Solution
The solution can be found in question1.py. To run the example test cases, use the command `python question1.py`.

### Complexity
The complexity of parsing the input is O(1) since the number of teleportations is at most 500, therefore lines in the input is at most 502. time and space complexity of Dijkstra's algorithm is O(E log V) where E = the number of edges and V = the number of vertices. The complexity of then going through the paths returned by Dijkstra's to find the minimum path is O(number of paths). The total time complexity is O(E log V + number of paths). This is the best time complexity we can get.

# Question 2

### My approach
First, the matrix is built using the given dimensions. On this matrix, the count of pizzerias that have visited each block is maintained. When the count for a block is modified, the max visits seen so far is also kept in check. For each of the pizzerias, a breadth first search starts from their X and Y coordinates, and then move until the max distance is hit for the pizzeria's delivery guy. Once breadth first search traversal for all of the pizzerias has completed, the max number of visits is returned.

### Solution
The solution can be found in question2.py. To run the example test cases, use the command `python question2.py`.

### Complexity
The complexity of parsing the input is O(1) since the number of pizzerias is at most 1000, therefore the number of lines is at most 1002. The time complexity of breadth first search is O(M * M) where M is the dimension of the matrix since every block in the matrix can be visited by each pizza delivery guy. Since we know there are at most 1000 pizzerias, the time complexity remains O(M * M) since 1000 is a constant. The space complexity for the matrix is O(M * M) as well. This is the best time and space complexity we can get.
