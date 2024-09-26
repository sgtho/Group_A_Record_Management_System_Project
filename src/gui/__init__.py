import customtkinter as ctk
from data.client_repository import ClientRepository  # Importing ClientRepository

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
        app.title("Travel Wings - Client Dashboard")

        # Configure grid layout (2 columns: sidebar and main content)
        app.grid_columnconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=3)
        app.grid_rowconfigure(0, weight=1)

        # Sidebar Frame (Left side)
        sidebar_frame = ctk.CTkFrame(master=app, width=200)
        sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        # Sidebar Content
        sidebar_logo = ctk.CTkLabel(master=sidebar_frame, text="TRAVEL\nWINGS", font=("Arial", 24, "bold"), justify="center")
        sidebar_logo.pack(pady=30)

        # Buttons in sidebar
        client_button = ctk.CTkButton(master=sidebar_frame, text="Client", width=160, corner_radius=10)
        client_button.pack(pady=10)

        flight_button = ctk.CTkButton(master=sidebar_frame, text="Flight", width=160, corner_radius=10)
        flight_button.pack(pady=10)

        airline_button = ctk.CTkButton(master=sidebar_frame, text="Airline", width=160, corner_radius=10)
        airline_button.pack(pady=10)

        # New record buttons at bottom of sidebar
        add_client_button = ctk.CTkButton(master=sidebar_frame, text="+ New Client", width=160, corner_radius=10, command=self.open_new_client_window)
        add_client_button.pack(pady=20, side="bottom")

        add_flight_button = ctk.CTkButton(master=sidebar_frame, text="+ New Flight", width=160, corner_radius=10)
        add_flight_button.pack(pady=10, side="bottom")

        add_airline_button = ctk.CTkButton(master=sidebar_frame, text="+ New Airline", width=160, corner_radius=10)
        add_airline_button.pack(pady=10, side="bottom")

        # Main Content Frame (Right side)
        content_frame = ctk.CTkFrame(master=app)
        content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Search bar
        search_frame = ctk.CTkFrame(master=content_frame, width=600, height=50)
        search_frame.pack(fill="x", pady=20)

        search_label = ctk.CTkLabel(master=search_frame, text="Client Dashboard", font=("Arial", 24, "bold"))
        search_label.pack(anchor="w")

        search_entry = ctk.CTkEntry(master=search_frame, width=400, placeholder_text="Search name or ID...")
        search_entry.pack(side="left", padx=10, pady=10)

        # Client Table Header
        table_frame = ctk.CTkFrame(master=content_frame)
        table_frame.pack(fill="both", expand=True)

        header_frame = ctk.CTkFrame(master=table_frame)
        header_frame.pack(fill="x", pady=10)

        headers = ["Client ID", "Type", "Name", "Address Line 1", "City", "State", "Zip Code", "Country", "Phone No."]
        for header in headers:
            label = ctk.CTkLabel(master=header_frame, text=header, width=10, font=("Arial", 10, "bold"))
            label.pack(side="left", padx=10)

        # Client Data
        data_frame = ctk.CTkFrame(master=table_frame)
        data_frame.pack(fill="both", expand=True)

        # Fetching client data from the repository
        client_data = self.client_repo.list()

        # Display client data in the UI
        for client in client_data:
            row_frame = ctk.CTkFrame(master=data_frame)
            row_frame.pack(fill="x", pady=5)

            for key in ["ID", "Type", "Name", "Address_Line_1", "City", "State", "Zip_Code", "Country", "Phone_Number"]:
                value = client.get(key, "")
                data_label = ctk.CTkLabel(master=row_frame, text=value, width=10)
                data_label.pack(side="left", padx=10)

        self.app = app

    def open_new_client_window(self):
        new_window = ctk.CTkToplevel()
        new_window.title("New Client")
        new_window.geometry("800x600")

        # Input fields for client information
        def save_client():
            new_client = {
                "Name": name_entry.get(),
                "Phone_Number": phone_entry.get(),
                "Address_Line_1": line1_entry.get(),
                "Address_Line_2": line2_entry.get(),
                "Address_Line_3": line3_entry.get(),
                "City": city_entry.get(),
                "State": state_entry.get(),
                "Zip_Code": zip_entry.get(),
                "Country": country_entry.get(),
                "Type": "Customer"  # Assuming all clients are "Customer"
            }
            self.client_repo.create(new_client)  # Save to clients.jsonl
            new_window.destroy()  # Close the window after saving

        # Client Info (Contact)
        ctk.CTkLabel(new_window, text="New Client", font=("Arial", 20, "bold")).pack(pady=10)
        ctk.CTkLabel(new_window, text="Contact", font=("Arial", 16, "bold")).pack(anchor="w", padx=20)

        contact_frame = ctk.CTkFrame(new_window)
        contact_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(contact_frame, text="Client Name: *").grid(row=0, column=0, padx=10, pady=5)
        name_entry = ctk.CTkEntry(contact_frame, width=300)
        name_entry.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(contact_frame, text="Phone No.: *").grid(row=0, column=2, padx=10)
        phone_entry = ctk.CTkEntry(contact_frame, width=300)
        phone_entry.grid(row=0, column=3, padx=10)

        # Client Info (Address)
        ctk.CTkLabel(new_window, text="Address", font=("Arial", 16, "bold")).pack(anchor="w", padx=20)
        
        address_frame = ctk.CTkFrame(new_window)
        address_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(address_frame, text="Line 1: *").grid(row=0, column=0, padx=10, pady=5)
        line1_entry = ctk.CTkEntry(address_frame, width=300)
        line1_entry.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(address_frame, text="Line 2:").grid(row=1, column=0, padx=10, pady=5)
        line2_entry = ctk.CTkEntry(address_frame, width=300)
        line2_entry.grid(row=1, column=1, padx=10)

        ctk.CTkLabel(address_frame, text="Line 3:").grid(row=2, column=0, padx=10, pady=5)
        line3_entry = ctk.CTkEntry(address_frame, width=300)
        line3_entry.grid(row=2, column=1, padx=10)

        ctk.CTkLabel(address_frame, text="City: *").grid(row=0, column=2, padx=10)
        city_entry = ctk.CTkEntry(address_frame, width=200)
        city_entry.grid(row=0, column=3, padx=10)

        ctk.CTkLabel(address_frame, text="State: *").grid(row=1, column=2, padx=10)
        state_entry = ctk.CTkEntry(address_frame, width=200)
        state_entry.grid(row=1, column=3, padx=10)

        ctk.CTkLabel(address_frame, text="Zip Code: *").grid(row=2, column=2, padx=10)
        zip_entry = ctk.CTkEntry(address_frame, width=200)
        zip_entry.grid(row=2, column=3, padx=10)

        ctk.CTkLabel(address_frame, text="Country: *").grid(row=3, column=0, padx=10, pady=5)
        country_entry = ctk.CTkEntry(address_frame, width=300)
        country_entry.grid(row=3, column=1, padx=10)

        # Save and Close buttons
        button_frame = ctk.CTkFrame(new_window)
        button_frame.pack(pady=20)

        close_button = ctk.CTkButton(button_frame, text="Close", fg_color="red", width=100, command=new_window.destroy)
        close_button.pack(side="left", padx=20)

        save_button = ctk.CTkButton(button_frame, text="Save", fg_color="green", width=100, command=save_client)
        save_button.pack(side="right", padx=20)

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
