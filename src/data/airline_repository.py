import json


class AirlineRepository:
    """
    AirlineRepository is responsible for managing airline records, which are stored in JSONL format.
    It provides methods to create, read, update, and delete (CRUD) records in a JSONL file.
    """

    def __init__(self, filename: str):
        """
        Initializes the repository with the specified file and loads the existing records.

        :param filename: The name of the JSONL file where airline records are stored.
        """
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        """
        Loads airline records from the specified JSONL file.

        :return: A list of dictionaries, each representing an airline record.
        """
        records = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    records.append(json.loads(line.strip()))
        except FileNotFoundError:
            return []
        return records

    def save_records(self):
        """
        Saves all airline records back to the JSONL file.
        Each record is written as a separate line in JSON format.
        """
        with open(self.filename, 'w') as file:
            for record in self.records:
                file.write(json.dumps(record) + '\n')  # Write each record as a new line

    def create(self, record: dict):
        """
        Adds a new airline record to the repository and saves it to the JSONL file.

        :param record: The airline record to add (as a dictionary).
        """
        record["ID"] = len(self.records) + 1
        self.records.append(record)
        self.save_records()

    def list(self):
        """
        Lists all airline records.

        :return: A list of all airline records.
        """
        return self.records

    def get(self, airline_id: int):
        """
        Retrieves an airline record by its ID.

        :param airline_id: The ID of the airline to retrieve.
        :return: The airline record if found, otherwise None.
        """
        for record in self.records:
            if record["ID"] == airline_id:
                return record
        return None

    def search_by_name(self, name: str):
        """
        Searches for airline records by airline company name.

        :param name: The airline company name or partial name to search for.
        :return: A list of airline records that match the provided airline company name (case-insensitive).
        """
        if len(name) == 0:
            return self.records
        filtered = []
        for record in self.records:
            if record["Name"].lower().startswith(name.lower()):
                filtered.append(record)
        return filtered

    def search_by_id(self, airline_id: str):
        """
        Searches for airline records by partial or full ID.

        :param airline_id: The partial or full ID to search for.
        :return: A list of airline records that match the provided ID.
        """
        if len(airline_id) == 0:
            return self.records
        filtered = []
        for record in self.records:
            if str(record["ID"]).startswith(airline_id):
                filtered.append(record)
        return filtered

    def update(self, updated_record: dict):
        """
        Updates an existing airline record.

        :param updated_record: The updated airline record (as a dictionary).
        """
        for idx, airline in enumerate(self.records):
            if airline["ID"] == updated_record["ID"]:
                self.records[idx] = updated_record
                break
        self.save_records()

    def delete(self, record: dict):
        """
        Deletes an airline record from the repository.

        :param record: The airline record to delete (as a dictionary).
        """
        for idx, airline in enumerate(self.records):
            if airline["ID"] == record["ID"]:
                del self.records[idx]
                break
        self.save_records()
