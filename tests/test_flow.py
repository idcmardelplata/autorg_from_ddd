from autorg.flow import Flow
import pytest

def test_given_a_name_flow_should_exists():
        assert Flow("Clarification") != None
