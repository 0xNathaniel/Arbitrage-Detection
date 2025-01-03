from math import log

class Graph:
    def __init__(self, currency_names, rates):
        self._vertices = len(currency_names)
        self._edges = []
        self._currency_names = currency_names
        self._build(rates, currency_names)
        
    def add_edge(self, u, v, w):
        if u >= self._vertices or v >= self._vertices or u < 0 or v < 0:
            raise ValueError("Vertex index out of bound")
        self._edges.append((u, v, w))
    
    def _build(self, rates, currency_names):
        for i in range(len(currency_names)):
            for j in range(len(currency_names)):
                if i != j:
                    # Logarithmic conversion
                    self.add_edge(i, j, -log(rates[i][j]))
                    
    @property
    def vertices(self):
        return self._vertices
    
    @vertices.setter
    def vectices(self, vertices):
        if vertices < 1:
            raise ValueError("Number of vertices must be at least 1")
        self._vertices = vertices
        
    @property
    def edges(self):
        return self._edges
    
    @property
    def currency_names(self):
        return self._currency_names
    
    @currency_names.setter
    def currency_names(self, currency_names):
        self._currency_names = currency_names