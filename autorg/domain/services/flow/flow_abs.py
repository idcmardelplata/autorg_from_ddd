from autorg.domain.entities.pregunta.pregunta_abs import Pregunta_ABS
class Flow_ABS:
    def __init__(self,name:str):
        self.name = name
        self.preguntas= list()
        self.index = 0
        self.unanswered_questions:list 

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