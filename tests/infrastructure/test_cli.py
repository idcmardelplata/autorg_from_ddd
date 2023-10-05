import pytest
from click.testing import CliRunner
from autorg.infrastructure.adapters.cli import cmd_input,inbox_list

#TEST: debo verificar que el input ingresado haya quedado persistido
#TEST: verificar que los inputs puedan filtrarse por hora/fecha
#TEST: si el comando inpout no recibe ningun parametro, debe lanzarse una excepcion


# TODO: APP adapter should recieve a instance of desired repo, no just use csv repo!

    


@pytest.mark.integration
def test_input_command_should_persist_data():
    runner = CliRunner()
    sut = runner.invoke(cmd_input, ["random input"])
    assert sut.output == "The input was saved correctly\n"
    assert sut.exit_code == 0

def test_list_inputs_should_show_a_list_of_all_inboxed_inputs():
    runner = CliRunner()
    sut = runner.invoke(cmd_input, ["random input"])
    sut = runner.invoke(cmd_input, ["random input 2"])
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
