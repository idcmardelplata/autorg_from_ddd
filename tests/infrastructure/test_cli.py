import pytest
from click.testing import CliRunner
from autorg.infrastructure.adapters.cli import inbox, inbox_list

# TEST: debo verificar que el input ingresado haya quedado persistido
# TEST: verificar que los inputs puedan filtrarse por hora/fecha
# TEST: el comando inbox debe contener todo lo relativo a la bandeja de entrada (listar, agregar etc)


# TODO: APP adapter should recieve a instance of desired repo, no just use csv repo!

@pytest.mark.integration
def test_input_command_should_persist_data():
    runner = CliRunner()
    sut = runner.invoke(inbox, ["random input"])
    assert sut.output == "The input was saved correctly\n"

    # ¿How verify that the input was stored?
    assert sut.exit_code == 0

@pytest.mark.skip
#FIX: Deberiamos replantear la forma de la prueba para que sea mas legible
def test_list_inputs_should_show_a_list_of_all_inboxed_inputs():
    runner = CliRunner()
    sut = runner.invoke(inbox, ["random input"])
    sut = runner.invoke(inbox, ["random input 2"])
    sut = runner.invoke(inbox_list, ["all"])
    actual =  [+1 for input in ["random input","random input 2"] if input in sut.output ]
    assert len(actual) == 2
    assert sut.exit_code == 0
    

#TEST: def test_list_inputs_should_show_a_error_msg_in_stderr_when_there_is_none_inboxed():
#    runner = CliRunner()
#    sut = runner.invoke(inbox_list, ["all"])
#    actual =  [+1 for input in ["random input","random input 2"] if input in sut.output ]
#    assert len(actual) == 2
#    assert sut.exit_code == 0
