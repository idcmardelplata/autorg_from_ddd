import pytest
# Should metadata be a dto or a set of pre derined interesting options like geolocalization?
# Metadata's attributes are up to what kind of file is
   
#- Organizar Inputs: El flujo por el cual se clasifica o se elimina organizables del sistema
#- Clarificar Inputs: El flujo por el cual se convierte cada significante en un organizable, a travez de preguntas clave y planificacion
#- Proceso: Es la combinacion de clarificar y organizar uno o mas inputs en una bandeja de inputs
#- Input: Entidad, representa una nueva informacion para el usuario
#- Bandeja de inputs / Fuente: Es un almacen de inputs

class Input:

    ID:int 

    def __init__(self,information:str,metadata:dict):
        self.information = information
        self.metadata = metadata
        self.ID = 4

    def get_id(self):
        return self.ID

def test_given_a_information_and_file_metadata_should_be_defined_as_a_input():
    information = "Something is happening"
    metadata = {"filename":"Data.txt"}
    assert Input(information,metadata) != None


def test_input_should_has_an_id_attr():
    assert isinstance(Input("Something",dict() ).get_id(),int)
