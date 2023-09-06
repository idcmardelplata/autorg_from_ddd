from autorg.clarification_service import Clarificacion_SRV
from autorg.flow.flow import Flow
from autorg.pregunta.pregunta import Pregunta
import pytest

# Este servicio da funcionalidad del flujo de clarificacion



def test_clarification_flow_should_init_with_the_question_what_this_does_mean_to_me():
    assert Clarificacion_SRV().get_flow().preguntas[0].get_question() == Pregunta("Que significa esto para mi").get_question()

def test_clarification_service_should_use_flow():
    assert isinstance(Clarificacion_SRV().get_flow(),Flow)
