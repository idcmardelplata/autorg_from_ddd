from autorg.significado import Significado
import pytest

def test_significado_should_be_defined_by_a_string():
    assert Significado("Esto significa esto") != None
