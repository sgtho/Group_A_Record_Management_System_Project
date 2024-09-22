import customtkinter as ctk
from data.client_repository import ClientRepository

class App:
    def __init__(self, client_repo: ClientRepository):
        self.client_repo = client_repo

        # build UI
        self.build_app()

    def start(self):
        self.app.mainloop()

    def build_app(self):
        app = ctk.CTk()  
        app.geometry("400x200")
        app.title("CustomTkinter Example")

        def on_button_click():
            print("Hello, World!")

        button = ctk.CTkButton(master=app, text="Click Me!", command=on_button_click)
        button.pack(pady=20)

        self.app = app