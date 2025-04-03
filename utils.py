from tkinter import messagebox
from typing import Callable

import customtkinter
import pandas as pd


def load_csv(file_path: str):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load CSV: {e}")
        return None


def run_if_value_exists(value, callback: Callable):
    if value is not None:
        callback()


def set_appearance_mode(value: str):
    customtkinter.set_appearance_mode(value)
