import tkinter as tk
from tkinter import ttk, messagebox


class IDCardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ID Card Generator")
        self.geometry("440x520")
        self.resizable(False, False)

        style = ttk.Style()
        style.configure("Header.TLabel", font=("Segoe UI", 15, "bold"))
        style.configure("Card.TLabel", font=("Consolas", 10), background="#ffffff")

        ttk.Label(self, text="ID Card Generator", style="Header.TLabel").pack(pady=(15, 10))

        form = ttk.Frame(self, padding=15)
        form.pack(fill="x")

        ttk.Label(form, text="Full Name:").pack(anchor="w")
        self.name_entry = ttk.Entry(form)
        self.name_entry.pack(fill="x", pady=(2, 10))

        ttk.Label(form, text="Age:").pack(anchor="w")
        self.age_entry = ttk.Entry(form)
        self.age_entry.pack(fill="x", pady=(2, 10))

        ttk.Label(form, text="Role / Additional Info:").pack(anchor="w")
        self.info_entry = ttk.Entry(form)
        self.info_entry.pack(fill="x", pady=(2, 15))

        btn = ttk.Button(form, text="Generate ID Card", command=self.generate_card)
        btn.pack(fill="x")

        self.card_frame = tk.Frame(self, bg="black", bd=1)
        self.card_label = ttk.Label(self.card_frame, justify="left", style="Card.TLabel", padding=8)
        self.card_label.pack()

    def generate_card(self):
        name = self.name_entry.get().strip()
        age_str = self.age_entry.get().strip()
        info = self.info_entry.get().strip()

        if not name or len(name.split()) < 2:
            messagebox.showerror("Error", "Please enter both a first and last name.")
            return

        if not age_str.isdigit() or not (1 <= int(age_str) <= 120):
            messagebox.showerror("Error", "Please enter a valid age between 1 and 120.")
            return

        if not info:
            messagebox.showerror("Error", "Please enter role or extra information.")
            return

        name = " ".join([w.capitalize() for w in name.split()])
        info = info[:24]

        card = (
            "+--------------------------------------+\n"
            "|         IDENTIFICATION CARD          |\n"
            "+--------------------------------------+\n"
            f"| Name : {name:<29} |\n"
            f"| Age  : {age_str:<29} |\n"
            f"| Info : {info:<29} |\n"
            "+--------------------------------------+"
        )

        self.card_label.config(text=card)
        self.card_frame.pack(pady=15)


if __name__ == "__main__":
    app = IDCardApp()
    app.mainloop()