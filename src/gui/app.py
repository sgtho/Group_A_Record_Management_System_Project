import customtkinter as ctk
from data import ClientRepository, AirlineRepository, FlightRepository
import gui.components as components


class App:
    def __init__(
        self,
        client_repo: ClientRepository,
        airline_repo: AirlineRepository,
        flight_repo: FlightRepository,
    ):
        self.client_repo = client_repo
        self.airline_repo = airline_repo
        self.flight_repo = flight_repo
        self.active_tab = "client"
        self.build_app()

    def start(self):
        self.app.mainloop()

    def build_app(self):
        self.app = ctk.CTk()
        self.app.geometry("1000x500")
        self.app.title("Travel Wings - Client Dashboard")
        self.app.focus_force()

        # Configure grid layout (2 columns: sidebar and main content)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=4)
        self.app.grid_rowconfigure(0, weight=1)

        self.sidebar = components.Sidebar(
            root=self.app,
            view_change_handler=self.handle_view_change,
            create_handler=self.handle_create,
            active_tab=self.active_tab,
        )

        self.active_view = components.ClientsView(
            root=self.app, client_repo=self.client_repo
        )

    def handle_view_change(self, view):
        self.active_tab = view
        self.active_view.destroy()
        if view == "client":
            self.active_view = components.ClientsView(
                root=self.app, client_repo=self.client_repo
            )
        elif view == "flight":
            self.active_view = components.FlightsView(
                root=self.app, flight_repo=self.flight_repo
            )
        else:
            self.active_view = components.AirlinesView(
                root=self.app, airline_repo=self.airline_repo
            )

    def update_view(self):
        self.handle_view_change(self.active_tab)

    def handle_create(self, record_type):
        if record_type == "client":
            self.add_client()
        elif record_type == "flight":
            self.add_flight()
        else:
            self.add_airline()

    def add_client(self):
        components.CreateClientModal(self.client_repo, self.update_view)

    def add_flight(self):
        components.CreateFlightModal(self.flight_repo, self.update_view)

    def add_airline(self):
        components.CreateAirlineModal(self.airline_repo, self.update_view)
