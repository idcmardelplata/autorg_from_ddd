# Input es una entidad debido a que se tendra un registro de no volver a ingresar un mismo input en el sistema
class Input:

    ID:int 

    def __init__(self,information:str,metadata:dict):
        self.information = information
        self.metadata = metadata
        self.ID = 4

    def get_id(self):
        return self.ID
