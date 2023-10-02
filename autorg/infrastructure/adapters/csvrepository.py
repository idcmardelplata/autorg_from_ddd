import os
import csv
from typing import Optional
from autorg.domain.protocols.repository import Repository

class CsvRepository(Repository):
    def __init__(self):
        self._repo_path = "data.csv"
        self._index = 0
        self.rows = []

    def _file_exists(self):
        return os.path.exists(self._repo_path)

    def store(self, input_text: str) -> None:
        rows = [ [self._index, input_text] ]

        mode = 'a' if os.path.exists("data.csv") else 'w'
        with open(self._repo_path, mode, newline='') as file:
             writer = csv.writer(file)
             writer.writerows(rows)
             self._index += 1

    def getAll(self) -> list[str]:
        if len(self.rows) != 0:
            return self.rows
        else:
            if  self._file_exists():
                with open(self._repo_path, "r", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        self.rows.append(row[1])
        return self.rows
