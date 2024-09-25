import customtkinter as ctk
from data.client_repository import ClientRepository

class App:
    def __init__(self, client_repo: ClientRepository):
        self.client_repo = client_repo

        # build UI
        self.build_app()

    def start(self):
        self.app.mainloop()

    def build_app(self):
        app = ctk.CTk()  
        app.geometry("1000x500")
        app.title("Group A - Record Management System")

        # Top frame: Search bar and label
        top_frame = ctk.CTkFrame(master=app)
        top_frame.pack(pady=10, padx=10, fill="x")

        search_label = ctk.CTkLabel(master=top_frame, text="Search Client:")
        search_label.pack(side="left", padx=10)

        search_entry = ctk.CTkEntry(master=top_frame, width=300, placeholder_text="Enter client name or ID")
        search_entry.pack(side="left", padx=10)

        search_button = ctk.CTkButton(master=top_frame, text="Search", command=self.search_client)
        search_button.pack(side="left", padx=10)

        # Middle frame: Client list and action buttons
        middle_frame = ctk.CTkFrame(master=app)
        middle_frame.pack(side="left", padx=20, pady=10, fill="y")

        # Left frame: Client actions (Add, Edit, Delete)
        left_frame = ctk.CTkFrame(master=middle_frame, width=200)
        left_frame.pack(pady=10, padx=10, fill="both", expand=True)

        add_button_client = ctk.CTkButton(master=left_frame, text="Add Client", command=self.add_client)
        add_button_client.pack(pady=10, fill="x")

        add_button_flight = ctk.CTkButton(master=left_frame, text="Add Flight", command=self.add_flight)
        add_button_flight.pack(pady=10, fill="x")

        add_button_airline = ctk.CTkButton(master=left_frame, text="Add Airline", command=self.add_airline)
        add_button_airline.pack(pady=10, fill="x")

        #Bottom frame: Client Dashboard
        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(pady=10, padx=10, fill="x")

        #Here we put our client table
        client_details_textbox = ctk.CTkTextbox(master=bottom_frame, height=500)
        client_details_textbox.pack(pady=10, fill="x")    

        self.app = app

    def search_client(self):
        # Search client logic
        print("Searching client...")

    def add_client(self):
        # Add client logic
        print("Adding client...")

    def add_flight(self):
        # Add flight logic
        print("Adding flight...")

    def add_airline(self):
        # Add airline logic
        print("Adding airline...")

