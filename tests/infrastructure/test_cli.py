import os
import pytest
from click.testing import CliRunner
from autorg.infrastructure.adapters.cli import add_command, ls_command

# TEST: debo verificar que el input ingresado haya quedado persistido
# TEST: verificar que los inputs puedan filtrarse por hora/fecha
# TEST: el comando inbox debe contener todo lo relativo a la bandeja de entrada (listar, agregar etc)


# TODO: APP adapter should recieve a instance of desired repo, no just use csv repo!

class TestCli:

    def setup_method(self):
        runner = CliRunner()
        self.runner = runner

    def teardown_method(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")


    @pytest.mark.integration
    def test_input_command_should_persist_data(self):
        sut = self.runner.invoke(add_command, ["random input"])
        assert sut.output == "The input was saved correctly\n"

        # ¿How verify that the input was stored?
        assert sut.exit_code == 0

    @pytest.mark.skip
    #FIX: Deberiamos replantear la forma de la prueba para que sea mas legible
    def test_list_inputs_should_show_a_list_of_all_inboxed_inputs(self):
        sut = self.runner.invoke(add_command, ["random input"])
        sut = self.runner.invoke(add_command, ["random input 2"])
        sut = self.runner.invoke(ls_command)
        actual =  [+1 for input in ["random input","random input 2"] if input in sut.output ]
        assert len(actual) == 2
        assert sut.exit_code == 0
    
    @pytest.mark.integration
    def test_list_inputs_should_show_a_msg_when_there_is_none_inboxed(self):
        sut = self.runner.invoke(ls_command)
        assert sut.output == "Not inputs found\n"
        assert sut.exit_code == 0

