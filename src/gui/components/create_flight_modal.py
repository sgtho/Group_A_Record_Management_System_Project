import customtkinter as ctk
from data import FlightRepository


class CreateFlightModal:
    def __init__(self, flight_repo: FlightRepository, callback):
        self.callback = callback
        self.flight_repo = flight_repo
        """Method to open a new window for adding a new flight."""
        self.new_window = ctk.CTkToplevel()
        self.new_window.title("New flight")
        self.new_window.geometry("800x600")
        self.new_window.focus_force()

        # Flight Info (Identification)
        ctk.CTkLabel(
            self.new_window, text="New Flight", font=("Arial", 20, "bold")
        ).pack(pady=10)
        ctk.CTkLabel(self.new_window, text="Flight", font=("Arial", 16, "bold")).pack(
            anchor="w", padx=20
        )

        self.error_label = ctk.CTkLabel(
            self.new_window,
            text="",
            text_color="#e67a67",
            font=("Arial", 16, "bold"),
        )

        self.id_frame = ctk.CTkFrame(self.new_window)
        self.id_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.id_frame, text="Client ID: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.client_id_entry = ctk.CTkEntry(self.id_frame, width=300)
        self.client_id_entry.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(self.id_frame, text="Airline ID: *").grid(row=0, column=2, padx=10)
        self.airline_id_entry = ctk.CTkEntry(self.id_frame, width=300)
        self.airline_id_entry.grid(row=0, column=3, padx=10)

        # Flight Info (Journey)
        ctk.CTkLabel(self.new_window, text="Journey", font=("Arial", 16, "bold")).pack(
            anchor="w", padx=20
        )

        self.journey_frame = ctk.CTkFrame(self.new_window)
        self.journey_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.journey_frame, text="Date/Time: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.date_time_entry = ctk.CTkEntry(self.journey_frame, width=300)
        self.date_time_entry.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(self.journey_frame, text="Start City:").grid(
            row=1, column=0, padx=10, pady=5
        )
        self.start_city_entry = ctk.CTkEntry(self.journey_frame, width=300)
        self.start_city_entry.grid(row=1, column=1, padx=10)

        ctk.CTkLabel(self.journey_frame, text="End City:").grid(
            row=2, column=0, padx=10, pady=5
        )
        self.end_city_entry = ctk.CTkEntry(self.journey_frame, width=300)
        self.end_city_entry.grid(row=2, column=1, padx=10)

        # Save and Close buttons
        self.button_frame = ctk.CTkFrame(self.new_window)
        self.button_frame.pack(pady=20)

        self.close_button = ctk.CTkButton(
            self.button_frame,
            text="Close",
            fg_color="red",
            width=100,
            command=self.new_window.destroy,
        )
        self.close_button.pack(side="left", padx=20)

        self.save_button = ctk.CTkButton(
            self.button_frame,
            text="Save",
            fg_color="green",
            width=100,
            command=self.save_flight,
        )
        self.save_button.pack(side="right", padx=20)

    def save_flight(self):
        new_flight = {
            "Client_ID": self.client_id_entry.get(),
            "Airline_ID": self.airline_id_entry.get(),
            "Type": "Flight",  # Type is set to "flight"
            "Date_Time": self.date_time_entry.get(),
            "Start_City": self.start_city_entry.get(),
            "End_City": self.end_city_entry.get(),
        }

        try:
            self.flight_repo.create(new_flight) # Save to flights.jsonl
        except Exception as e:
            self.error_label.pack()
            self.error_label.configure(text=f"Error creating flight: {e}")
            return
        
        self.callback()  # Reload the flight table to show the new record
        self.new_window.destroy()  # Close the window after saving
