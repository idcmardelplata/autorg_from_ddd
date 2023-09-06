class Input:
    """ 
    Input es una entidad debido a que se tendra un registro de no volver a ingresar un mismo input en el sistema
    """
    ID:int 

    def __init__(self,information:str,metadata:dict):
        self.information = self._check_input_content(information)
        self.metadata = metadata
        self.ID = 4

    def get_id(self):
        return self.ID

    def _check_input_content(self, content: str):
        if len(content) == 0:
            raise EmptyValueError
        elif len(content) > 1000:
            raise ValueTooLargeError
        else:
            return content


class EmptyValueError(ValueError):
    pass

class ValueTooLargeError(ValueError):
    pass
