from autorg.pregunta.pregunta import Pregunta
class Flow:
    def __init__(self,name):
        self.name = name
        self.preguntas= list()
        self.__load_questions(name)

    def __load_questions(self,name:str):
        if name.__eq__("Clarification"):
            self.preguntas.append(Pregunta("Que significa esto para mi"))
        if name.__eq__("Another"):
            self.preguntas.append(Pregunta("Esto tiene sentido?"))

    def get_questions(self):
        return self.preguntas
