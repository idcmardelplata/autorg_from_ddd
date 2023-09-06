from autorg.pregunta.pregunta import Pregunta
from autorg.flow.flow import Flow
class Clarificacion:

    def __init__(self):
        self.flujo:list = list()
        self.flow = Flow("Clarification")
        self.flujo.append(Pregunta("Que significa esto para mi"))

    def get_flow(self):
        return self.flow
