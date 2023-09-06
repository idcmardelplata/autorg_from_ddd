class Input:

    ID:int 

    def __init__(self,information:str,metadata:dict):
        self.information = information
        self.metadata = metadata
        self.ID = 4

    def get_id(self):
        return self.ID
