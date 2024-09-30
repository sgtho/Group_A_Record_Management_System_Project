import customtkinter as ctk
from data.client_repository import ClientRepository


class CreateClientModal:
    def __init__(self, client_repo: ClientRepository, callback):
        self.callback = callback
        self.client_repo = client_repo
        """Method to open a new window for adding a new client."""
        self.new_window = ctk.CTkToplevel()
        self.new_window.title("New Client")
        self.new_window.geometry("800x600")
        self.new_window.focus_force()

        # Client Info (Contact)
        ctk.CTkLabel(
            self.new_window, text="New Client", font=("Arial", 20, "bold")
        ).pack(pady=10)
        ctk.CTkLabel(self.new_window, text="Contact", font=("Arial", 16, "bold")).pack(
            anchor="w", padx=20
        )

        self.contact_frame = ctk.CTkFrame(self.new_window)
        self.contact_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.contact_frame, text="Client Name: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.name_entry = ctk.CTkEntry(self.contact_frame, width=300)
        self.name_entry.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(self.contact_frame, text="Phone No.: *").grid(
            row=0, column=2, padx=10
        )
        self.phone_entry = ctk.CTkEntry(self.contact_frame, width=300)
        self.phone_entry.grid(row=0, column=3, padx=10)

        # Client Info (Address)
        ctk.CTkLabel(self.new_window, text="Address", font=("Arial", 16, "bold")).pack(
            anchor="w", padx=20
        )

        self.address_frame = ctk.CTkFrame(self.new_window)
        self.address_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.address_frame, text="Line 1: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.line1_entry = ctk.CTkEntry(self.address_frame, width=300)
        self.line1_entry.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(self.address_frame, text="Line 2:").grid(
            row=1, column=0, padx=10, pady=5
        )
        self.line2_entry = ctk.CTkEntry(self.address_frame, width=300)
        self.line2_entry.grid(row=1, column=1, padx=10)

        ctk.CTkLabel(self.address_frame, text="Line 3:").grid(
            row=2, column=0, padx=10, pady=5
        )
        self.line3_entry = ctk.CTkEntry(self.address_frame, width=300)
        self.line3_entry.grid(row=2, column=1, padx=10)

        ctk.CTkLabel(self.address_frame, text="City: *").grid(row=0, column=2, padx=10)
        self.city_entry = ctk.CTkEntry(self.address_frame, width=200)
        self.city_entry.grid(row=0, column=3, padx=10)

        ctk.CTkLabel(self.address_frame, text="State: *").grid(row=1, column=2, padx=10)
        self.state_entry = ctk.CTkEntry(self.address_frame, width=200)
        self.state_entry.grid(row=1, column=3, padx=10)

        ctk.CTkLabel(self.address_frame, text="Zip Code: *").grid(
            row=2, column=2, padx=10
        )
        self.zip_entry = ctk.CTkEntry(self.address_frame, width=200)
        self.zip_entry.grid(row=2, column=3, padx=10)

        ctk.CTkLabel(self.address_frame, text="Country: *").grid(
            row=3, column=0, padx=10, pady=5
        )
        self.country_entry = ctk.CTkEntry(self.address_frame, width=300)
        self.country_entry.grid(row=3, column=1, padx=10)

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
            command=self.save_client,
        )
        self.save_button.pack(side="right", padx=20)

    def save_client(self):
        new_client = {
            "Name": self.name_entry.get(),
            "Address_Line_1": self.line1_entry.get(),
            "Address_Line_2": self.line2_entry.get(),
            "Address_Line_3": self.line3_entry.get(),
            "City": self.city_entry.get(),
            "State": self.state_entry.get(),
            "Zip_Code": self.zip_entry.get(),
            "Country": self.country_entry.get(),
            "Phone_Number": self.phone_entry.get(),
        }
        self.client_repo.create(new_client)
        if self.callback is not None:
            self.callback()
        self.new_window.destroy()
