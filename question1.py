from collections import defaultdict, deque
import math, unittest

def parse_input(filename):
	'''
	Parse and form the input file for use.

	Args:
		filename: File containing input data 

	Returns:
		
	'''
	# Retrieve input from file as an array
	lines = open(filename).read().split('\n')    

	num_stations = int(lines[1])
	if num_stations < 1 or num_stations > 500:
		raise Exception('Number of stations must be between 1 and 500.')

	earth_coord = '0.00 0.00 0.00'
	zearth_coord = lines[0]

	coordinates = []
	coordinates.append(earth_coord)
	coordinates.append(zearth_coord)

	for i in range(num_stations):
		new_coord = lines[i + 2]
		coordinates.append(new_coord)

	return process_coordinates(coordinates), num_stations


def process_coordinates(coordinates):
	'''
	Process each coordinate and convert string into an array of floats.

	Args:
		coordinates: An array containing a string representation of the coordinates.

	Returns:
		coordinates_as_floats: An array of arrays of 3 coordinates represented as floats.
	'''
	coordinates_as_floats = []

	for coord in coordinates:
		# Split coordinate string into array of coordinates
		new_coord = coord.split(' ')

		new_coord_as_floats = []

		for num in new_coord:
			num_as_float = float(num)
			if num_as_float < -10000.0 or num_as_float > 10000.0:
				raise Exception('Coordinate must be between -10000.00 and 10000.00.')
			new_coord_as_floats.append(num_as_float)

		coordinates_as_floats.append(new_coord_as_floats)

	return coordinates_as_floats


def calculate_euclidean_distance(from_coord, to_coord):
	'''
	Calculates Euclidean distance between two coordinates.

	Args:
		from_coord (int array)
		to_coord (int array)

	Returns:
		Euclidean distance (int) between from_coord and to_coord
	'''
	x_squared = math.pow(from_coord[0] - to_coord[0], 2)
	y_squared = math.pow(from_coord[1] - to_coord[1], 2)
	z_squared = math.pow(from_coord[2] - to_coord[2], 2)
	return math.sqrt(x_squared + y_squared + z_squared)
	

class Graph:
	'''
	Creates a graph with vertices, edges, and distances.
	'''

	def __init__(self):
		self.vertices = set()
		self.edges = defaultdict(list)
		self.distances = {}

	def add_vertex(self, value):
		self.vertices.add(value)

	def add_edge(self, from_coord, to_coord, distance):
		self.edges[from_coord].append(to_coord)
		self.edges[to_coord].append(from_coord)
		self.distances[(from_coord, to_coord)] = distance

	def populate_graph(self, coordinates):
		'''
		Populate a graph with the given coordinates.
		'''
		for i in range(len(coordinates)):
			for j in range(len(coordinates)):
				if i != j and i < j:
					i_coord = (coordinates[i][0], coordinates[i][1], coordinates[i][2])
					j_coord = (coordinates[j][0], coordinates[j][1], coordinates[j][2])
					self.add_vertex(i_coord)
					distance = calculate_euclidean_distance(coordinates[i], coordinates[j])
					self.add_edge(i_coord, j_coord, distance)


def dijkstra(graph, start):
	'''
	Dijkstra's algorithm to calculate the shortest paths between vertices in a graph.

	Args:
		graph: Graph populated with stations, Zearth, and Earth coordinates
		start: Earth coordinates

	Returns:
		visited: Vertices visited
		paths: Traversed paths
	'''
	visited = {start: 0}
	path = {}

	vertices = set(graph.vertices)
	while vertices:
		min_vertex = None
		for vertex in vertices:
			if vertex in visited:
				if min_vertex is None or visited[vertex] < visited[min_vertex]:
					min_vertex = vertex

		if not min_vertex:
			break

		vertices.remove(min_vertex)
		curr_distance = visited[min_vertex]

		for edge in graph.edges[min_vertex]:
			try:
				distance = curr_distance + graph.distances[(min_vertex, edge)]
				if edge not in visited or distance < visited[edge]:
					visited[edge] = distance
					path[edge] = min_vertex
			except:
				continue

	return visited, path


def min_path(graph, from_coord, to_coord):
	'''
	Calculates the minimum path between Earth and Zearth

	Args:
		from_coord (coordinate): Earth coordinates
		to_coord (coordinate): Zearth coordinates

	Returns:
		min_so_far (int): Length of minimum path
	'''
	visited, all_paths = dijkstra(graph, from_coord)
	min_so_far = float('inf')
	for key, val in visited.items():
		if val != 0:
			min_so_far = round(min(min_so_far, val), 2)
	return min_so_far


class TestCalculateMinPaths(unittest.TestCase):

	def test_max_visits_returns_2_00(self):
		self.assertEqual(min_path(graph_1, from_coord, to_coord), 2.00)

	def test_max_visits_returns_1_73(self):
		self.assertEqual(min_path(graph_2, from_coord, to_coord), 1.73)


if __name__ == "__main__":
	# Parse and process input files
	filename_1 = 'input1_1.txt'
	coordinates_1, num_stations_1 = parse_input(filename_1)
	graph_1 = Graph()
	graph_1.populate_graph(coordinates_1)

	filename_2 = 'input1_2.txt'
	coordinates_2, num_stations_2 = parse_input(filename_2)
	graph_2 = Graph()
	graph_2.populate_graph(coordinates_2)

	from_coord = (coordinates_1[0][0], coordinates_1[0][1], coordinates_1[0][2])
	to_coord = (coordinates_1[1][0], coordinates_1[1][1], coordinates_1[1][2])

	# Run tests
	unittest.main()
