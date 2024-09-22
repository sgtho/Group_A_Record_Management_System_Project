import json
from typing import List, Dict, Any

class ClientRepository:
    def __init__(self, filename: str):
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        records = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    records.append(json.loads(line.strip()))
        except FileNotFoundError:
            return []
        return records

    def save_records(self):
        with open(self.filename, 'w') as file:
            for record in self.records:
                file.write(json.dumps(record) + '\n')  # Write each record as a new line

    def create(self, record):
        self.records.append(record)
        self.save_records()

    def list(self):
        return self.records