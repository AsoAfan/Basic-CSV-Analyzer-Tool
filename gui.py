from tkinter import filedialog, messagebox

import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame

from csv_generator import CSVGenerator
from plot import plot_graph
from stats import compute_statistics
from utils import load_csv, set_appearance_mode


class CSVAnalyzerApp:
    def __init__(self, root):

        self.df: DataFrame = None

        self.root = root
        self.root.title("CSV Analyzer")
        self.root.geometry("1000x600")
        self.root.minsize(800, 500)

        self.sidebar = ctk.CTkFrame(root, width=220, corner_radius=10)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        self.file_label = ctk.CTkLabel(self.sidebar, text="No file uploaded", wraplength=180)
        self.file_label.pack(pady=5)

        self.upload_btn = ctk.CTkButton(self.sidebar, text="Upload CSV", command=self.load_csv)
        self.upload_btn.pack(pady=10, padx=10)

        self.column_var = ctk.StringVar()
        self.column_dropdown = ctk.CTkComboBox(
            master=self.sidebar,
            border_width=0,
            variable=self.column_var,
            values=[],
            state="readonly", command=lambda
                _: self.compute_statistics() if self.df is not None else None)

        self.column_dropdown.pack(pady=10, padx=10)

        self.color_var = ctk.StringVar(value="green")
        self.color_dropdown = ctk.CTkComboBox(
            self.sidebar, border_width=0, variable=self.color_var, values=["blue", "red", "green", "purple", "orange"],
            command=lambda _: self.compute_statistics() if self.df is not None else None
        )

        self.color_dropdown.pack(pady=10, padx=10)

        self.stats_btn = ctk.CTkButton(self.sidebar, text="Compute Statistics", command=self.compute_statistics)
        self.stats_btn.pack(pady=10, padx=10)

        self.generate_csv_button = ctk.CTkButton(self.sidebar, text="Generate CSV", command=self.open_csv_generator)
        self.generate_csv_button.pack(pady=10, padx=10)

        self.main_frame = ctk.CTkFrame(root)
        self.main_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

        self.stats_frame = ctk.CTkFrame(self.main_frame)
        self.stats_frame.pack(fill="x", padx=10, pady=10)

        self.stats_label = ctk.CTkLabel(self.stats_frame, text="Statistics", font=("Arial", 16, "bold"))
        self.stats_label.pack(pady=5)

        self.stats_text = ctk.CTkTextbox(self.stats_frame, height=100, font=("Arial", 12))
        self.stats_text.pack(fill="x", padx=10, pady=10)

        self.figure, self.ax = plt.subplots(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self.main_frame)
        self.canvas.get_tk_widget().pack(expand=True, fill="both", padx=10, pady=10)

        self.nav_frame = ctk.CTkFrame(root, width=200, corner_radius=10)
        self.nav_frame.pack(side="right", fill="y", padx=10, pady=10)

        appearance_mode_var = ctk.StringVar(value="system")
        self.theme_btn = ctk.CTkSegmentedButton(
            master=self.nav_frame,
            values=["system", "dark", "light"],
            variable=appearance_mode_var,
            command=lambda _: set_appearance_mode(appearance_mode_var.get())
        )
        self.theme_btn.pack(pady=10, padx=10)

        self.graph_var = ctk.StringVar(value="Histogram")
        graph_types = ["Histogram", "Box Plot", "Scatter Plot", "Line Chart", "Bar Chart", "Pie Chart"]

        for graph in graph_types:
            btn = ctk.CTkButton(
                self.nav_frame,
                text=graph,
                command=lambda g=graph: self.set_graph_type(g)
            )
            btn.pack(pady=5, padx=10, fill="x")

        self.csv_generator = None

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        self.file_label.configure(text=f"File: {file_path.split('/')[-1]}")
        self.df = load_csv(file_path)

        if self.df is None:
            return

        numerical_columns = self.df.select_dtypes(include=[np.number]).columns.tolist()

        if not numerical_columns:
            messagebox.showerror("Error", "No numerical columns found in CSV.")
            return

        max_rows = 1000
        if self.df.shape[0] > max_rows:
            messagebox.showerror("Error",
                                 f"Too many rows in CSV.\n Maximum number of rows is {max_rows}.\n CSV has {self.df.shape[0]} rows.")
            return

        self.column_dropdown.configure(values=numerical_columns)
        self.column_var.set(numerical_columns[0])

        messagebox.showinfo("Success", "CSV file loaded successfully.")

    def set_graph_type(self, graph_type):
        self.graph_var.set(graph_type)
        self.compute_statistics()

    def compute_statistics(self):
        if self.df is None:
            messagebox.showerror("Error", "No CSV file loaded.")
            return

        column = self.column_var.get()
        if not column:
            messagebox.showerror("Error", "Please select a column.")
            return

        data = self.df[column].dropna()
        if data.empty:
            messagebox.showerror("Error", "Selected column has no valid data.")
            return

        stats_text = compute_statistics(data)
        self.stats_text.delete("0.0", "end")
        self.stats_text.insert("0.0", stats_text)

        self.ax.clear()
        plot_graph(self.ax, data, column, self.color_var.get(), self.graph_var.get())
        self.canvas.draw()

    def open_csv_generator(self):
        if self.csv_generator is None:
            self.csv_generator = CSVGenerator(self.root)
        self.csv_generator.show()
