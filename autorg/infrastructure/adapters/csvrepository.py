import os
import csv
from autorg.domain.protocols.protocols import Repository

class CsvRepository(Repository):
    def __init__(self):
        self._repo_path = "data.csv"
        self._index = 0

    def _file_exists(self):
        return os.path.exists(self._repo_path)

    def find(self, data: str):
        if not self._file_exists():
            return False

        with open(self._repo_path, 'r', encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == data:
                    return int(row[0])

    def store(self, input_text: str) -> None:
        rows = [ [self._index, input_text] ]

        mode = 'a' if os.path.exists("data.csv") else 'w'
        with open(self._repo_path, mode, newline='') as file:
             writer = csv.writer(file)
             writer.writerows(rows)
             self._index += 1

    def getAll(self) -> list[str] | None:
        rows = []
        if not self._file_exists():
            return None

        with open(self._repo_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row[1])
            return rows
