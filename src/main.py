from gui import App
from data.client_repository import ClientRepository

client_repo = ClientRepository("src/record/clients.jsonl")

app = App(client_repo)

app.start()