from autorg.domain.entities.input import Input, EmptyValueError, ValueTooLargeError
import pytest
from datetime import datetime


# Should metadata be a dto or a set of pre derined interesting options like geolocalization?
# Metadata's attributes are up to what kind of file is
   
#- Organizar Inputs: El flujo por el cual se clasifica o se elimina organizables del sistema
#- Clarificar Inputs: El flujo por el cual se convierte cada significante en un organizable, a travez de preguntas clave y planificacion
#- Proceso: Es la combinacion de clarificar y organizar uno o mas inputs en una bandeja de inputs
#- Input: Entidad, representa una nueva informacion para el usuario
#- Bandeja de inputs / Fuente: Es un almacen de inputs

# interface: read_content
# text, video, audio
# 

# parser, from_csv, from_json, from_markdown

# input -> (clarificar -> ordenable [logica])

# tareas (la tarea es algo medianamente abstracto)
#     con fecha de vencimiento
#     para ahora
#     con prioridad
#     bloqueada_por: tarea
#     is_action?


#learning: #1, ddd,  #martin, modelado de dominios., #12-10-23
#learning: { #1 }, ddd,  { #martin }, modelado de dominios., { #12-10-23 }

# modelado de dominios

# class input:




    # larning: -> Aprendizaje (ddd)
    # teachers: #martin, 

# TODO: El input deberia tener metadatos por defecto?
# TODO: ¿Que sucede si no se especifican los metadatos?
# TODO: ¿Que tipos de metadatos son estrictamente necesarios que tenga un input?
# TODO: ¿Es responsabilidad del input procesar los metadatos?
# TODO: ¿Donde vamos a almacenar temporalmente los inputs?
# TODO: ¿Es necesario un `CRUD` de inputs?
# TODO: ¿Es necesario poder buscar un input?
# TODO: ¿La bandeja de inputs debe dar todas las opciones para gestionar inputs?
# TODO: Una vez procesados el inputs y los metadatos, ¿en que formato deberia pasarle la informacion al clarificador?
# TODO: ¿Que datos necesita minimamente el clarificador para poder trabajar?
# TEST: ¿Deberia crear un helper para las pruebas de los inputs?
# TODO: La creacion de tareas require rellenar varios parametros, ¿deberiamos crearlos mediante una factoria?

# class Test_Input:
#
#
#     def test_given_a_information_and_file_metadata_should_be_defined_as_a_input(self):
#         information = "Something is happening"
#         metadata = {"filename":"Data.txt"}
#         assert Input(information,metadata) != None
#
# def test_an_input_should_not_be_empty():
#     input_content = ""
#     input_creation_date = datetime(2023, 9, 7, 16, 25, 18)
#     with pytest.raises(EmptyValueError):
#         Input(input_content,{"creation_date": input_creation_date})
#
# def test_an_input_should_not_be_too_big():
#     input_content = "A" * 1001
#     metadata = {}
#     with pytest.raises(ValueTooLargeError):
#         Input(input_content, metadata)
#
# def test_should_get_the_input_content():
#     input_creation_date = datetime(2023, 9, 7, 16, 25, 18)
#     sut = Input("Hello world", {"creation_date": input_creation_date})
#     assert sut.content() == "Hello world"
#
# def test_the_id_of_the_input_should_be_defined_by_number():
#     sut = Input("Someting", {"creation_date": datetime(2023, 9, 7, 16, 25, 18) })
#     assert type(sut.id()) is int 
#
# def test_the_input_must_not_contain_any_spaces_before_or_after_its_content():
#     sut = Input(" random content wiht    some spaces    ", {"creation_date": datetime(2023, 9, 7, 16, 25, 18) })
#     assert sut.content() == "random content wiht    some spaces"
#
# def test_input_must_contain_its_creation_date():
#     input_content = "some random content"
#     input_creation_date = datetime(2023, 9, 7, 16, 25, 18)
#     metadata = {"creation_date": input_creation_date}
#
#     sut = Input(input_content, metadata)
#     assert sut.get_creation_date() == input_creation_date
#




class Collect:
    def __init__(self):
        self._inputs = []

    def _exists(self, text: str) -> bool:
        if text in self._inputs:
            return True
        else:
            return False

    def input(self, text: str):
        if self._exists(text):
            return
        else:
            self._inputs.append(text)

    
    def getAll(self ):
        return self._inputs


def test_added_input_should_store_in_list():
    sut = Collect()
    sut.input("some random input")
    assert len(sut.getAll() ) == 1

def test_added_input_should_be_unique():
    sut = Collect()
    sut.input("some random input")
    sut.input("some random input")
    assert len(sut.getAll() ) == 1

def test_should_return_list_of_str():
    sut = Collect()
    sut.input("some random input")
    sut.input("some random input")
    assert type (sut.getAll()) is list

def test_collect_can_hold_many_inputs():
    sut = Collect()
    sut.input("some random input")
    sut.input("some random input 2")
    assert len(sut.getAll() ) == 2

# def test_input_list_should_be_stored():
#     sut = Collect(Memory_repository())
#     sut.input("some random input")
#     assert sut.getAll()[0] == "some random input"




