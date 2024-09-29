import customtkinter as ctk


class EditClientModal:
    def __init__(self, client, client_repo, callback):
        self.client_repo = client_repo
        self.callback = callback
        self.client = client
        """Open the client details in view mode."""
        self.view_window = ctk.CTkToplevel()
        self.view_window.title(f"Client ID #{client['ID']}")
        self.view_window.geometry("800x600")
        self.view_window.focus_force()

        # Client ID
        ctk.CTkLabel(
            self.view_window,
            text=f"Client ID #{client['ID']}",
            font=("Arial", 24, "bold"),
        ).pack(pady=10)

        # Contact Info
        self.contact_frame = ctk.CTkFrame(self.view_window)
        self.contact_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.contact_frame, text="Client Name: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.client_name_entry = ctk.CTkEntry(self.contact_frame, width=300)
        self.client_name_entry.insert(0, client["Name"])
        self.client_name_entry.grid(row=0, column=1, padx=10)
        self.client_name_entry.configure(
            state="disabled"
        )  # Initially in view-only mode

        ctk.CTkLabel(self.contact_frame, text="Phone No.: *").grid(
            row=0, column=2, padx=10
        )
        self.phone_entry = ctk.CTkEntry(self.contact_frame, width=300)
        self.phone_entry.insert(0, client["Phone_Number"])
        self.phone_entry.grid(row=0, column=3, padx=10)
        self.phone_entry.configure(state="disabled")

        # Address Info
        ctk.CTkLabel(self.view_window, text="Address", font=("Arial", 16, "bold")).pack(
            anchor="w", padx=20
        )

        self.address_frame = ctk.CTkFrame(self.view_window)
        self.address_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(self.address_frame, text="Line 1: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.line1_entry = ctk.CTkEntry(self.address_frame, width=300)
        self.line1_entry.insert(0, client["Address_Line_1"])
        self.line1_entry.grid(row=0, column=1, padx=10)
        self.line1_entry.configure(state="disabled")

        ctk.CTkLabel(self.address_frame, text="Line 2:").grid(
            row=1, column=0, padx=10, pady=5
        )
        self.line2_entry = ctk.CTkEntry(self.address_frame, width=300)
        self.line2_entry.insert(0, client["Address_Line_2"])
        self.line2_entry.grid(row=1, column=1, padx=10)
        self.line2_entry.configure(state="disabled")

        ctk.CTkLabel(self.address_frame, text="Line 3:").grid(
            row=2, column=0, padx=10, pady=5
        )
        self.line3_entry = ctk.CTkEntry(self.address_frame, width=300)
        self.line3_entry.insert(0, client["Address_Line_3"])
        self.line3_entry.grid(row=2, column=1, padx=10)
        self.line3_entry.configure(state="disabled")

        ctk.CTkLabel(self.address_frame, text="City: *").grid(row=0, column=2, padx=10)
        self.city_entry = ctk.CTkEntry(self.address_frame, width=200)
        self.city_entry.insert(0, client["City"])
        self.city_entry.grid(row=0, column=3, padx=10)
        self.city_entry.configure(state="disabled")

        ctk.CTkLabel(self.address_frame, text="State: *").grid(row=1, column=2, padx=10)
        self.state_entry = ctk.CTkEntry(self.address_frame, width=200)
        self.state_entry.insert(0, client["State"])
        self.state_entry.grid(row=1, column=3, padx=10)
        self.state_entry.configure(state="disabled")

        ctk.CTkLabel(self.address_frame, text="Zip Code: *").grid(
            row=2, column=2, padx=10
        )
        self.zip_entry = ctk.CTkEntry(self.address_frame, width=200)
        self.zip_entry.insert(0, client["Zip_Code"])
        self.zip_entry.grid(row=2, column=3, padx=10)
        self.zip_entry.configure(state="disabled")

        ctk.CTkLabel(self.address_frame, text="Country: *").grid(
            row=3, column=0, padx=10, pady=5
        )
        self.country_entry = ctk.CTkEntry(self.address_frame, width=300)
        self.country_entry.insert(0, client["Country"])
        self.country_entry.grid(row=3, column=1, padx=10)
        self.country_entry.configure(state="disabled")

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
            command=self.delete_client,
        )

    def enable_edit(self):
        """Enable editing mode for the client details."""
        self.client_name_entry.configure(state="normal")
        self.phone_entry.configure(state="normal")
        self.line1_entry.configure(state="normal")
        self.line2_entry.configure(state="normal")
        self.line3_entry.configure(state="normal")
        self.city_entry.configure(state="normal")
        self.state_entry.configure(state="normal")
        self.zip_entry.configure(state="normal")
        self.country_entry.configure(state="normal")
        self.edit_button.pack_forget()  # Hide Edit button in edit mode
        # Show Update and Delete buttons in edit mode
        self.update_button.pack(side="right", padx=10)
        self.delete_button.pack(side="right", padx=10)
        self.back_button.pack(side="left", padx=10)

    def disable_edit(self):
        """Disable editing mode (Back to view mode)."""
        self.client_name_entry.configure(state="disabled")
        self.phone_entry.configure(state="disabled")
        self.line1_entry.configure(state="disabled")
        self.line2_entry.configure(state="disabled")
        self.line3_entry.configure(state="disabled")
        self.city_entry.configure(state="disabled")
        self.state_entry.configure(state="disabled")
        self.zip_entry.configure(state="disabled")
        self.country_entry.configure(state="disabled")
        self.back_button.pack_forget()
        self.update_button.pack_forget()
        self.delete_button.pack_forget()
        self.edit_button.pack(side="right", padx=10)

    def confirm(self):
        # Once confirmed, update the client record
        updated_client = {
            "ID": self.client["ID"],
            "Type": "Client",
            "Name": self.client_name_entry.get(),
            "Phone_Number": self.phone_entry.get(),
            "Address_Line_1": self.line1_entry.get(),
            "Address_Line_2": self.line2_entry.get(),
            "Address_Line_3": self.line3_entry.get(),
            "City": self.city_entry.get(),
            "State": self.state_entry.get(),
            "Zip_Code": self.zip_entry.get(),
            "Country": self.country_entry.get(),
        }
        self.client_repo.update(updated_client)  # Save the updated client details
        self.confirmation_window.destroy()
        self.view_window.destroy()  # Close the window after updating
        if self.callback is not None:
            self.callback()  # Refresh the table to reflect changes

    def delete_client(self):
        """Delete the given client from the repository."""
        # Pop-up confirmation window for deletion
        self.confirmation_window = ctk.CTkToplevel(self.view_window)
        self.confirmation_window.title("Confirm Deletion")
        self.confirmation_window.geometry("400x200")
        self.confirmation_window.focus_force()

        ctk.CTkLabel(
            self.confirmation_window,
            text="Are you sure to delete?",
            font=("Arial", 18, "bold"),
        ).pack(pady=20)

        # Button Frame for delete and cancel options
        button_frame = ctk.CTkFrame(self.confirmation_window)
        button_frame.pack(pady=20)

        def confirm_delete():
            self.client_repo.delete(self.client)  # Delete the client from repository
            self.confirmation_window.destroy()  # Close the confirmation window
            self.view_window.destroy()  # Close the main client window after deletion
            if self.callback is not None:
                self.callback()  # Refresh the table to reflect changes

        delete_button = ctk.CTkButton(
            button_frame,
            text="Delete",
            fg_color="red",
            width=100,
            command=confirm_delete,
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

    def confirm_update(self):
        """Confirmation window for updating client details."""
        self.confirmation_window = ctk.CTkToplevel(self.view_window)
        self.confirmation_window.title("Confirm Update")
        self.confirmation_window.geometry("400x200")
        self.confirmation_window.focus_force()

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
