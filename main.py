import tkinter as tk
import win32api  # Per Windows
import finestra_inserimento_risultati


def modifica_dati_pilota():
    # Aggiungi qui la logica per modificare i dati del pilota
    print("Dati del pilota modificati")


def modifica_risultati():
    # Aggiungi qui la logica per modificare i risultati
    print("Risultati modificati")


def inserisci_nuovo_risultato():
    finestra_inserimento_risultati.inserisci()
    print("Inserisci nuovo risultato")



# Ottenere le dimensioni dello schermo
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)

# Calcola le dimensioni della finestra come un quarto dello schermo
window_width = int(width / 2)
window_height = int(height / 2)

# Creazione della finestra principale
root = tk.Tk()
root.title("Programma Test Kevin")

# Impostare le dimensioni della finestra
root.geometry(f"{window_width}x{window_height}")

# Frame per contenere i pulsanti
button_frame = tk.Frame(root)
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Pulsante per registrare risultati
btn_registra_risultati = tk.Button(button_frame,
                                   text="Inserisci nuovo risultato",
                                   command=inserisci_nuovo_risultato)
btn_registra_risultati.pack(pady=15)

# Pulsante per modificare i dati del pilota
btn_modifica_dati_pilota = tk.Button(button_frame,
                                     text="Modifica Dati Pilota",
                                     command=modifica_dati_pilota)
btn_modifica_dati_pilota.pack(pady=15)

# Pulsante per modificare risultati
btn_modifica_risultati = tk.Button(button_frame,
                                   text="Modifica Risultati",
                                   command=modifica_risultati)
btn_modifica_risultati.pack(pady=15)

# Avvio della finestra principale
root.mainloop()
