from .significado_abs import Significado_ABS
# Significado es una entidad debido a que sera rastreada mediante el flujo de procesamiento.
class Significado(Significado_ABS):
    def __init__(self,significado:str):
        super().__init__(significado)

