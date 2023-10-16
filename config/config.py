import tomllib

class Config():
    def __init__(self) -> None:
        self._read_file()
        self.project: dict = {}

    def _read_file(self):
        try:
            with open("config.toml", "rb") as f:
                data = tomllib.load(f)
                self.config = data
            
        except FileNotFoundError as err:
            print(f"Error: file not found {err}")

    def storage(self, key) -> dict[str, str]:
        return self.config.get("storage")[key]

    def load_project_metadata(self):
        self.project["name"] = self.config.get("project")["name"]
        self.project["version"] = self.config.get("project")["version"]
