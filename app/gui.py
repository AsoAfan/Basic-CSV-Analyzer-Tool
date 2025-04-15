from tkinter import filedialog, messagebox
import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
from app.csv_generator import CSVGenerator
from app.plot import plot_graph
from app.stats import compute_statistics
from app.utils import load_csv, set_appearance_mode


class CSVAnalyzerApp:
    def __init__(self, root, ):

        self.df: DataFrame|None = None
        self.table_header_row = None
        self.root = root
        self.root.title("CSV Analyzer")
        self.root.geometry("1000x600")
        self.root.minsize(800, 500)

        self.headers = []
        self.rows = []

        self.current_page = 0
        self.rows_per_page = 25

        # SIDEBAR - START
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
        # SIDEBAR - END
        # ================
        # MAIN - START
        self.main_frame = ctk.CTkFrame(root, corner_radius=24)
        self.main_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)


        self.tab_view = ctk.CTkTabview(self.main_frame, fg_color="transparent", corner_radius=4)
        self.tab_view.pack( fill="both", expand=True, ipadx=10, ipady=10)
        self.tab_view.add("main")
        self.tab_view.add("table")

        # TABLE_TAB - START

        self.table_frame = ctk.CTkFrame(self.tab_view.tab("table"))
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)



        self.table_header_row = ctk.CTkFrame(self.table_frame)
        self.table_header_row.pack(fill="x", anchor="n", padx=12, pady=10)

        self.scrollable_frame = ctk.CTkScrollableFrame(self.table_frame)
        self.scrollable_frame.pack(fill="both", expand=True)

        self.pagination_frame = ctk.CTkFrame(self.table_frame)
        self.pagination_frame.pack(fill="x", pady=5)

        self.pagination_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.pagination_frame.grid_rowconfigure(0)

        self.prev_btn = ctk.CTkButton(self.pagination_frame, text="Previous", command=self.show_previous_page)
        self.prev_btn.grid(row=0, column=0, sticky="w", padx=20)

        self.page_label = ctk.CTkLabel(self.pagination_frame, text="Page 1")
        self.page_label.grid(row=0, column=1, sticky="nsew")

        self.next_btn = ctk.CTkButton(self.pagination_frame, text="Next", command=self.show_next_page)
        self.next_btn.grid(row=0, column=2, sticky="e", padx=20)

        # TABLE_TAB - END

        # Stats frame - START
        self.stats_frame = ctk.CTkFrame(self.tab_view.tab("main"), fg_color=("#cfcfcf", "#333333") )
        self.stats_frame.pack(fill="x", padx=10, pady=10)

        self.stats_label = ctk.CTkLabel(self.stats_frame, text="Statistics", font=("Arial", 16, "bold"))
        self.stats_label.pack(pady=5)

        self.stats_text = ctk.CTkTextbox(self.stats_frame, height=100, font=("Arial", 12))
        self.stats_text.pack(fill="x", padx=10, pady=10)
        # STATS FRAME - END

        # GRAPH - START
        self.figure, self.ax = plt.subplots(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self.tab_view.tab("main"))
        self.canvas.get_tk_widget().pack(expand=True, fill="both", padx=10, pady=10)

        # LEFT_SIDE - START
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
        for label in self.headers:
            label.destroy()

        for col_index, col_name in enumerate(self.df.columns):
            label = ctk.CTkLabel(
                self.table_header_row,
                text=col_name,
                anchor="center",
                justify="center",
                width=100
            )
            label.grid(row=0, column=col_index, padx=10, pady=5, sticky="nsew")
            self.headers.append(label)

        for col_index in range(len(numerical_columns)):
            self.table_header_row.grid_columnconfigure(col_index, weight=1)
        self.column_dropdown.configure(values=numerical_columns)
        self.column_var.set(numerical_columns[0])

        print(self.df.values)



        self.current_page = 0
        self.show_page(self.current_page)


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

        self.tab_view.set("main")


        stats_text = compute_statistics(data)
        self.stats_text.delete("0.0", "end")
        self.stats_text.insert("0.0", stats_text)

        self.ax.clear()
        plot_graph(self.ax, data, column, self.color_var.get(), self.graph_var.get())
        self.canvas.draw()

    def open_csv_generator(self):
        if self.csv_generator is None:
            self.csv_generator = CSVGenerator(self.root)
        else:
            try:
                self.csv_generator.show()
            except Exception:
                self.csv_generator = CSVGenerator(self.root)

    def show_page(self, page_num):
        if self.df is None:
            return

        total_rows = len(self.df)
        start = page_num * self.rows_per_page
        end = start + self.rows_per_page

        for row in self.rows:
            row.destroy()
        self.rows.clear()

        for index in range(start, min(end, total_rows)):
            data_row = self.df.iloc[index]
            row_frame = ctk.CTkFrame(self.scrollable_frame)
            row_frame.pack(fill="x", expand=True, padx=10, pady=5)
            self.rows.append(row_frame)

            for col_index, cell in enumerate(data_row):
                label = ctk.CTkLabel(
                    row_frame,
                    text=cell,
                    anchor="center",
                    justify="center",
                    width=100
                )
                label.grid(row=0, column=col_index, padx=10, pady=5, sticky="nsew")

            for col_index in range(len(data_row)):
                row_frame.grid_columnconfigure(col_index, weight=1)

        self.page_label.configure(text=f"Page {page_num + 1}")

        if total_rows <= self.rows_per_page:
            self.pagination_frame.pack_forget()
        else:
            self.pagination_frame.pack(fill="x", pady=5)
            self.prev_btn.grid_forget()
            self.next_btn.grid_forget()

            if page_num > 0:
                self.prev_btn.grid(row=0, column=0, padx=10)

            if end < total_rows:
                self.next_btn.grid(row=0, column=2, padx=10)

    def show_next_page(self):
        if self.df is not None and (self.current_page + 1) * self.rows_per_page < len(self.df):
            self.current_page += 1
            self.show_page(self.current_page)

    def show_previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.show_page(self.current_page)


