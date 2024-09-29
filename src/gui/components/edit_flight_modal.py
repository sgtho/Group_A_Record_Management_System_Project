import customtkinter as ctk
from data import FlightRepository


class EditFlightModal:
    def __init__(self, flight, flight_repo: FlightRepository, callback):
        self.flight_repo = flight_repo
        self.callback = callback
        self.flight = flight
        """Open the flight details in view mode."""
        self.view_window = ctk.CTkToplevel()
        self.view_window.title(f"Flight ID #{flight['ID']}")
        self.view_window.geometry("800x600")

        # Flight ID
        ctk.CTkLabel(
            self.view_window,
            text=f"Flight ID #{flight['ID']}",
            font=("Arial", 24, "bold"),
        ).pack(pady=10)

        # Indentification
        self.id_frame = ctk.CTkFrame(self.view_window)
        self.id_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.id_frame, text="Client ID: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.client_id_entry = ctk.CTkEntry(self.id_frame, width=300)
        self.client_id_entry.insert(0, flight["Client_ID"])
        self.client_id_entry.grid(row=0, column=1, padx=10)
        self.client_id_entry.configure(state="disabled")  # Initially in view-only mode

        ctk.CTkLabel(self.id_frame, text="Airline ID.: *").grid(
            row=0, column=2, padx=10
        )
        self.airline_id_entry = ctk.CTkEntry(self.id_frame, width=300)
        self.airline_id_entry.insert(0, flight["Airline_ID"])
        self.airline_id_entry.grid(row=0, column=3, padx=10)
        self.airline_id_entry.configure(state="disabled")

        # Journet Info
        ctk.CTkLabel(self.view_window, text="Journey", font=("Arial", 16, "bold")).pack(
            anchor="w", padx=20
        )

        self.journey_frame = ctk.CTkFrame(self.view_window)
        self.journey_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.journey_frame, text="Date/Time: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.date_time_entry = ctk.CTkEntry(self.journey_frame, width=300)
        self.date_time_entry.insert(0, flight["Date_Time"])
        self.date_time_entry.grid(row=0, column=1, padx=10)
        self.date_time_entry.configure(state="disabled")

        ctk.CTkLabel(self.journey_frame, text="Start City:").grid(
            row=1, column=0, padx=10, pady=5
        )
        self.start_city_entry = ctk.CTkEntry(self.journey_frame, width=300)
        self.start_city_entry.insert(0, flight["Start_City"])
        self.start_city_entry.grid(row=1, column=1, padx=10)
        self.start_city_entry.configure(state="disabled")

        ctk.CTkLabel(self.journey_frame, text="End City:").grid(
            row=2, column=0, padx=10, pady=5
        )
        self.end_city_entry = ctk.CTkEntry(self.journey_frame, width=300)
        self.end_city_entry.insert(0, flight["End_City"])
        self.end_city_entry.grid(row=2, column=1, padx=10)
        self.end_city_entry.configure(state="disabled")

        # Buttons (View Mode)
        self.button_frame = ctk.CTkFrame(self.view_window)
        self.button_frame.pack(pady=20)

        # Removed "Close" button and added "Update" button in edit mode
        self.edit_button = ctk.CTkButton(
            self.button_frame, text="Edit", width=100, command=self.enable_edit
        )
        self.edit_button.pack(side="right", padx=10)

        # Buttons for Edit Mode
        self.back_button = ctk.CTkButton(
            self.button_frame,
            text="Back",
            fg_color="gray",
            width=100,
            command=self.disable_edit,
        )
        self.update_button = ctk.CTkButton(
            self.button_frame,
            text="Update",
            fg_color="green",
            width=100,
            command=self.confirm_update,
        )
        self.delete_button = ctk.CTkButton(
            self.button_frame,
            text="Delete",
            fg_color="red",
            width=100,
            command=self.delete_flight,
        )

    def enable_edit(self):
        """Enable editing mode for the flight details."""
        self.client_id_entry.configure(state="normal")
        self.airline_id_entry.configure(state="normal")
        self.date_time_entry.configure(state="normal")
        self.start_city_entry.configure(state="normal")
        self.end_city_entry.configure(state="normal")

        self.edit_button.pack_forget()  # Hide Edit button in edit mode
        # Show Update and Delete buttons in edit mode
        self.update_button.pack(side="right", padx=10)
        self.delete_button.pack(side="right", padx=10)
        self.back_button.pack(side="left", padx=10)

    def disable_edit(self):
        """Disable editing mode (Back to view mode)."""
        self.client_id_entry.configure(state="disabled")
        self.airline_id_entry.configure(state="disabled")
        self.date_time_entry.configure(state="disabled")
        self.start_city_entry.configure(state="disabled")
        self.end_city_entry.configure(state="disabled")
        self.back_button.pack_forget()
        self.update_button.pack_forget()
        self.delete_button.pack_forget()
        self.edit_button.pack(side="right", padx=10)

    def confirm_update(self):
        """Confirmation window for updating flight details."""
        self.confirmation_window = ctk.CTkToplevel(self.view_window)
        self.confirmation_window.title("Confirm Update")
        self.confirmation_window.geometry("400x200")

        # Warning Label
        ctk.CTkLabel(
            self.confirmation_window,
            text="Once you update the record, it cannot be recovered.\nAre you sure you want to update?",
            font=("Arial", 14, "bold"),
        ).pack(pady=20)

        # Button Frame for update and cancel options
        button_frame = ctk.CTkFrame(self.confirmation_window)
        button_frame.pack(pady=20)

        update_button = ctk.CTkButton(
            button_frame,
            text="Update",
            fg_color="green",
            width=100,
            command=self.confirm,
        )
        update_button.pack(side="left", padx=10)

        cancel_button = ctk.CTkButton(
            button_frame,
            text="Cancel",
            fg_color="gray",
            width=100,
            command=self.confirmation_window.destroy,
        )
        cancel_button.pack(side="right", padx=10)

    def delete_flight(self):
        """Delete the given flight from the repository."""
        # Pop-up confirmation window for deletion
        self.confirmation_window = ctk.CTkToplevel(self.view_window)
        self.confirmation_window.title("Confirm Deletion")
        self.confirmation_window.geometry("400x200")

        ctk.CTkLabel(
            self.confirmation_window,
            text="Are you sure to delete?",
            font=("Arial", 18, "bold"),
        ).pack(pady=20)

        # Button Frame for delete and cancel options
        button_frame = ctk.CTkFrame(self.confirmation_window)
        button_frame.pack(pady=20)

        delete_button = ctk.CTkButton(
            button_frame,
            text="Delete",
            fg_color="red",
            width=100,
            command=self.confirm_delete,
        )
        delete_button.pack(side="left", padx=10)

        cancel_button = ctk.CTkButton(
            button_frame,
            text="Cancel",
            fg_color="gray",
            width=100,
            command=self.confirmation_window.destroy,
        )
        cancel_button.pack(side="right", padx=10)

    def confirm_delete(self):
        self.flight_repo.delete(self.flight)  # Delete the flight from repository
        self.confirmation_window.destroy()  # Close the confirmation window
        self.view_window.destroy()  # Close the main flight window after deletion
        self.callback()  # Refresh the table to reflect changes

    def confirm(self):
        # Once confirmed, update the flight record
        updated_flight = {
            "ID": self.flight["ID"],
            "Type": "Flight",
            "Client_ID": self.client_id_entry.get(),
            "Airline_ID": self.airline_id_entry.get(),
            "Date_Time": self.date_time_entry.get(),
            "Start_City": self.start_city_entry.get(),
            "End_City": self.end_city_entry.get(),
        }
        self.flight_repo.update(updated_flight)  # Save the updated flight details
        self.confirmation_window.destroy()
        self.view_window.destroy()  # Close the window after updating
        self.callback()  # Refresh the table to reflect changes
