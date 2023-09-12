import hashlib
class Input:
    """ 
    Input es una entidad debido a que se tendra un registro de no volver a ingresar un mismo input en el sistema
    """
    ID:int 

    def __init__(self,information:str,metadata:dict):
        self._content = self._check_input_content(information)
        self._content = self._content.strip()
        self._creation_date = metadata.get("creation_date")

    def get_creation_date(self):
        return self._creation_date 

    def id(self):
        md5 = hashlib.md5()
        md5.update(self._content.encode('utf-8'))
        return md5.digest()

    def _check_input_content(self, content: str):
        if len(content) == 0:
            raise EmptyValueError
        elif len(content) > 1000:
            raise ValueTooLargeError
        else:
            return content

    def content(self):
        return self._content


class EmptyValueError(ValueError):
    pass

class ValueTooLargeError(ValueError):
    pass