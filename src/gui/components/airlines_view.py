import customtkinter as ctk
from data import AirlineRepository
from .edit_airline_modal import EditAirlineModal


class AirlinesView:
    def __init__(self, root, airline_repo: AirlineRepository):
        self.airline_repo = airline_repo
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
            text="Airlines Dashboard",
            font=("Arial", 32, "bold"),
            bg_color="transparent",
        )
        dashboard_label.pack(anchor="w")

        search_label = ctk.CTkLabel(
            master=search_frame,
            text="Search start city or ID",
            font=("Arial", 16, "normal"),
            bg_color="transparent",
        )
        search_label.pack(anchor="w")
        self.search_var = ctk.StringVar()
        self.search_var.trace_add("write", self.load_airline_data)
        search_entry = ctk.CTkEntry(
            master=search_frame,
            width=200,
            height=30,
            textvariable=self.search_var,
        )
        search_entry.pack(anchor="w", pady=0)

        # Airline Table Header
        self.table_frame = ctk.CTkFrame(master=content_frame)
        self.table_frame.pack(fill="both", expand=True)

        header_frame = ctk.CTkFrame(master=self.table_frame)
        header_frame.pack(fill="x", pady=10)

        headers = ["Airline ID", "Type", "Company Name"]
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

        # Load and display initial airline data
        self.load_airline_data()

    def load_airline_data(self, *args):
        """Load and display airlinr data from the repository."""
        # Clear old data
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Display the headers again
        header_frame = ctk.CTkFrame(master=self.table_frame)
        header_frame.pack(fill="x", pady=10)
        headers = ["Airline ID", "Type", "Company Name"]
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

        # Fetching airline data from the repository
        airline_data = self.airline_repo.list()
        search_value = self.search_var.get()
        if search_value != "":
            if str.isdigit(search_value):
                airline_data = self.airline_repo.search_by_id(search_value)
            else:
                airline_data = self.airline_repo.search_by_name(search_value)

        # Display airline data in the UI
        for airline in airline_data:
            row_frame = ctk.CTkFrame(master=self.table_frame)
            row_frame.pack(fill="x", pady=5)

            for key in ["ID", "Type", "Company_Name"]:
                value = airline.get(key, "")
                data_label = ctk.CTkLabel(master=row_frame, text=value, width=10)
                data_label.pack(side="left", padx=10)

            # View button for each airline
            view_button = ctk.CTkButton(
                master=row_frame,
                text="View",
                width=10,
                command=lambda c=airline: self.view_airline(c),
            )
            view_button.pack(side="left", padx=10)

    def view_airline(self, airline):
        EditAirlineModal(airline, self.airline_repo, self.load_airline_data)

    def destroy(self):
        self.root.destroy()
