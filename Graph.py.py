class graphClass:

    def add_Edge(slf,vertex,edge):
      if vertex not in slf.gp:
        slf.add_Vertex(vertex)
      if edge not in slf.gp[vertex]:
        slf.gp[vertex].append(edge)
      else:
        print("The edge already exists.")

    def print_Graph(slf):
      for node in slf.gp:
        print("\n")
        print("The node",node,end='')
        if len(slf.gp[node]) == 0:
          print(" has no edges")
        else:
          print(" has edges to ",end='')
        for neighbor in slf.gp[node]:
          print(neighbor,end=' ')

    def __init__(slf,gp):
      if gp == None:
        slf.gp = {}
      else:
        slf.gp = gp

    def add_Vertex(slf,vertex):
      slf.gp[vertex] = []

    def Is_Connected(slf,vertex,edge):
      if edge in slf.gp[vertex]:
        return True
      else:
        return False

myGraph = {
  "a":["b","c"],
  "b":["c"],
  "c":["a"]
 }  

graph1 = graphClass(myGraph)
graph1.add_Vertex("d")
graph1.add_Edge("d","a")
graph1.add_Edge("f","d")
print(graph1.Is_Connected("a","g"))
graph1.print_Graph()