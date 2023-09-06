from autorg.input import Input
import pytest
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

# TODO: ¿Que ocurre con un input vacio?
# TODO: ¿Que sucede con un input demasiado grande?
# TODO: ¿Que sucede si no se especifican los metadatos?
# TODO: ¿Que tipos de metadatos son estrictamente necesarios que tenga un input?
# TODO: ¿Es responsabilidad del input procesar los metadatos?
# TODO: ¿Donde vamos a almacenar temporalmente los inputs?
# TODO: ¿Es necesario un `CRUD` de inputs?
# TODO: ¿Es necesario poder buscar un input?
# TODO: ¿La bandeja de inputs debe dar todas las opciones para gestionar inputs?
# TODO: Una vez procesados el inputs y los metadatos, ¿en que formato deberia pasarle la informacion al clarificador?
# TODO: ¿Que datos necesita minimamente el clarificador para poder trabajar?



def test_given_a_information_and_file_metadata_should_be_defined_as_a_input():
    information = "Something is happening"
    metadata = {"filename":"Data.txt"}
    assert Input(information,metadata) != None


def test_input_should_has_an_id_attr():
    # TODO: El input deberia tener metadatos por defecto?
    assert isinstance(Input("Something",dict() ).get_id(),int)
