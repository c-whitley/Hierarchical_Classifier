import numpy as np
from sklearn.ensemble import RandomForestClassifier

class Hierarchical:
	"""

	"""

	def __init__(self):

		self.current_node = 0
		self.current_layer = 0
		self.nodes = []

	def fit(self, x, y, **kwargs):

		self.n_layers = np.min(y.shape)
		self.headers = kwargs.get("headers", np.arange(self.n_layers))
		self.n_leaf = 0
		#self.tree = self.build_tree(x, y, 0)

		self.tree = Decision_Node(x, y, self.headers[0], 0, self.current_layer)


	def build_tree(self, x, y, current_layer):


		if current_layer == self.n_layers:

			self.n_leaf += 1

			return y[:, current_layer-1][0]

			#return Leaf(x, y)

		#print(y.shape, x.shape)


		rows = {name: (x[y[:, current_layer]==name], y[y[:, current_layer]==name]) 
		for name in np.unique(y[:, current_layer])}


		branches = {}

		for name, data in rows.items():

			self.current_node += 1

			branches[name] = self.build_tree(data[0], data[1], current_layer + 1)

			self.nodes.append(Decision_Node(data[0], data[1], self.headers[current_layer]
					, branches[name]
					, self.current_node))

		#branches = {name: self.build_tree(data[0], data[1], current_layer + 1) 
		#for name, data in rows.items()}

		return branches


class Decision_Node(Hierarchical):


	def __init__(self, x, y, name, n, current_layer, clf = RandomForestClassifier):

		self.name = name
		self.n = n

		self.x = x
		self.y = y
		self.current_layer = current_layer

		# Initialise the classifier for the node
		self.clf = clf()
		self.node_fit()


	def node_fit(self):

		if len(np.unique(self.y[:, self.current_layer])) == 1:

			return y[0]

		self.clf.fit(self.x, self.y[:, self.current_layer])


		# Dictionary to hold all of the nodes edges
		self.edges = {}

		# Iterate through all possible labels and create new node
		for class_name in np.unique(self.y[:, self.current_layer]):

			self.edges[class_name] = Decision_Node(
				  self.x[self.y[:, self.current_layer] == class_name]
				, self.y[self.y[:, self.current_layer] == class_name, self.current_layer]
				, Hierarchical.headers[self.current_layer + 1]
				, Hierarchical.current_node + 1
				, self.current_layer + 1)
