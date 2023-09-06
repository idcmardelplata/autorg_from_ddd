from autorg.clarification_service import Clarificacion_SRV
from .helpers.fake_flow import Fake_Flow as Flow
from .helpers.fake_pregunta import Fake_Pregunta as Pregunta
import pytest

def test_service_should_accept_a_flow_as_a_parameter_in_constr():
    assert Clarificacion_SRV(Flow("Clarification")) != None

# Este servicio da funcionalidad del flujo de clarificacion
@pytest.mark.parametrize(
    ("serv"),
    [
        (Clarificacion_SRV(Flow("Clarification")))
    ]
)
class Test_Clarificacion_Servicio:

    def test_clarification_flow_should_init_with_the_question_what_this_does_mean_to_me(self,serv):
        assert serv.get_flow().preguntas[0].get_question() == Pregunta("Que significa esto para mi").get_question()

    def test_clarification_service_should_use_flow(self,serv):
        assert isinstance(serv.get_flow(),Flow)

