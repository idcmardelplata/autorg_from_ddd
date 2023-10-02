import pytest
from click.testing import CliRunner
from autorg.infrastructure.adapters.cli import cmd_input

#TEST: debo verificar que el input ingresado haya quedado persistido
#TEST: verificar que los inputs puedan filtrarse por hora/fecha
#TEST: si el comando inpout no recibe ningun parametro, debe lanzarse una excepcion


@pytest.mark.integration
def test_input_command_should_persist_data():
    runner = CliRunner()
    sut = runner.invoke(cmd_input, ["random input"])
    assert sut.output == "The input was saved correctly\n"
    assert sut.exit_code == 0
