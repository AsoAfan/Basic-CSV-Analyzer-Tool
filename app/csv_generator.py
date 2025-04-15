import random
import time
from tkinter import messagebox

import customtkinter as ctk
import pandas as pd


class CSVGenerator:
    def __init__(self, root):
        self.window = ctk.CTkToplevel(root)
        self.window.title("CSV Generator")
        self.window.geometry("500x400")
        self.window.resizable(False, False)

        self.column_entry = ctk.CTkEntry(self.window, placeholder_text="Enter column names (comma separated)")
        self.column_entry.pack(pady=10, padx=10, fill="x")

        self.row_entry = ctk.CTkEntry(self.window, placeholder_text="Enter number of rows")
        self.row_entry.pack(pady=10, padx=10, fill="x")

        self.progress_label = ctk.CTkLabel(self.window, text="", font=("Arial", 12))
        self.progress_label.pack(pady=5)

        self.generate_btn = ctk.CTkButton(self.window, text="Generate CSV", command=self.generate_csv)
        self.generate_btn.pack(pady=10, padx=10)

    def show(self):
            self.window.deiconify()


    def generate_csv(self):
        column_names = self.column_entry.get().split(",")
        try:
            num_rows = int(self.row_entry.get())
            if num_rows <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number of rows.")
            return

        self.progress_label.configure(text="Generating CSV... Please wait.")
        self.window.update_idletasks()

        data = {col.strip(): [random.randint(1, 100) for _ in range(num_rows)] for col in column_names}

        data = {"#": list(range(1, num_rows + 1)), **data}

        df = pd.DataFrame(data)
        file_path = "data/generated_data_" + time.strftime("%Y_%m_%d_%H_%M_%p") + ".csv"
        df.to_csv(file_path, index=False)

        self.progress_label.configure(text=f"CSV saved: {file_path}")
