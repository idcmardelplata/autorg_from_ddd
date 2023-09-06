from autorg.pregunta.pregunta_abs import Pregunta_ABS
class Fake_Pregunta(Pregunta_ABS):

    def __init__(self,pregunta):
        self.pregunta = pregunta

    def get_question(self):
        return self.pregunta

