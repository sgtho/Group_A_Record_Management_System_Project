import customtkinter as ctk
from data.airline_repository import AirlineRepository


class CreateAirlineModal:
    def __init__(self, airline_repo: AirlineRepository, callback):
        self.airline_repo = airline_repo
        self.callback = callback
        """Method to open a new window for adding a new airline."""
        self.new_window = ctk.CTkToplevel()
        self.new_window.title("New Airline")
        self.new_window.geometry("800x600")
        self.new_window.focus_force()

        # Airline Info (Contact)
        ctk.CTkLabel(
            self.new_window, text="New Airline", font=("Arial", 20, "bold")
        ).pack(pady=10)

        self.error_label = ctk.CTkLabel(
            self.new_window,
            text="",
            text_color="#e67a67",
            font=("Arial", 16, "bold"),
        )

        company_frame = ctk.CTkFrame(self.new_window)
        company_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(company_frame, text="Company Name: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.name_entry = ctk.CTkEntry(company_frame, width=300)
        self.name_entry.grid(row=0, column=1, padx=10)

        # Save and Close buttons
        button_frame = ctk.CTkFrame(self.new_window)
        button_frame.pack(pady=20)

        close_button = ctk.CTkButton(
            button_frame,
            text="Close",
            fg_color="red",
            width=100,
            command=self.new_window.destroy,
        )
        close_button.pack(side="left", padx=20)

        save_button = ctk.CTkButton(
            button_frame,
            text="Save",
            fg_color="green",
            width=100,
            command=self.save_airline,
        )
        save_button.pack(side="right", padx=20)

    # Input fields for airline information
    def save_airline(self):
        self.new_airline = {
            "ID": len(self.airline_repo.list()) + 1,  # Auto-incrementing ID
            "Type": "Airline",  # Type is set to "Airline"
            "Company_Name": self.name_entry.get(),
        }

        try:
            self.airline_repo.create(self.new_airline) # Save to airlines.jsonl
        except Exception as e:
            self.error_label.pack()
            self.error_label.configure(text=f"Error creating airline: {e}")
            return

        self.callback()  # Reload the airline table to show the new record
        self.new_window.destroy()  # Close the window after saving
