import customtkinter as ctk
from .edit_client_modal import EditClientModal
from data import ClientRepository


class ClientsView:
    def __init__(self, root, client_repo: ClientRepository):
        self.client_repo = client_repo
        # Main Content Frame (Right side)
        content_frame = ctk.CTkFrame(master=root, fg_color="transparent")
        content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.root = content_frame

        # Search bar
        search_frame = ctk.CTkFrame(
            master=content_frame, width=600, height=50, fg_color="transparent"
        )
        search_frame.pack(fill="x", pady=0)

        dashboard_label = ctk.CTkLabel(
            master=search_frame,
            text="Clients Dashboard",
            font=("Arial", 32, "bold"),
            bg_color="transparent",
        )
        dashboard_label.pack(anchor="w")

        search_label = ctk.CTkLabel(
            master=search_frame,
            text="Search name or ID",
            font=("Arial", 16, "normal"),
            bg_color="transparent",
        )
        search_label.pack(anchor="w")
        self.search_var = ctk.StringVar()
        self.search_var.trace_add("write", self.load_client_data)
        search_entry = ctk.CTkEntry(
            master=search_frame,
            width=200,
            height=30,
            textvariable=self.search_var,
        )
        search_entry.pack(anchor="w", pady=0)

        # Client Table Header
        self.table_frame = ctk.CTkFrame(master=content_frame)
        self.table_frame.pack(fill="both", expand=True)

        header_frame = ctk.CTkFrame(master=self.table_frame)
        header_frame.pack(fill="x", pady=10)

        headers = [
            "Client ID",
            "Type",
            "Name",
            "Address Line 1",
            "City",
            "State",
            "Zip Code",
            "Country",
            "Phone No.",
        ]
        for header in headers:
            label = ctk.CTkLabel(
                master=header_frame, text=header, width=10, font=("Arial", 10, "bold")
            )
            label.pack(side="left", padx=10)

        # Add "View" button header
        label = ctk.CTkLabel(
            master=header_frame, text="View", width=10, font=("Arial", 10, "bold")
        )
        label.pack(side="left", padx=10)

        # Load and display initial client data
        self.load_client_data()

    def load_client_data(self, *args):
        """Load and display client data from the repository."""
        # Clear old data
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Display the headers again
        header_frame = ctk.CTkFrame(master=self.table_frame)
        header_frame.pack(fill="x", pady=10)
        headers = [
            "Client ID",
            "Type",
            "Name",
            "Address Line 1",
            "City",
            "State",
            "Zip Code",
            "Country",
            "Phone No.",
        ]
        for header in headers:
            label = ctk.CTkLabel(
                master=header_frame, text=header, width=10, font=("Arial", 10, "bold")
            )
            label.pack(side="left", padx=10)

        # Add "View" button header
        label = ctk.CTkLabel(
            master=header_frame, text="View", width=10, font=("Arial", 10, "bold")
        )
        label.pack(side="left", padx=10)

        # Fetching client data from the repository
        client_data = self.client_repo.list()
        search_value = self.search_var.get()
        if search_value != "":
            if str.isdigit(search_value):
                client_data = self.client_repo.search_by_id(search_value)
            else:
                client_data = self.client_repo.search_by_name(search_value)

        # Display client data in the UI
        for client in client_data:
            row_frame = ctk.CTkFrame(master=self.table_frame)
            row_frame.pack(fill="x", pady=5)

            for key in [
                "ID",
                "Type",
                "Name",
                "Address_Line_1",
                "City",
                "State",
                "Zip_Code",
                "Country",
                "Phone_Number",
            ]:
                value = client.get(key, "")
                data_label = ctk.CTkLabel(master=row_frame, text=value, width=10)
                data_label.pack(side="left", padx=10)

            # View button for each client
            view_button = ctk.CTkButton(
                master=row_frame,
                text="View",
                width=10,
                command=lambda c=client: self.view_client(c),
            )
            view_button.pack(side="left", padx=10)

    def view_client(self, client):
        EditClientModal(client, self.client_repo, self.load_client_data)

    def destroy(self):
        self.root.destroy()
