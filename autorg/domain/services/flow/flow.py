from autorg.domain.entities.pregunta.pregunta import Pregunta
from autorg.domain.services.flow.flow_abs import Flow_ABS
class Flow(Flow_ABS):
    def __init__(self,name:str):
        super().__init__(name)
        self.__load_questions(name) 
        self.unanswered_questions = self.preguntas 

    def __load_questions(self,name:str):
        if name.__eq__("Clarification"):
            lista_preguntas = ["Que significa esto para mi","Es accionable?","Que creo que debo hacer","Cuantas acciones atomicas","Depende de mi?","Es accion siguiente o esta bloqueada?","El no accionable tiene valor potencial?"]
            for pregunta in lista_preguntas:
                self.preguntas.append(Pregunta(pregunta))
        if name.__eq__("Another"):
            self.preguntas.append(Pregunta("Esto tiene sentido?"))

    def get_questions(self):
        return self.preguntas

    def start(self):
        return self

    def get_index(self):
        return self.index

    def answer_current_question(self,response:str):
        self.unanswered_questions.pop(0)
        self.index=+1

    def get_current_question(self):
        return self.unanswered_questions[0]

    def get_unanswered_questions(self):
        return self.unanswered_questions
