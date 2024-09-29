from gui import App
from data import ClientRepository, AirlineRepository

client_repo = ClientRepository("src/record/clients.jsonl")
airline_repo = AirlineRepository("src/record/airlines.jsonl")

app = App(client_repo, airline_repo)

app.start()
