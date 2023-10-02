from autorg.domain.aggregates.collect import Collect
from autorg.infrastructure.adapters.csvrepository import CsvRepository
import pytest
import os


#TEST: ¿Debo manejar alguna logica para borrar los elementos segun algun criterio?
#TEST: Hay un bug sorpresa que deberias buscar josu.... :) #TaskForHome. #Tip (centrate en la funcionalidad basica del componente)

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
        self.collect.input("First input")
        self.collect.input("Second input")
        assert len(self.collect.getAll()) == 2


    @pytest.mark.integration
    def test_should_return_all_inputs(self):
        items = ["First element", "second input", "third input", "more content"]
        for item in items:
            self.collect.input(item)
    
        assert len(self.collect.getAll()) == len(items)
