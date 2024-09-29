import customtkinter as ctk


class AirlinesView:
    def __init__(self, root, client_repo):
        self.client_repo = client_repo
        # Main Content Frame (Right side)
        content_frame = ctk.CTkFrame(master=root, fg_color="transparent")
        content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.root = content_frame

        # Search bar
        search_frame = ctk.CTkFrame(
            master=content_frame, width=600, height=50, fg_color="transparent"
        )
        search_frame.pack(fill="x", pady=0)

        search_label = ctk.CTkLabel(
            master=search_frame,
            text="Airlines Dashboard",
            font=("Arial", 32, "bold"),
            bg_color="transparent",
        )
        search_label.pack(anchor="w")

        search_entry = ctk.CTkEntry(
            master=search_frame,
            width=200,
            height=30,
            placeholder_text="Search name or ID...",
        )
        search_entry.pack(anchor="w", pady=30)

    def destroy(self):
        self.root.destroy()
