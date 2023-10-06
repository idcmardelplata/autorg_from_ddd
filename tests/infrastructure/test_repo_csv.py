from autorg.domain.aggregates.collect import Collect
from autorg.domain.entities.input import Input
from autorg.infrastructure.adapters.csvrepository import CsvRepository
import pytest
import os


# TEST: ¿Debo manejar alguna logica para borrar los elementos segun algun criterio?
# si, deberias borrar inputs que no se deseen clarificar
# la funcionalidad deberia agregarse primero desde app para usar los spyes
# TEST: Hay un bug sorpresa que deberias buscar josu.... :) #TaskForHome. #Tip (centrate en la funcionalidad basica del componente)
# NOTE: El repositorio csv tiene un metodo, store, el cual deberia estar declarado en su interfaz a implementar!
# TEST: solo puede incluirse un solo input por vez o deberia inserarse tambien por lista?
class TestRepo:
    @classmethod
    def teardown_class(_cls):
        print("elimina el fichero data.csv")
        if os.path.exists("data.csv"):
            os.remove("data.csv")

    def setup_method(self):
        """
        Create subjects for tests
        """
        if os.path.exists("data.csv"):
            os.remove("data.csv")

        repo = CsvRepository()
        collect = Collect(repo)
        self.repo = repo
        self.collect = collect

    @pytest.mark.integration
    def test_repo_should_store_data_in_csv_file(self):
        self.collect.add_input("First input")
        self.collect.add_input("Second input")
        assert len(self.collect.getAll()) == 2

    @pytest.mark.integration
    def test_should_return_all_inputs(self):
        items = ["First element", "second input", "third input", "more content"]
        for item in items:
            self.collect.add_input(item)

        assert len(self.collect.getAll()) == len(items)

    @pytest.mark.integration
    def test_input_id_should_increment_in_each_new_input(self):
        self.collect.add_input("another input")
        assert self.collect.getAll()[0].id() == 0
        self.collect.add_input("another input 1")
        self.collect.add_input("another input 2")
        assert self.collect.getAll()[2].id() == 2
    
    def test_literal_content_should_be_the_same(self):
        self.collect.add_input("item")
        result = self.collect.getAll().pop()
        assert type(result) is Input
        assert result.value()["content"] == "item"
