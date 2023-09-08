from .fake_pregunta import Fake_Pregunta as Pregunta
from autorg.domain.services.flow.flow_abs import Flow_ABS
class Fake_Flow(Flow_ABS):
    def __init__(self,name):
        self.name = name
        self.preguntas_str = ["Que significa esto para mi","Es accionable?","Que creo que debo hacer","Cuantas acciones atomicas","Depende de mi?","Es accion siguiente o esta bloqueada?","El no accionable tiene valor potencial?"]
        self.preguntas = [Pregunta(x) for x in self.preguntas_str]
        self.index = 0
        self.__load_questions(name) 
        self.unanswered_questions:list = self.preguntas 

    def __load_questions(self,name:str):
        pass

    def get_questions(self):
        pass

    def start(self):
        pass

    def get_index(self):
        pass

    def answer_current_question(self,response:str):
        pass

    def get_current_question(self):
        pass

    def get_unanswered_questions(self):
        pass
