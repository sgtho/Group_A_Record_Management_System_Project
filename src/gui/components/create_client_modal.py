import customtkinter as ctk
from data.client_repository import ClientRepository


class CreateClientModal:
    def __init__(self, client_repo: ClientRepository, callback):
        self.client_repo = client_repo
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
            self.client_repo.create(new_client)
            if callback is not None:
                callback()
            new_window.destroy()

        # Client Info (Contact)
        ctk.CTkLabel(new_window, text="New Client", font=("Arial", 20, "bold")).pack(
            pady=10
        )
        ctk.CTkLabel(new_window, text="Contact", font=("Arial", 16, "bold")).pack(
            anchor="w", padx=20
        )

        contact_frame = ctk.CTkFrame(new_window)
        contact_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(contact_frame, text="Client Name: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        name_entry = ctk.CTkEntry(contact_frame, width=300)
        name_entry.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(contact_frame, text="Phone No.: *").grid(row=0, column=2, padx=10)
        phone_entry = ctk.CTkEntry(contact_frame, width=300)
        phone_entry.grid(row=0, column=3, padx=10)

        # Client Info (Address)
        ctk.CTkLabel(new_window, text="Address", font=("Arial", 16, "bold")).pack(
            anchor="w", padx=20
        )

        address_frame = ctk.CTkFrame(new_window)
        address_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(address_frame, text="Line 1: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        line1_entry = ctk.CTkEntry(address_frame, width=300)
        line1_entry.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(address_frame, text="Line 2:").grid(
            row=1, column=0, padx=10, pady=5
        )
        line2_entry = ctk.CTkEntry(address_frame, width=300)
        line2_entry.grid(row=1, column=1, padx=10)

        ctk.CTkLabel(address_frame, text="Line 3:").grid(
            row=2, column=0, padx=10, pady=5
        )
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

        ctk.CTkLabel(address_frame, text="Country: *").grid(
            row=3, column=0, padx=10, pady=5
        )
        country_entry = ctk.CTkEntry(address_frame, width=300)
        country_entry.grid(row=3, column=1, padx=10)

        # Save and Close buttons
        button_frame = ctk.CTkFrame(new_window)
        button_frame.pack(pady=20)

        close_button = ctk.CTkButton(
            button_frame,
            text="Close",
            fg_color="red",
            width=100,
            command=new_window.destroy,
        )
        close_button.pack(side="left", padx=20)

        save_button = ctk.CTkButton(
            button_frame, text="Save", fg_color="green", width=100, command=save_client
        )
        save_button.pack(side="right", padx=20)
