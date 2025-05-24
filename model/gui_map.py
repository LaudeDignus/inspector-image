import tkinter as tk
from tkinter import filedialog, messagebox
from model import map_info

def launch_gui():
    def select_image():
        file_path = filedialog.askopenfilename(title="Choisir une image", filetypes=[("Images", "*.jpg *.jpeg")])
        if not file_path:
            return
        try:
            map_info.extract_map(file_path)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur : {e}")

    root = tk.Tk()
    root.title("Extracteur GPS")

    frame = tk.Frame(root, padx=60, pady=60)
    frame.pack()

    btn = tk.Button(frame, text="📁 Sélectionner une image", command=select_image)
    btn.pack(pady=10)

    root.mainloop()
