from gui import App
from data import ClientRepository, AirlineRepository, FlightRepository

client_repo = ClientRepository("src/record/clients.jsonl")
airline_repo = AirlineRepository("src/record/airlines.jsonl")
flight_repo = FlightRepository("src/record/flights.jsonl")

app = App(client_repo=client_repo, airline_repo=airline_repo, flight_repo=flight_repo)

app.start()
