import customtkinter as ctk
from data.airline_repository import AirlineRepository  # Importing AirlineRepository

class App:
    def __init__(self, airline_repo: AirlineRepository):
        self.airline_repo = airline_repo
        # build UI
        self.build_app()

    def start(self):
        self.app.mainloop()

    def build_app(self):
        self.app = ctk.CTk()
        self.app.geometry("1000x500")
        self.app.title("Travel Wings - Airline Dashboard")

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

        #New record buttons at bottom of sidebar
        add_client_button = ctk.CTkButton(master=sidebar_frame, text="+ New Client", width=160, corner_radius=10) #, command=self.open_new_client_window)
        add_client_button.pack(pady=20, side="bottom")

        add_flight_button = ctk.CTkButton(master=sidebar_frame, text="+ New Flight", width=160, corner_radius=10)
        add_flight_button.pack(pady=10, side="bottom")

        add_airline_button = ctk.CTkButton(master=sidebar_frame, text="+ New Airline", width=160, corner_radius=10, command=self.open_new_airline_window)
        add_airline_button.pack(pady=10, side="bottom")

        # Main Content Frame (Right side)
        content_frame = ctk.CTkFrame(master=self.app)
        content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Search bar
        search_frame = ctk.CTkFrame(master=content_frame, width=600, height=50)
        search_frame.pack(fill="x", pady=20)

        search_label = ctk.CTkLabel(master=search_frame, text="Airline Dashboard", font=("Arial", 24, "bold"))
        search_label.pack(anchor="w")

        search_entry = ctk.CTkEntry(master=search_frame, width=400, placeholder_text="Search name or ID...")
        search_entry.pack(side="left", padx=10, pady=10)

        # Airline Table Header
        self.table_frame = ctk.CTkFrame(master=content_frame)
        self.table_frame.pack(fill="both", expand=True)

        header_frame = ctk.CTkFrame(master=self.table_frame)
        header_frame.pack(fill="x", pady=10)

        headers = ["Airline ID", "Type", "Company Name"]
        for header in headers:
            label = ctk.CTkLabel(master=header_frame, text=header, width=10, font=("Arial", 10, "bold"))
            label.pack(side="left", padx=10)

        # Add "View" button header
        label = ctk.CTkLabel(master=header_frame, text="View", width=10, font=("Arial", 10, "bold"))
        label.pack(side="left", padx=10)

        # Load and display initial airline data
        self.load_airline_data()

    def load_airline_data(self):
        """Load and display airlinr data from the repository."""
        # Clear old data
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Display the headers again
        header_frame = ctk.CTkFrame(master=self.table_frame)
        header_frame.pack(fill="x", pady=10)
        headers = ["Airline ID", "Type", "Company Name"]
        for header in headers:
            label = ctk.CTkLabel(master=header_frame, text=header, width=10, font=("Arial", 10, "bold"))
            label.pack(side="left", padx=10)

        # Add "View" button header
        label = ctk.CTkLabel(master=header_frame, text="View", width=10, font=("Arial", 10, "bold"))
        label.pack(side="left", padx=10)

        # Fetching airline data from the repository
        airline_data = self.airline_repo.list()

        # Display airline data in the UI
        for airline in airline_data:
            row_frame = ctk.CTkFrame(master=self.table_frame)
            row_frame.pack(fill="x", pady=5)

            for key in ["ID", "Type", "Company_Name"]:
                value = airline.get(key, "")
                data_label = ctk.CTkLabel(master=row_frame, text=value, width=10)
                data_label.pack(side="left", padx=10)

            # View button for each airline
            view_button = ctk.CTkButton(master=row_frame, text="View", width=10, command=lambda c=airline: self.view_airline(c))
            view_button.pack(side="left", padx=10)

    def open_new_airline_window(self):
        """Method to open a new window for adding a new airline."""
        new_window = ctk.CTkToplevel()
        new_window.title("New Airline")
        new_window.geometry("800x600")

        # Input fields for airline information
        def save_airline():
            new_airline = {
                "ID": len(self.airline_repo.list()) + 1,  # Auto-incrementing ID
                "Type": "Airline",  # Type is set to "Airline"
                "Company_Name": name_entry.get(),
            }
            self.airline_repo.create(new_airline)  # Save to airlines.jsonl
            self.load_airline_data()  # Reload the airline table to show the new record
            new_window.destroy()  # Close the window after saving

        # Airline Info (Contact)
        ctk.CTkLabel(new_window, text="New Airline", font=("Arial", 20, "bold")).pack(pady=10)
        

        company_frame = ctk.CTkFrame(new_window)
        company_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(company_frame, text="Company Name: *").grid(row=0, column=0, padx=10, pady=5)
        name_entry = ctk.CTkEntry(company_frame, width=300)
        name_entry.grid(row=0, column=1, padx=10)

        
        # Save and Close buttons
        button_frame = ctk.CTkFrame(new_window)
        button_frame.pack(pady=20)

        close_button = ctk.CTkButton(button_frame, text="Close", fg_color="red", width=100, command=new_window.destroy)
        close_button.pack(side="left", padx=20)

        save_button = ctk.CTkButton(button_frame, text="Save", fg_color="green", width=100, command=save_airline)
        save_button.pack(side="right", padx=20)

    def view_airline(self, airline):
        """Open the airline details in view mode."""
        view_window = ctk.CTkToplevel()
        view_window.title(f"Airline ID #{airline['ID']}")
        view_window.geometry("800x600")

        # Display airline details (View mode)
        def enable_edit():
            """Enable editing mode for the airline details."""
            airline_name_entry.configure(state="normal")
            edit_button.pack_forget()  # Hide Edit button in edit mode
            # Show Update and Delete buttons in edit mode
            update_button.pack(side="right", padx=10)
            delete_button.pack(side="right", padx=10)
            back_button.pack(side="left", padx=10)

        def disable_edit():
            """Disable editing mode (Back to view mode)."""
            airline_name_entry.configure(state="disabled")
            back_button.pack_forget()
            update_button.pack_forget()
            delete_button.pack_forget()
            edit_button.pack(side="right", padx=10)

        def confirm_update():
            """Confirmation window for updating airline details."""
            confirmation_window = ctk.CTkToplevel(view_window)
            confirmation_window.title("Confirm Update")
            confirmation_window.geometry("400x200")

            # Warning Label
            ctk.CTkLabel(confirmation_window, text="Once you update the record, it cannot be recovered.\nAre you sure you want to update?", font=("Arial", 14, "bold")).pack(pady=20)

            # Button Frame for update and cancel options
            button_frame = ctk.CTkFrame(confirmation_window)
            button_frame.pack(pady=20)

            def confirm():
                # Once confirmed, update the airline record
                updated_airline = {
                    "ID": airline['ID'],
                    "Type": "Airline",
                    "Company_Name": airline_name_entry.get()
                }
                self.airline_repo.update(updated_airline)  # Save the updated airline details
                confirmation_window.destroy()
                view_window.destroy()  # Close the window after updating
                self.load_airline_data()  # Refresh the table to reflect changes

            update_button = ctk.CTkButton(button_frame, text="Update", fg_color="green", width=100, command=confirm)
            update_button.pack(side="left", padx=10)

            cancel_button = ctk.CTkButton(button_frame, text="Cancel", fg_color="gray", width=100, command=confirmation_window.destroy)
            cancel_button.pack(side="right", padx=10)

        def delete_airline():
            """Delete the given airline from the repository."""
            # Pop-up confirmation window for deletion
            confirmation_window = ctk.CTkToplevel(view_window)
            confirmation_window.title("Confirm Deletion")
            confirmation_window.geometry("400x200")

            ctk.CTkLabel(confirmation_window, text="Are you sure to delete?", font=("Arial", 18, "bold")).pack(pady=20)

            # Button Frame for delete and cancel options
            button_frame = ctk.CTkFrame(confirmation_window)
            button_frame.pack(pady=20)

            def confirm_delete():
                self.airline_repo.delete(airline)  # Delete the airline from repository
                confirmation_window.destroy()  # Close the confirmation window
                view_window.destroy()  # Close the main airline window after deletion
                self.load_airline_data()  # Refresh the table to reflect changes

            delete_button = ctk.CTkButton(button_frame, text="Delete", fg_color="red", width=100, command=confirm_delete)
            delete_button.pack(side="left", padx=10)

            cancel_button = ctk.CTkButton(button_frame, text="Cancel", fg_color="gray", width=100, command=confirmation_window.destroy)
            cancel_button.pack(side="right", padx=10)

        # Airline ID
        ctk.CTkLabel(view_window, text=f"Airline ID #{airline['ID']}", font=("Arial", 24, "bold")).pack(pady=10)

        # Contact Info
        contact_frame = ctk.CTkFrame(view_window)
        contact_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(contact_frame, text="Airline Name: *").grid(row=0, column=0, padx=10, pady=5)
        airline_name_entry = ctk.CTkEntry(contact_frame, width=300)
        airline_name_entry.insert(0, airline["Company_Name"])
        airline_name_entry.grid(row=0, column=1, padx=10)
        airline_name_entry.configure(state="disabled")  # Initially in view-only mode

        
        # Buttons (View Mode)
        button_frame = ctk.CTkFrame(view_window)
        button_frame.pack(pady=20)

        # Removed "Close" button and added "Update" button in edit mode
        edit_button = ctk.CTkButton(button_frame, text="Edit", width=100, command=enable_edit)
        edit_button.pack(side="right", padx=10)

        # Buttons for Edit Mode
        back_button = ctk.CTkButton(button_frame, text="Back", fg_color="gray", width=100, command=disable_edit)
        update_button = ctk.CTkButton(button_frame, text="Update", fg_color="green", width=100, command=confirm_update)
        delete_button = ctk.CTkButton(button_frame, text="Delete", fg_color="red", width=100, command=delete_airline)

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
