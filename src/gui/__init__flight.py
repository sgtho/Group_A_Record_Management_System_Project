import customtkinter as ctk
from data.flight_repository import FlightRepository  # Importing FlightRepository

class App:
    def __init__(self, flight_repo: FlightRepository):
        self.flight_repo = flight_repo
        # build UI
        self.build_app()

    def start(self):
        self.app.mainloop()

    def build_app(self):
        self.app = ctk.CTk()
        self.app.geometry("1000x500")
        self.app.title("Travel Wings - Flight Dashboard")

        # Configure grid layout (2 columns: sidebar and main content)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=3)
        self.app.grid_rowconfigure(0, weight=1)

        # Sidebar Frame (Left side)
        sidebar_frame = ctk.CTkFrame(master=self.app, width=200)
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
        add_client_button = ctk.CTkButton(master=sidebar_frame, text="+ New Client", width=160, corner_radius=10)
        add_client_button.pack(pady=20, side="bottom")

        add_flight_button = ctk.CTkButton(master=sidebar_frame, text="+ New Flight", width=160, corner_radius=10, command=self.open_new_flight_window)
        add_flight_button.pack(pady=10, side="bottom")

        add_airline_button = ctk.CTkButton(master=sidebar_frame, text="+ New Airline", width=160, corner_radius=10)
        add_airline_button.pack(pady=10, side="bottom")

        # Main Content Frame (Right side)
        content_frame = ctk.CTkFrame(master=self.app)
        content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Search bar
        search_frame = ctk.CTkFrame(master=content_frame, width=600, height=50)
        search_frame.pack(fill="x", pady=20)

        search_label = ctk.CTkLabel(master=search_frame, text="Flight Dashboard", font=("Arial", 24, "bold"))
        search_label.pack(anchor="w")

        search_entry = ctk.CTkEntry(master=search_frame, width=400, placeholder_text="Search Booking Number or Client ID...")
        search_entry.pack(side="left", padx=10, pady=10)

        # Flight Table Header
        self.table_frame = ctk.CTkFrame(master=content_frame)
        self.table_frame.pack(fill="both", expand=True)

        header_frame = ctk.CTkFrame(master=self.table_frame)
        header_frame.pack(fill="x", pady=10)

        headers = ["Booking Number", "Client ID", "Airline ID", "Type", "Date/Time", "Start City", "End City"]
        for header in headers:
            label = ctk.CTkLabel(master=header_frame, text=header, width=10, font=("Arial", 10, "bold"))
            label.pack(side="left", padx=10)

        # Add "View" button header
        label = ctk.CTkLabel(master=header_frame, text="View", width=10, font=("Arial", 10, "bold"))
        label.pack(side="left", padx=10)

        # Load and display initial flight data
        self.load_flight_data()

    def load_flight_data(self):
        """Load and display flight data from the repository."""
        # Clear old data
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Display the headers again
        header_frame = ctk.CTkFrame(master=self.table_frame)
        header_frame.pack(fill="x", pady=10)
        headers = ["Booking Number", "Client ID", "Airline ID", "Type", "Date/Time", "Start City", "End City"]
        for header in headers:
            label = ctk.CTkLabel(master=header_frame, text=header, width=10, font=("Arial", 10, "bold"))
            label.pack(side="left", padx=10)

        # Add "View" button header
        label = ctk.CTkLabel(master=header_frame, text="View", width=10, font=("Arial", 10, "bold"))
        label.pack(side="left", padx=10)

        # Fetching flight data from the repository
        flight_data = self.flight_repo.list()

        # Display flight data in the UI
        for flight in flight_data:
            row_frame = ctk.CTkFrame(master=self.table_frame)
            row_frame.pack(fill="x", pady=5)

            for key in ["Booking_Number", "Client_ID", "Airline_ID", "Type", "Date_Time", "Start_City", "End_City"]:
                value = flight.get(key, "")
                data_label = ctk.CTkLabel(master=row_frame, text=value, width=10)
                data_label.pack(side="left", padx=10)

            # View button for each flight
            view_button = ctk.CTkButton(master=row_frame, text="View", width=10, command=lambda c=flight: self.view_flight(c))
            view_button.pack(side="left", padx=10)

    def open_new_flight_window(self):
        """Method to open a new window for adding a new flight."""
        new_window = ctk.CTkToplevel()
        new_window.title("New flight")
        new_window.geometry("800x600")

        # Input fields for flight information
        def save_flight():
            new_flight = {
                "Booking_Number": len(self.flight_repo.list()) + 1,  # Auto-incrementing ID
                "Client_ID": client_id_entry.get(),
                "Airline_ID": airline_id_entry.get(),
                "Type": "Flight",  # Type is set to "flight"
                "Date_Time": date_time_entry.get(),
                "Start_City": start_city_entry.get(),
                "End_City": end_city_entry.get(),
            }
            self.flight_repo.create(new_flight)  # Save to flights.jsonl
            self.load_flight_data()  # Reload the flight table to show the new record
            new_window.destroy()  # Close the window after saving

        # Flight Info (Identification)
        ctk.CTkLabel(new_window, text="New Flight", font=("Arial", 20, "bold")).pack(pady=10)
        ctk.CTkLabel(new_window, text="Flight", font=("Arial", 16, "bold")).pack(anchor="w", padx=20)

        id_frame = ctk.CTkFrame(new_window)
        id_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(id_frame, text="Client ID: *").grid(row=0, column=0, padx=10, pady=5)
        client_id_entry = ctk.CTkEntry(id_frame, width=300)
        client_id_entry.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(id_frame, text="Airline ID: *").grid(row=0, column=2, padx=10)
        airline_id_entry = ctk.CTkEntry(id_frame, width=300)
        airline_id_entry.grid(row=0, column=3, padx=10)

        # Flight Info (Journey)
        ctk.CTkLabel(new_window, text="Journey", font=("Arial", 16, "bold")).pack(anchor="w", padx=20)

        journey_frame = ctk.CTkFrame(new_window)
        journey_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(journey_frame, text="Date/Time: *").grid(row=0, column=0, padx=10, pady=5)
        date_time_entry = ctk.CTkEntry(journey_frame, width=300)
        date_time_entry.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(journey_frame, text="Start City:").grid(row=1, column=0, padx=10, pady=5)
        start_city_entry = ctk.CTkEntry(journey_frame, width=300)
        start_city_entry.grid(row=1, column=1, padx=10)

        ctk.CTkLabel(journey_frame, text="End City:").grid(row=2, column=0, padx=10, pady=5)
        end_city_entry = ctk.CTkEntry(journey_frame, width=300)
        end_city_entry.grid(row=2, column=1, padx=10)


        # Save and Close buttons
        button_frame = ctk.CTkFrame(new_window)
        button_frame.pack(pady=20)

        close_button = ctk.CTkButton(button_frame, text="Close", fg_color="red", width=100, command=new_window.destroy)
        close_button.pack(side="left", padx=20)

        save_button = ctk.CTkButton(button_frame, text="Save", fg_color="green", width=100, command=save_flight)
        save_button.pack(side="right", padx=20)

    def view_flight(self, flight):
        """Open the flight details in view mode."""
        view_window = ctk.CTkToplevel()
        view_window.title(f"Booking Number #{flight['Booking_Number']}")
        view_window.geometry("800x600")

        # Display flight details (View mode)
        def enable_edit():
            """Enable editing mode for the flight details."""
            client_id_entry.configure(state="normal")
            airline_id_entry.configure(state="normal")
            date_time_entry.configure(state="normal")
            start_city_entry.configure(state="normal")
            end_city_entry.configure(state="normal")
            
            edit_button.pack_forget()  # Hide Edit button in edit mode
            # Show Update and Delete buttons in edit mode
            update_button.pack(side="right", padx=10)
            delete_button.pack(side="right", padx=10)
            back_button.pack(side="left", padx=10)

        def disable_edit():
            """Disable editing mode (Back to view mode)."""
            client_id_entry.configure(state="disabled")
            airline_id_entry.configure(state="disabled")
            date_time_entry.configure(state="disabled")
            start_city_entry.configure(state="disabled")
            end_city_entry.configure(state="disabled")
            back_button.pack_forget()
            update_button.pack_forget()
            delete_button.pack_forget()
            edit_button.pack(side="right", padx=10)

        def confirm_update():
            """Confirmation window for updating flight details."""
            confirmation_window = ctk.CTkToplevel(view_window)
            confirmation_window.title("Confirm Update")
            confirmation_window.geometry("400x200")

            # Warning Label
            ctk.CTkLabel(confirmation_window, text="Once you update the record, it cannot be recovered.\nAre you sure you want to update?", font=("Arial", 14, "bold")).pack(pady=20)

            # Button Frame for update and cancel options
            button_frame = ctk.CTkFrame(confirmation_window)
            button_frame.pack(pady=20)

            def confirm():
                # Once confirmed, update the flight record
                updated_flight = {
                    "Booking_Number": flight['Booking_Number'],
                    "Client_ID": client_id_entry.get(),
                    "Airline_ID": airline_id_entry.get(),
                    "Type": "Flight",
                    "Date_Time": date_time_entry.get(),
                    "Start_City": start_city_entry.get(),
                    "End_City": end_city_entry.get(),
                }
                self.flight_repo.update(updated_flight)  # Save the updated flight details
                confirmation_window.destroy()
                view_window.destroy()  # Close the window after updating
                self.load_flight_data()  # Refresh the table to reflect changes

            update_button = ctk.CTkButton(button_frame, text="Update", fg_color="green", width=100, command=confirm)
            update_button.pack(side="left", padx=10)

            cancel_button = ctk.CTkButton(button_frame, text="Cancel", fg_color="gray", width=100, command=confirmation_window.destroy)
            cancel_button.pack(side="right", padx=10)

        def delete_flight():
            """Delete the given flight from the repository."""
            # Pop-up confirmation window for deletion
            confirmation_window = ctk.CTkToplevel(view_window)
            confirmation_window.title("Confirm Deletion")
            confirmation_window.geometry("400x200")

            ctk.CTkLabel(confirmation_window, text="Are you sure to delete?", font=("Arial", 18, "bold")).pack(pady=20)

            # Button Frame for delete and cancel options
            button_frame = ctk.CTkFrame(confirmation_window)
            button_frame.pack(pady=20)

            def confirm_delete():
                self.flight_repo.delete(flight)  # Delete the flight from repository
                confirmation_window.destroy()  # Close the confirmation window
                view_window.destroy()  # Close the main flight window after deletion
                self.load_flight_data()  # Refresh the table to reflect changes

            delete_button = ctk.CTkButton(button_frame, text="Delete", fg_color="red", width=100, command=confirm_delete)
            delete_button.pack(side="left", padx=10)

            cancel_button = ctk.CTkButton(button_frame, text="Cancel", fg_color="gray", width=100, command=confirmation_window.destroy)
            cancel_button.pack(side="right", padx=10)

        # Booking Number
        ctk.CTkLabel(view_window, text=f"Booking Number #{flight['Booking_Number']}", font=("Arial", 24, "bold")).pack(pady=10)

        # Indentification
        id_frame = ctk.CTkFrame(view_window)
        id_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(id_frame, text="Client ID: *").grid(row=0, column=0, padx=10, pady=5)
        client_id_entry = ctk.CTkEntry(id_frame, width=300)
        client_id_entry.insert(0, flight["Client_ID"])
        client_id_entry.grid(row=0, column=1, padx=10)
        client_id_entry.configure(state="disabled")  # Initially in view-only mode

        ctk.CTkLabel(id_frame, text="Airline ID.: *").grid(row=0, column=2, padx=10)
        airline_id_entry = ctk.CTkEntry(id_frame, width=300)
        airline_id_entry.insert(0, flight["Airline_ID"])
        airline_id_entry.grid(row=0, column=3, padx=10)
        airline_id_entry.configure(state="disabled")

        # Journet Info
        ctk.CTkLabel(view_window, text="Journey", font=("Arial", 16, "bold")).pack(anchor="w", padx=20)

        journey_frame = ctk.CTkFrame(view_window)
        journey_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(journey_frame, text="Date/Time: *").grid(row=0, column=0, padx=10, pady=5)
        date_time_entry = ctk.CTkEntry(journey_frame, width=300)
        date_time_entry.insert(0, flight["Date_Time"])
        date_time_entry.grid(row=0, column=1, padx=10)
        date_time_entry.configure(state="disabled")

        ctk.CTkLabel(journey_frame, text="Start City:").grid(row=1, column=0, padx=10, pady=5)
        start_city_entry = ctk.CTkEntry(journey_frame, width=300)
        start_city_entry.insert(0, flight["Start_City"])
        start_city_entry.grid(row=1, column=1, padx=10)
        start_city_entry.configure(state="disabled")

        ctk.CTkLabel(journey_frame, text="End City:").grid(row=2, column=0, padx=10, pady=5)
        end_city_entry = ctk.CTkEntry(journey_frame, width=300)
        end_city_entry.insert(0, flight["End_City"])
        end_city_entry.grid(row=2, column=1, padx=10)
        end_city_entry.configure(state="disabled")

        # Buttons (View Mode)
        button_frame = ctk.CTkFrame(view_window)
        button_frame.pack(pady=20)

        # Removed "Close" button and added "Update" button in edit mode
        edit_button = ctk.CTkButton(button_frame, text="Edit", width=100, command=enable_edit)
        edit_button.pack(side="right", padx=10)

        # Buttons for Edit Mode
        back_button = ctk.CTkButton(button_frame, text="Back", fg_color="gray", width=100, command=disable_edit)
        update_button = ctk.CTkButton(button_frame, text="Update", fg_color="green", width=100, command=confirm_update)
        delete_button = ctk.CTkButton(button_frame, text="Delete", fg_color="red", width=100, command=delete_flight)

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
