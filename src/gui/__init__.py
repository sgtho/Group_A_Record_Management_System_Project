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
        self.app = ctk.CTk()
        self.app.geometry("1000x500")
        self.app.title("Travel Wings - Client Dashboard")

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
        add_client_button = ctk.CTkButton(master=sidebar_frame, text="+ New Client", width=160, corner_radius=10, command=self.open_new_client_window)
        add_client_button.pack(pady=20, side="bottom")

        add_flight_button = ctk.CTkButton(master=sidebar_frame, text="+ New Flight", width=160, corner_radius=10)
        add_flight_button.pack(pady=10, side="bottom")

        add_airline_button = ctk.CTkButton(master=sidebar_frame, text="+ New Airline", width=160, corner_radius=10)
        add_airline_button.pack(pady=10, side="bottom")

        # Main Content Frame (Right side)
        content_frame = ctk.CTkFrame(master=self.app)
        content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Search bar
        search_frame = ctk.CTkFrame(master=content_frame, width=600, height=50)
        search_frame.pack(fill="x", pady=20)

        search_label = ctk.CTkLabel(master=search_frame, text="Client Dashboard", font=("Arial", 24, "bold"))
        search_label.pack(anchor="w")

        search_entry = ctk.CTkEntry(master=search_frame, width=400, placeholder_text="Search name or ID...")
        search_entry.pack(side="left", padx=10, pady=10)

        # Client Table Header
        self.table_frame = ctk.CTkFrame(master=content_frame)
        self.table_frame.pack(fill="both", expand=True)

        header_frame = ctk.CTkFrame(master=self.table_frame)
        header_frame.pack(fill="x", pady=10)

        headers = ["Client ID", "Type", "Name", "Address Line 1", "City", "State", "Zip Code", "Country", "Phone No."]
        for header in headers:
            label = ctk.CTkLabel(master=header_frame, text=header, width=10, font=("Arial", 10, "bold"))
            label.pack(side="left", padx=10)

        # Add "View" button header
        label = ctk.CTkLabel(master=header_frame, text="View", width=10, font=("Arial", 10, "bold"))
        label.pack(side="left", padx=10)

        # Load and display initial client data
        self.load_client_data()

    def load_client_data(self):
        """Load and display client data from the repository."""
        # Clear old data
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Display the headers again
        header_frame = ctk.CTkFrame(master=self.table_frame)
        header_frame.pack(fill="x", pady=10)
        headers = ["Client ID", "Type", "Name", "Address Line 1", "City", "State", "Zip Code", "Country", "Phone No."]
        for header in headers:
            label = ctk.CTkLabel(master=header_frame, text=header, width=10, font=("Arial", 10, "bold"))
            label.pack(side="left", padx=10)

        # Add "View" button header
        label = ctk.CTkLabel(master=header_frame, text="View", width=10, font=("Arial", 10, "bold"))
        label.pack(side="left", padx=10)

        # Fetching client data from the repository
        client_data = self.client_repo.list()

        # Display client data in the UI
        for client in client_data:
            row_frame = ctk.CTkFrame(master=self.table_frame)
            row_frame.pack(fill="x", pady=5)

            for key in ["ID", "Type", "Name", "Address_Line_1", "City", "State", "Zip_Code", "Country", "Phone_Number"]:
                value = client.get(key, "")
                data_label = ctk.CTkLabel(master=row_frame, text=value, width=10)
                data_label.pack(side="left", padx=10)

            # View button for each client
            view_button = ctk.CTkButton(master=row_frame, text="View", width=10, command=lambda c=client: self.view_client(c))
            view_button.pack(side="left", padx=10)

    def open_new_client_window(self):
        """Method to open a new window for adding a new client."""
        new_window = ctk.CTkToplevel()
        new_window.title("New Client")
        new_window.geometry("800x600")

        # Input fields for client information
        def save_client():
            new_client = {
                "ID": len(self.client_repo.list()) + 1,  # Auto-incrementing ID
                "Type": "Client",  # Type is set to "Client"
                "Name": name_entry.get(),
                "Address_Line_1": line1_entry.get(),
                "Address_Line_2": line2_entry.get(),
                "Address_Line_3": line3_entry.get(),
                "City": city_entry.get(),
                "State": state_entry.get(),
                "Zip_Code": zip_entry.get(),
                "Country": country_entry.get(),
                "Phone_Number": phone_entry.get(),
            }
            self.client_repo.create(new_client)  # Save to clients.jsonl
            self.load_client_data()  # Reload the client table to show the new record
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

    def view_client(self, client):
        """Open the client details in view mode."""
        view_window = ctk.CTkToplevel()
        view_window.title(f"Client ID #{client['ID']}")
        view_window.geometry("800x600")

        # Display client details (View mode)
        def enable_edit():
            """Enable editing mode for the client details."""
            client_name_entry.configure(state="normal")
            phone_entry.configure(state="normal")
            line1_entry.configure(state="normal")
            line2_entry.configure(state="normal")
            line3_entry.configure(state="normal")
            city_entry.configure(state="normal")
            state_entry.configure(state="normal")
            zip_entry.configure(state="normal")
            country_entry.configure(state="normal")
            edit_button.pack_forget()  # Hide Edit button in edit mode
            # Show Update and Delete buttons in edit mode
            update_button.pack(side="right", padx=10)
            delete_button.pack(side="right", padx=10)
            back_button.pack(side="left", padx=10)

        def disable_edit():
            """Disable editing mode (Back to view mode)."""
            client_name_entry.configure(state="disabled")
            phone_entry.configure(state="disabled")
            line1_entry.configure(state="disabled")
            line2_entry.configure(state="disabled")
            line3_entry.configure(state="disabled")
            city_entry.configure(state="disabled")
            state_entry.configure(state="disabled")
            zip_entry.configure(state="disabled")
            country_entry.configure(state="disabled")
            back_button.pack_forget()
            update_button.pack_forget()
            delete_button.pack_forget()
            edit_button.pack(side="right", padx=10)

        def confirm_update():
            """Confirmation window for updating client details."""
            confirmation_window = ctk.CTkToplevel(view_window)
            confirmation_window.title("Confirm Update")
            confirmation_window.geometry("400x200")

            # Warning Label
            ctk.CTkLabel(confirmation_window, text="Once you update the record, it cannot be recovered.\nAre you sure you want to update?", font=("Arial", 14, "bold")).pack(pady=20)

            # Button Frame for update and cancel options
            button_frame = ctk.CTkFrame(confirmation_window)
            button_frame.pack(pady=20)

            def confirm():
                # Once confirmed, update the client record
                updated_client = {
                    "ID": client['ID'],
                    "Type": "Client",
                    "Name": client_name_entry.get(),
                    "Phone_Number": phone_entry.get(),
                    "Address_Line_1": line1_entry.get(),
                    "Address_Line_2": line2_entry.get(),
                    "Address_Line_3": line3_entry.get(),
                    "City": city_entry.get(),
                    "State": state_entry.get(),
                    "Zip_Code": zip_entry.get(),
                    "Country": country_entry.get()
                }
                self.client_repo.update(updated_client)  # Save the updated client details
                confirmation_window.destroy()
                view_window.destroy()  # Close the window after updating
                self.load_client_data()  # Refresh the table to reflect changes

            update_button = ctk.CTkButton(button_frame, text="Update", fg_color="green", width=100, command=confirm)
            update_button.pack(side="left", padx=10)

            cancel_button = ctk.CTkButton(button_frame, text="Cancel", fg_color="gray", width=100, command=confirmation_window.destroy)
            cancel_button.pack(side="right", padx=10)

        def delete_client():
            """Delete the given client from the repository."""
            # Pop-up confirmation window for deletion
            confirmation_window = ctk.CTkToplevel(view_window)
            confirmation_window.title("Confirm Deletion")
            confirmation_window.geometry("400x200")

            ctk.CTkLabel(confirmation_window, text="Are you sure to delete?", font=("Arial", 18, "bold")).pack(pady=20)

            # Button Frame for delete and cancel options
            button_frame = ctk.CTkFrame(confirmation_window)
            button_frame.pack(pady=20)

            def confirm_delete():
                self.client_repo.delete(client)  # Delete the client from repository
                confirmation_window.destroy()  # Close the confirmation window
                view_window.destroy()  # Close the main client window after deletion
                self.load_client_data()  # Refresh the table to reflect changes

            delete_button = ctk.CTkButton(button_frame, text="Delete", fg_color="red", width=100, command=confirm_delete)
            delete_button.pack(side="left", padx=10)

            cancel_button = ctk.CTkButton(button_frame, text="Cancel", fg_color="gray", width=100, command=confirmation_window.destroy)
            cancel_button.pack(side="right", padx=10)

        # Client ID
        ctk.CTkLabel(view_window, text=f"Client ID #{client['ID']}", font=("Arial", 24, "bold")).pack(pady=10)

        # Contact Info
        contact_frame = ctk.CTkFrame(view_window)
        contact_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(contact_frame, text="Client Name: *").grid(row=0, column=0, padx=10, pady=5)
        client_name_entry = ctk.CTkEntry(contact_frame, width=300)
        client_name_entry.insert(0, client["Name"])
        client_name_entry.grid(row=0, column=1, padx=10)
        client_name_entry.configure(state="disabled")  # Initially in view-only mode

        ctk.CTkLabel(contact_frame, text="Phone No.: *").grid(row=0, column=2, padx=10)
        phone_entry = ctk.CTkEntry(contact_frame, width=300)
        phone_entry.insert(0, client["Phone_Number"])
        phone_entry.grid(row=0, column=3, padx=10)
        phone_entry.configure(state="disabled")

        # Address Info
        ctk.CTkLabel(view_window, text="Address", font=("Arial", 16, "bold")).pack(anchor="w", padx=20)

        address_frame = ctk.CTkFrame(view_window)
        address_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(address_frame, text="Line 1: *").grid(row=0, column=0, padx=10, pady=5)
        line1_entry = ctk.CTkEntry(address_frame, width=300)
        line1_entry.insert(0, client["Address_Line_1"])
        line1_entry.grid(row=0, column=1, padx=10)
        line1_entry.configure(state="disabled")

        ctk.CTkLabel(address_frame, text="Line 2:").grid(row=1, column=0, padx=10, pady=5)
        line2_entry = ctk.CTkEntry(address_frame, width=300)
        line2_entry.insert(0, client["Address_Line_2"])
        line2_entry.grid(row=1, column=1, padx=10)
        line2_entry.configure(state="disabled")

        ctk.CTkLabel(address_frame, text="Line 3:").grid(row=2, column=0, padx=10, pady=5)
        line3_entry = ctk.CTkEntry(address_frame, width=300)
        line3_entry.insert(0, client["Address_Line_3"])
        line3_entry.grid(row=2, column=1, padx=10)
        line3_entry.configure(state="disabled")

        ctk.CTkLabel(address_frame, text="City: *").grid(row=0, column=2, padx=10)
        city_entry = ctk.CTkEntry(address_frame, width=200)
        city_entry.insert(0, client["City"])
        city_entry.grid(row=0, column=3, padx=10)
        city_entry.configure(state="disabled")

        ctk.CTkLabel(address_frame, text="State: *").grid(row=1, column=2, padx=10)
        state_entry = ctk.CTkEntry(address_frame, width=200)
        state_entry.insert(0, client["State"])
        state_entry.grid(row=1, column=3, padx=10)
        state_entry.configure(state="disabled")

        ctk.CTkLabel(address_frame, text="Zip Code: *").grid(row=2, column=2, padx=10)
        zip_entry = ctk.CTkEntry(address_frame, width=200)
        zip_entry.insert(0, client["Zip_Code"])
        zip_entry.grid(row=2, column=3, padx=10)
        zip_entry.configure(state="disabled")

        ctk.CTkLabel(address_frame, text="Country: *").grid(row=3, column=0, padx=10, pady=5)
        country_entry = ctk.CTkEntry(address_frame, width=300)
        country_entry.insert(0, client["Country"])
        country_entry.grid(row=3, column=1, padx=10)
        country_entry.configure(state="disabled")

        # Buttons (View Mode)
        button_frame = ctk.CTkFrame(view_window)
        button_frame.pack(pady=20)

        # Removed "Close" button and added "Update" button in edit mode
        edit_button = ctk.CTkButton(button_frame, text="Edit", width=100, command=enable_edit)
        edit_button.pack(side="right", padx=10)

        # Buttons for Edit Mode
        back_button = ctk.CTkButton(button_frame, text="Back", fg_color="gray", width=100, command=disable_edit)
        update_button = ctk.CTkButton(button_frame, text="Update", fg_color="green", width=100, command=confirm_update)
        delete_button = ctk.CTkButton(button_frame, text="Delete", fg_color="red", width=100, command=delete_client)

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
