from autorg.pregunta.pregunta import Pregunta
class Flow:
    def __init__(self,name):
        self.name = name
        self.preguntas= list()
        self.preguntas.append(Pregunta("Que significa esto para mi"))
