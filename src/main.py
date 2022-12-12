from sys import argv
from classes.CreardorGrafica import CreadorGrafica

class main:

    script, archivo = argv
    nombreArchivo = "assets/%s"%archivo
    objGrafica = CreadorGrafica(nombreArchivo)
    grafica = objGrafica.getGrafica()
    