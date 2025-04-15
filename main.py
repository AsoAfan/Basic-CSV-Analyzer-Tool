import customtkinter as ctk

from app.gui import CSVAnalyzerApp

if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = CSVAnalyzerApp(root)
    root.mainloop()
