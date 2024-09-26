import json


class ClientRepository:
    """
    ClientRepository is responsible for managing client records, which are stored in JSONL format.
    It provides methods to create, read, update, and delete (CRUD) records in a JSONL file.
    """

    def __init__(self, filename: str):
        """
        Initializes the repository with the specified file and loads the existing records.

        :param filename: The name of the JSONL file where client records are stored.
        """
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        """
        Loads client records from the specified JSONL file.

        :return: A list of dictionaries, each representing a client record.
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
        Saves all client records back to the JSONL file.
        Each record is written as a separate line in JSON format.
        """
        with open(self.filename, 'w') as file:
            for record in self.records:
                file.write(json.dumps(record) + '\n')  # Write each record as a new line

    def create(self, record: dict):
        """
        Adds a new client record to the repository and saves it to the JSONL file.

        :param record: The client record to add (as a dictionary).
        """
        record["ID"] = len(self.records) + 1
        self.records.append(record)
        self.save_records()

    def list(self):
        """
        Lists all client records.

        :return: A list of all client records.
        """
        return self.records

    def get(self, client_id: int):
        """
        Retrieves a client record by its ID.

        :param client_id: The ID of the client to retrieve.
        :return: The client record if found, otherwise None.
        """
        for record in self.records:
            if record["ID"] == client_id:
                return record
        return None

    def search_by_name(self, name: str):
        """
        Searches for client records by name.

        :param name: The name or partial name to search for.
        :return: A list of client records that match the provided name (case-insensitive).
        """
        if len(name) == 0:
            return self.records
        filtered = []
        for record in self.records:
            if record["Name"].lower().startswith(name.lower()):
                filtered.append(record)
        return filtered

    def search_by_id(self, client_id: str):
        """
        Searches for client records by partial or full ID.

        :param client_id: The partial or full ID to search for.
        :return: A list of client records that match the provided ID.
        """
        if len(client_id) == 0:
            return self.records
        filtered = []
        for record in self.records:
            if str(record["ID"]).startswith(client_id):
                filtered.append(record)
        return filtered

    def update(self, updated_record: dict):
        """
        Updates an existing client record.

        :param updated_record: The updated client record (as a dictionary).
        """
        for idx, client in enumerate(self.records):
            if client["ID"] == updated_record["ID"]:
                self.records[idx] = updated_record
                break
        self.save_records()

    def delete(self, record: dict):
        """
        Deletes a client record from the repository.

        :param record: The client record to delete (as a dictionary).
        """
        for idx, client in enumerate(self.records):
            if client["ID"] == record["ID"]:
                del self.records[idx]
                break
        self.save_records()