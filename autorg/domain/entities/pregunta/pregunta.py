from .pregunta_abs import Pregunta_ABS
class Pregunta(Pregunta_ABS):

    def __init__(self,pregunta:str):
        super().__init__(pregunta)
        self.pregunta = pregunta

    def get_question(self):
        return self.pregunta

