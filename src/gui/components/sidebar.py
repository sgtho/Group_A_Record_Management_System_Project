import customtkinter as ctk


class Sidebar:
    def __init__(
        self,
        root,
        view_change_handler,
        create_handler,
        active_tab,
    ):
        self.view_change_handler = view_change_handler
        self.create_handler = create_handler
        self.active_tab = active_tab
        self.bg_color = "#8e8e8e"
        # Sidebar Frame (Left side)
        sidebar_frame = ctk.CTkFrame(
            master=root, width=400, fg_color="transparent", bg_color=self.bg_color
        )
        sidebar_frame.grid(row=0, column=0, sticky="nsew")

        # Sidebar Content
        sidebar_logo = ctk.CTkLabel(
            master=sidebar_frame,
            text="TRAVEL\nWINGS",
            font=("Arial", 24, "bold"),
            justify="center",
            fg_color="transparent",
            bg_color=self.bg_color,
        )
        sidebar_logo.pack(pady=20)

        # Buttons in sidebar
        self.client_button = ctk.CTkButton(
            master=sidebar_frame,
            text="Clients",
            font=("Arial", 18, "bold"),
            width=160,
            height=40,
            corner_radius=0,
            bg_color=self.bg_color,
            command=self.change_to_client_view,
        )
        self.client_button.pack(pady=0, fill="x")

        self.flight_button = ctk.CTkButton(
            master=sidebar_frame,
            text="Flights",
            font=("Arial", 18, "bold"),
            width=160,
            height=40,
            corner_radius=0,
            bg_color=self.bg_color,
            fg_color="transparent",
            command=self.change_to_flight_view,
        )
        self.flight_button.pack(pady=0, fill="x")

        self.airline_button = ctk.CTkButton(
            master=sidebar_frame,
            text="Airlines",
            font=("Arial", 18, "bold"),
            width=160,
            height=40,
            corner_radius=0,
            bg_color=self.bg_color,
            fg_color="transparent",
            command=self.change_to_airline_view,
        )
        self.airline_button.pack(pady=0, fill="x")

        # New record buttons at bottom of sidebar
        add_airline_button = ctk.CTkButton(
            master=sidebar_frame,
            text="+ New Airline",
            font=("Arial", 18, "bold"),
            width=160,
            height=40,
            corner_radius=0,
            bg_color=self.bg_color,
            command=self.create_airline_handler,
        )
        add_airline_button.pack(pady=10, side="bottom")

        add_flight_button = ctk.CTkButton(
            master=sidebar_frame,
            text="+ New Flight",
            font=("Arial", 18, "bold"),
            width=160,
            height=40,
            corner_radius=0,
            bg_color=self.bg_color,
            command=self.create_flight_handler,
        )
        add_flight_button.pack(pady=10, side="bottom")

        add_client_button = ctk.CTkButton(
            master=sidebar_frame,
            text="+ New Client",
            font=("Arial", 18, "bold"),
            width=160,
            height=40,
            corner_radius=0,
            bg_color=self.bg_color,
            command=self.create_client_handler,
        )
        add_client_button.pack(pady=10, side="bottom")

        self.update_tabs()

    def set_active_tab(self, new_active):
        self.active_tab = new_active
        self.update_tabs()

    def update_tabs(self):
        self.client_button.configure(fg_color="transparent")
        self.airline_button.configure(fg_color="transparent")
        self.flight_button.configure(fg_color="transparent")
        if self.active_tab == "client":
            self.client_button.configure(fg_color=["#3B8ED0", "#1F6AA5"])
        elif self.active_tab == "airline":
            self.airline_button.configure(fg_color=["#3B8ED0", "#1F6AA5"])
        else:
            self.flight_button.configure(fg_color=["#3B8ED0", "#1F6AA5"])

    def change_to_client_view(self):
        self.set_active_tab("client")
        self.view_change_handler("client")

    def change_to_airline_view(self):
        self.set_active_tab("airline")
        self.view_change_handler("airline")

    def change_to_flight_view(self):
        self.set_active_tab("flight")
        self.view_change_handler("flight")

    def create_client_handler(self):
        self.create_handler("client")

    def create_airline_handler(self):
        self.create_handler("airline")

    def create_flight_handler(self):
        self.create_handler("flight")
