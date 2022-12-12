from classes.Graph import Graph

class CreadorGrafica:

    def __init__(self,nombre):
        self.lecturaArchivo(nombre)

    def lecturaArchivo(self,nombre):
        listaLineas = []
        with open(nombre) as archivo:
            listaLineas = archivo.readlines()
        grafica = self.creacionGrafica(listaLineas.pop(0))
        self.grafica = self.unirVertices(listaLineas, grafica)

    def creacionGrafica(self,cadena):
        grafica = Graph()
        listaVertices  = cadena.split(',')
        eliminarSalto = listaVertices[len(listaVertices) - 1].replace('\n','')
        listaVertices[len(listaVertices) - 1] = eliminarSalto
        for vertice in listaVertices:
            grafica.addVertex(vertice)
                
        return grafica

    def unirVertices(self,listaCadenas, grafica):
        graph = grafica
        for cadena in listaCadenas:
            listaAristas  = cadena.split(',')
            eliminarSalto = listaAristas[1].replace('\n','')
            listaAristas[1] = eliminarSalto
            graph.addEdge(listaAristas[0], listaAristas[1], listaAristas[2])
        return graph  
    
    def getGrafica(self):
        return self.grafica