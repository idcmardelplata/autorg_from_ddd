from autorg.clarification import Clarificacion
from autorg.flow.flow import Flow
from autorg.pregunta.pregunta import Pregunta
import pytest

# Este servicio da funcionalidad del flujo de clarificacion



def test_clarification_flow_should_init_with_the_question_what_this_does_mean_to_me():
    assert Clarificacion().flujo[0].get_question() == Pregunta("Que significa esto para mi").get_question()

def test_clarification_service_should_use_flow():
    assert isinstance(Clarificacion().get_flow(),Flow)
