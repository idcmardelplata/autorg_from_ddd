from autorg.pregunta.pregunta import Pregunta
from autorg.domain.services.flow.flow import Flow
class Clarificacion_SRV:

    def __init__(self,flow):
        self.flow = flow

    def get_flow(self):
        return self.flow
