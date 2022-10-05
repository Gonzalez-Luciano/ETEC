import tkinter as tk
from tkinter import ttk

style = ttk.Style()
style.theme_create( "yummy", parent="clam", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0],"background": "#FFFFFF", } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": "#FFFFFF" },
            "map":       {"background": [("selected", "#8CD0F7")],
                        "expand": [("selected", [2, 2, 2, 0])] } } } )
style.theme_use("yummy")