from autorg.pregunta.pregunta import Pregunta
class Flow:
    def __init__(self,name):
        self.name = name
        self.preguntas= list()
        self.__load_questions(name) 

    def __load_questions(self,name:str):
        if name.__eq__("Clarification"):
            lista_preguntas = ["Que significa esto para mi","Es accionable?","Que creo que debo hacer","Cuantas acciones atomicas","Depende de mi?","Es accion siguiente o esta bloqueada?","El no accionable tiene valor potencial?"]
            for pregunta in lista_preguntas:
                self.preguntas.append(Pregunta(pregunta))
        if name.__eq__("Another"):
            self.preguntas.append(Pregunta("Esto tiene sentido?"))

    def get_questions(self):
        return self.preguntas
