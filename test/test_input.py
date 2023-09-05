import pytest
# Should metadata be a dto or a set of pre derined interesting options like geolocalization?
# Metadata's attributes are up to what kind of file is

class Input:
    def __init__(self,information:str,metadata:dict):
        self.information = information
        self.metadata = metadata

def test_given_a_information_and_file_metadata_should_be_defined_as_a_input():
    information = "Something is happening"
    metadata = {"filename":"Data.txt"}
    assert Input(information,metadata) != None
