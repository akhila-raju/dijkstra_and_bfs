from collections import deque
import unittest


def parse_input(filename):
	'''
	Parse and process input file for use.

	Args:
		filename: File containing input data

	Returns:
		tuple (pizzerias, dimension):
			pizzerias (2d int array): Processed pizzerias input
			dimension (int)
	'''
	# Retrieve input from file as an array
	lines = open(filename).read().split('\n')    

	first_line = lines[0].split()
	dimension, num_pizzerias = int(first_line[0]), int(first_line[1])

	# Input validation
	if dimension < 1 or dimension > 1000:
		raise Exception('Dimension must be between 1 and 1000.')
	if num_pizzerias < 1 or num_pizzerias > 1000:
		raise Exception('Number of pizzerias must be between 1 and 1000.')

	pizzerias = []
	for i in range(num_pizzerias):
		new_pizzeria = lines[i + 1]
		pizzerias.append(new_pizzeria)

	# Process pizzerias input
	return process_pizzerias(pizzerias, dimension), dimension


def process_pizzerias(pizzerias, dimension):
	'''
	Process each pizzeria string and convert coordinates and max distance into integers.

	Args:
		pizzerias (string array): String representation of pizzeria data.

	Returns:
		pizzerias_as_ints (2D int array): An array of arrays of 3 values (X, Y, R) represented as ints.
	'''
	pizzerias_as_ints = []

	for pizzeria in pizzerias:
		# Split coordinate string into array of coordinates
		split_pizzeria = pizzeria.split(' ')
		X, Y, R = int(split_pizzeria[0]), int(split_pizzeria[1]), int(split_pizzeria[2])

		# Input validation
		if X < 1 or Y > dimension:
			raise Exception('X and Y values are out of bounds.')
		if R < 1 or R > 100:
			raise Exception('R value out of bounds.')

		pizzerias_as_ints.append([X, Y, R])

	return pizzerias_as_ints


def generate_matrix(dimension):
	'''
	Generates matrix of given dimension.

	Args:
		dimension (int)

	Returns:
		matrix (2D array)
	'''
	return [[0 for i in range(dimension)] for j in range(dimension)]


def modify_row_col(row, col, dimension):
	'''
	Calculates row and column for indexing starting at bottom left corner.
	
	Args:
		row (int)
		col (int)

	Returns:
		new_row (int)
		new_col (int)
	'''
	new_row = dimension - row
	new_col = col - 1
	return new_row, new_col


def calculate_max_visits(pizzerias, dimension):
	'''
	Calculate the number of pizzerias that deliver pizzas to the block with the greatest selection of pizzas.

	Args:
		matrix (2D int array): Matrix that keeps track of visits, initialized as 0s.
		pizzerias (2D int array): Contains X, Y, R values for each pizzeria.

	Returns:
		max_visits (int): The max number of pizzerias 
	'''
	# Initialize matrix of all 0s.
	matrix = generate_matrix(dimension)
	max_visits = 0

	for pizzeria in pizzerias:
		queue = deque()
		# Calculate row and column for indexing starting at bottom left corner
		modified_row, modified_col = modify_row_col(pizzeria[0], pizzeria[1], dimension)
		queue.append([modified_row, modified_col, pizzeria[2]])
		pizza_guy_visited = set()

		while queue:
			delivery_guy_loc = queue.popleft()
			row, col, curr_distance = delivery_guy_loc

			if (row, col) not in visited:
				# Increment visit count on block
				matrix[row][col] += 1
				# Mark block as visited
				pizza_guy_visited.add((row, col))

				# Track the max number of visits
				max_visits = max(max_visits, matrix[row][col])

				# Continue BFS only if distance > 0
				if curr_distance > 0:
					
					# Up
					if row - 1 >= 0 and (row - 1, col) not in pizza_guy_visited:
						queue.append([row - 1, col, curr_distance - 1])

					# Down
					if row + 1 < dimension and (row + 1, col) not in pizza_guy_visited:
						queue.append([row + 1, col, curr_distance - 1])

					# Left
					if col - 1 >= 0 and (row, col - 1) not in pizza_guy_visited:
						queue.append([row, col - 1, curr_distance - 1])

					# Right
					if col + 1 < dimension and (row, col + 1) not in pizza_guy_visited:
						queue.append([row, col + 1, curr_distance - 1])

	return max_visits


class Question2Tests(unittest.TestCase):

	def test_generate_matrix(self):
		self.assertEqual(generate_matrix(2), [[0, 0], [0, 0]])

	def test_modify_row_col_returns_2_2(self):
		self.assertEqual(modify_row_col(3, 3, 5), (2, 2))

	def test_modify_row_col_returns_4_0(self):
		self.assertEqual(modify_row_col(1, 1, 5), (4, 0))

	def test_max_visits_returns_2(self):
		self.assertEqual(calculate_max_visits(pizzerias, dimension), 2)


if __name__ == "__main__":
    # Parse and process input file
    filename = 'input2.txt'
    pizzerias, dimension = parse_input(filename)

    # Run tests
    unittest.main()
