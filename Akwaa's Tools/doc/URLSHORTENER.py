from tkinter import Entry
import customtkinter as ctk
import pyshorteners

def shorten_url():
    url = Entry.get()
    if url:
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            result_label.configure(text=f"URL Raccourci : {short_url}")
        except Exception as e:
            result_label.configure(text=f"Error : {str(e)}")

app = ctk.CTk()
app.geometry("400x200")
app.title("URL Shortener")

ctk.set_appearance_mode("dark")
label = ctk.CTkLabel(app, text="Entrez votre URL : ", font=("Arial", 14))
label.pack(pady=10)

entry = ctk.CTkEntry(app, width=100, font=("Arial", 12))
entry.pack(pady=5)

shorten_button = ctk.CTkButton(app, text="Raccourcir l'URL", command=shorten_url)
shorten_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
result_label.pack(pady=10)

app.mainloop()