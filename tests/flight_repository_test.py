import unittest
import json
import os
from src.data.flight_repository import FlightRepository


class TestFlightRepository(unittest.TestCase):

    def setUp(self):
        """
        This method is called before each test. It sets up a temporary file and initial records for testing.
        """
        self.filename = "test_flights.jsonl"

        self.initial_records = [
            {   "ID": 101,
                "Client_ID": 1, 
                "Airline_ID": 201,
                "Type": "Flight", 
                "Date_Time": "30 Sep 2024 10:10",
                "Start_City": "Los Gatos",
                "End_City": "UK"
            },
            {   "ID": 102,
                "Client_ID": 2, 
                "Airline_ID": 202,
                "Type": "Flight", 
                "Date_Time": "30 OCt 2024 22:22",
                "Start_City": "Los Angeles",
                "End_City": "Germany"
            },
        ]
        with open(self.filename, "w") as file:
            for record in self.initial_records:
                file.write(json.dumps(record) + "\n")
        self.repo = FlightRepository(self.filename)

    def tearDown(self):
        """
        This method is called after each test. It cleans up by removing the temporary test file.
        """
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load_records(self):
        """
        Test that records are loaded correctly from the file.
        """
        records = self.repo.load_records()
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]["ID"], 101)
        self.assertEqual(records[1]["ID"], 102)

    def test_create_record(self):
        """
        Test that a new record is added successfully.
        """
        new_record = {
                "ID": 901,
                "Client_ID": 3, 
                "Airline_ID": 902,
                "Type": "Flight", 
                "Date_Time": "01 Jan 2025 00:00",
                "Start_City": "Italy",
                "End_City": "Finland"
            }

        self.repo.create(new_record)

        records = self.repo.list()
        self.assertEqual(len(records), 3)
        self.assertIn(new_record, records)

    def test_list_records(self):
        """
        Test that all records are listed correctly.
        """
        records = self.repo.list()
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]["ID"], 101)
        self.assertEqual(records[1]["ID"], 102)

    def test_get_record_by_id(self):
        """
        Test that a record can be retrieved by its ID.
        """
        record = self.repo.get(101)
        self.assertIsNotNone(record)
        self.assertEqual(record["ID"], 101)

        record = self.repo.get(999)  # Non-existing ID
        self.assertIsNone(record)

    def test_search_by_start_city(self):
        """
        Test that records can be searched by start city.
        """
        result = self.repo.search_by_start_city("Los")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["Start_City"], "Los Gatos")

        result = self.repo.search_by_start_city("New")
        self.assertEqual(len(result), 0)

    def test_search_by_id(self):
        """
        Test that records can be searched by ID.
        """
        result = self.repo.search_by_id("101")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["ID"], 101)

        result = self.repo.search_by_id("0")
        self.assertEqual(len(result), 0)

    def test_update_record(self):
        """
        Test that an existing record is updated correctly.
        """
        updated_record = {
                "ID": 101,
                "Client_ID": 8, 
                "Airline_ID": 802,
                "Type": "Flight", 
                "Date_Time": "01 Feb 2025 20:00",
                "Start_City": "Finland",
                "End_City": "Italy"
        }

        self.repo.update(updated_record)

        record = self.repo.get(101)
        self.assertEqual(record["Client_ID"], 8)

    def test_delete_record(self):
        """
        Test that a record is deleted successfully.
        """
        record_to_delete = {
                "ID": 101,
                "Client_ID": 8, 
                "Airline_ID": 802,
                "Type": "Flight", 
                "Date_Time": "01 Feb 2025 20:00",
                "Start_City": "Finland",
                "End_City": "Italy"
        }
        self.repo.delete(record_to_delete)

        records = self.repo.list()
        self.assertEqual(len(records), 1)
        self.assertNotIn(record_to_delete, records)


if __name__ == "__main__":
    unittest.main()
