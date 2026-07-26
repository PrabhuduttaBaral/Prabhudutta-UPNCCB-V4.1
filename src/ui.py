"""
==========================================================
Prabhudutta-UPNCCB V4.1
UI Module
==========================================================
"""

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class AppUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Prabhudutta-UPNCCB V4.1 Professional")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        # -----------------------------
        # Status
        # -----------------------------
        self.status = tk.StringVar(value="Ready")

        ttk.Label(
            self.root,
            text="Status:"
        ).pack(anchor="w", padx=10, pady=(10, 0))

        ttk.Label(
            self.root,
            textvariable=self.status,
            foreground="blue"
        ).pack(anchor="w", padx=10)

        # -----------------------------
        # Buttons
        # -----------------------------
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        self.btn_start = ttk.Button(frame, text="START")
        self.btn_start.grid(row=0, column=0, padx=5)

        self.btn_stop = ttk.Button(frame, text="STOP")
        self.btn_stop.grid(row=0, column=1, padx=5)

        # -----------------------------
        # Progress
        # -----------------------------
        self.progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=700,
            mode="determinate"
        )

        self.progress.pack(pady=10)

        # -----------------------------
        # Log Window
        # -----------------------------
        self.log = ScrolledText(
            self.root,
            width=105,
            height=28
        )

        self.log.pack(padx=10, pady=10)

    def write_log(self, message):

        self.log.insert(tk.END, message + "\n")
        self.log.see(tk.END)

    def set_status(self, text):

        self.status.set(text)

    def run(self):

        self.root.mainloop()