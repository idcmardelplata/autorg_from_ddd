from autorg.domain.entities.pregunta.pregunta import Pregunta
from autorg.domain.services.flow.flow_abs import Flow_ABS
class Clarificacion_SRV:


    def __init__(self,flow:Flow_ABS):
        self.flow = flow

    def get_flow(self):
        return self.flow
