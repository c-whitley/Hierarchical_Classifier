import numpy as np
import networkx as nx

class HC:
	"""
	Recursive hierarchichal classifier.


	"""

	def __init__(self, clf_type, **kwargs):
	    
	    self.clf_type = clf_type

	    
	def fit(self, x, y, layer_names = None):
	    
	    self.x = x
	    self.y = y

	    self.n_layers = self.y.shape[1]

	    if layer_names != None:

	    	self.layer_names = layer_names

	    else:

	    	self.layer_names = np.arange(self.n_layers)

	    #self.model = self.node(self.x, self.y[:, 0], 0)

	    node_n = 0
	    layer_n = 0

	    self.n_in_layer = 0

	    self.graph = nx.DiGraph()
	    self.layer_nodes = dict()

	    #self.clf_list = {ln: {self.graph.add_edge(ln)} 
	    #for i, ln in enumerate(self.layer_names)}

	    #for i, layer_name in enumerate(self.layer_names):
	    #	for j , class_ in enumerate(np.unique(self.y[:,i])):

	    #		self.graph.add_edge(layer_name, class_)

	    		#self.graph.add_node(node_n, layer = self.layer_names[layer_n])


	    self.model = self.new_node(self.x, self.y, "Start", node_n, layer_n)


#    def n_new(self,x ,y):

#   	for i, name in enumerate(np.unique(y[:, layer_n - 1])):

    		




	def new_node(self, x, y, from_, node_n, layer_n):


		if len(np.unique(y[:, layer_n])) == 1:
		
			return self.layer_nodes

		layer_n += 1

		#self.clf_list[self.layer_names[layer_n-1]] = self.clf_type()
		#self.clf_list[self.layer_names[layer_n-1]].fit(x, y)
		
		print(np.unique(y[:, layer_n-1]))

		print(layer_n)


		if layer_n == self.n_layers:

			layer_n = 0


		layer_nodes = dict()

		for i, name in enumerate(np.unique(y[:, layer_n -1])):

			#print(node_n)

			print("Edge", from_, name)

			self.graph.add_edge(from_, name, class_ = name)

			self.layer_nodes[name] = self.new_node(x[y[:, layer_n-1] == name],
				 		  y[y[:, layer_n-1] == name],
				 		  name,
				 		  node_n,
				 		  layer_n)


			node_n += 1



		print("node_n", node_n)

		node_n +=1


	def node(self,x, y, i):
	    
		if len(np.unique(y)) == 1:

			return np.unique(y)

		else:

			i += 1

			clf = self.clf_type().fit(x,y)

			out_dict = dict()

			for name in np.unique(y[:,i]):

				print(name)
				print(x.shape)
				print(y.shape)
				print((y == name).shape)

				print(x[y == name])

				out_dict[name] = self.node(x[y == name]\
					, self.y[y == name, i] , i)

			return out_dict
        