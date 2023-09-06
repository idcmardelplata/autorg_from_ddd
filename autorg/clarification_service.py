from autorg.pregunta.pregunta import Pregunta
from autorg.flow.flow import Flow
class Clarificacion_SRV:

    def __init__(self):
        self.flow = Flow("Clarification")

    def get_flow(self):
        return self.flow
