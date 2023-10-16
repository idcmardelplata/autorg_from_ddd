# cargar el fichero de configuracion config.toml
# la configuracion debe ser dividida entre secciones toml
# cada seccion debe retornar un diccionario

import pytest
from config.config import Config


@pytest.mark.integration
def test_should_load_config_from_file():
    config = Config()
    assert type(config.storage("csv").get("filepath")) is str
    assert config.storage("csv")["filepath"] == "data.csv"

@pytest.mark.integration
def test_config_should_load_project_metadata_on_start():
    config = Config()
    config.load_project_metadata()
    assert config.project["name"] == "autorg"
    assert config.project["version"] == "0.1.0"

@pytest.mark.integration
def test_config_get_storage_should_fail_if_key_not_exists():
    config = Config()
    with pytest.raises(KeyError):
        config.storage("non-existent key")

