import customtkinter as ctk
from data import AirlineRepository


class EditAirlineModal:
    def __init__(self, airline, airline_repo: AirlineRepository, callback):
        self.airline_repo = airline_repo
        self.callback = callback
        self.airline = airline
        """Open the airline details in view mode."""
        self.view_window = ctk.CTkToplevel()
        self.view_window.title(f"Airline ID #{airline['ID']}")
        self.view_window.geometry("800x600")
        self.view_window.focus_force()

        self.error_label = ctk.CTkLabel(
            self.view_window,
            text="",
            text_color="#e67a67",
            font=("Arial", 16, "bold"),
        )

        # Airline ID
        ctk.CTkLabel(
            self.view_window,
            text=f"Airline ID #{airline['ID']}",
            font=("Arial", 24, "bold"),
        ).pack(pady=10)

        # Contact Info
        contact_frame = ctk.CTkFrame(self.view_window)
        contact_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(contact_frame, text="Airline Name: *").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.airline_name_entry = ctk.CTkEntry(contact_frame, width=300)
        self.airline_name_entry.insert(0, airline["Company_Name"])
        self.airline_name_entry.grid(row=0, column=1, padx=10)
        self.airline_name_entry.configure(
            state="disabled"
        )  # Initially in view-only mode

        # Buttons (View Mode)
        button_frame = ctk.CTkFrame(self.view_window)
        button_frame.pack(pady=20)

        # Removed "Close" button and added "Update" button in edit mode
        self.edit_button = ctk.CTkButton(
            button_frame, text="Edit", width=100, command=self.enable_edit
        )
        self.edit_button.pack(side="right", padx=10)

        # Buttons for Edit Mode
        self.back_button = ctk.CTkButton(
            button_frame,
            text="Back",
            fg_color="gray",
            width=100,
            command=self.disable_edit,
        )
        self.update_button = ctk.CTkButton(
            button_frame,
            text="Update",
            fg_color="green",
            width=100,
            command=self.confirm_update,
        )
        self.delete_button = ctk.CTkButton(
            button_frame,
            text="Delete",
            fg_color="red",
            width=100,
            command=self.delete_airline,
        )

    # Display airline details (View mode)
    def enable_edit(self):
        """Enable editing mode for the airline details."""
        self.airline_name_entry.configure(state="normal")
        self.edit_button.pack_forget()  # Hide Edit button in edit mode
        # Show Update and Delete buttons in edit mode
        self.update_button.pack(side="right", padx=10)
        self.delete_button.pack(side="right", padx=10)
        self.back_button.pack(side="left", padx=10)

    def disable_edit(self):
        """Disable editing mode (Back to view mode)."""
        self.airline_name_entry.configure(state="disabled")
        self.back_button.pack_forget()
        self.update_button.pack_forget()
        self.delete_button.pack_forget()
        self.edit_button.pack(side="right", padx=10)

    def confirm(self):
        # Once confirmed, update the airline record
        updated_airline = {
            "ID": self.airline["ID"],
            "Type": "Airline",
            "Company_Name": self.airline_name_entry.get(),
        }

        try:
            self.airline_repo.update(updated_airline)  # Save the updated airline details
        except Exception as e:
            self.error_label.pack()
            self.error_label.configure(text=f"Error creating airline: {e}")
            self.confirmation_window.destroy()
            return

        self.confirmation_window.destroy()
        self.view_window.destroy()  # Close the window after updating
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

        self.delete_button = ctk.CTkButton(
            button_frame,
            text="Delete",
            fg_color="red",
            width=100,
            command=self.confirm_delete,
        )
        self.delete_button.pack(side="left", padx=10)

        cancel_button = ctk.CTkButton(
            button_frame,
            text="Cancel",
            fg_color="gray",
            width=100,
            command=self.confirmation_window.destroy,
        )
        cancel_button.pack(side="right", padx=10)

    def confirm_delete(self):
        self.airline_repo.delete(self.airline)  # Delete the airline from repository
        self.confirmation_window.destroy()  # Close the confirmation window
        self.view_window.destroy()  # Close the main airline window after deletion
        self.callback()  # Refresh the table to reflect changes

    def confirm_update(self):
        """Confirmation window for updating client details."""
        self.confirmation_window = ctk.CTkToplevel(self.view_window)
        self.view_clientconfirmation_window.title("Confirm Update")
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

    # Display airline details (View mode)
    def enable_edit(self):
        """Enable editing mode for the airline details."""
        self.airline_name_entry.configure(state="normal")
        self.edit_button.pack_forget()  # Hide Edit button in edit mode
        # Show Update and Delete buttons in edit mode
        self.update_button.pack(side="right", padx=10)
        self.delete_button.pack(side="right", padx=10)
        self.back_button.pack(side="left", padx=10)

    def disable_edit(self):
        """Disable editing mode (Back to view mode)."""
        self.airline_name_entry.configure(state="disabled")
        self.back_button.pack_forget()
        self.update_button.pack_forget()
        self.delete_button.pack_forget()
        self.edit_button.pack(side="right", padx=10)

    def confirm(self):
        # Once confirmed, update the airline record
        self.updated_airline = {
            "ID": self.airline["ID"],
            "Type": "Airline",
            "Company_Name": self.airline_name_entry.get(),
        }

        try:
            self.airline_repo.update(
                self.updated_airline
        )   # Save the updated airline details
        except Exception as e:
            self.error_label.pack()
            self.error_label.configure(text=f"Error creating airline: {e}")
            self.confirmation_window.destroy()
            return

        self.confirmation_window.destroy()
        self.view_window.destroy()  # Close the window after updating
        self.callback()  # Refresh the table to reflect changes

    def confirm_update(self):
        """Confirmation window for updating airline details."""
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

    def delete_airline(self):
        """Delete the given airline from the repository."""
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
        self.airline_repo.delete(self.airline)  # Delete the airline from repository
        self.confirmation_window.destroy()  # Close the confirmation window
        self.view_window.destroy()  # Close the main airline window after deletion
        self.callback()  # Refresh the table to reflect changes
