# Record_Management_System_Project
This group project is to design a record management system for a specialist travel agent. The system will manage three types of records: 1. Client records, 2. Flight Records and 3. Airline Company records.

### How do I get set up? ###
Using the terminal, on MacOS/Linux systems, from inside this project directory run:
```
source .venv/bin/activate
```

If using windows, you will need to run (Command Prompt):
```
.venv\Scripts\activate
```

If using PyCharm it should automatically detect the `.venv` directory and will show a banner which you can click
to use the `.venv` configuration.

# Running the code
To start the application you can run:
```
python src/main.py
```

# Running the tests
To run all the test files under the `tests/` directory you can run:
```
python -m unittest discover -s tests -p "*_test.py"
```