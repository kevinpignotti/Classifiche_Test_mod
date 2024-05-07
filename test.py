import tkinter as tk
from tkinter import ttk
import sqlite3
from registrazione_risultati import registra_risultati
import re


def limit_input(*args):
    max_range = len(dizionario_entry) // 2 + 1
    for z in range(1, max_range):
        if z % 3 != 0:
            value = dizionario_entry[f"entry{z}"].get()
            if len(value) > 2:
                dizionario_entry[f"entry{z}"].set(value[:2])
            elif not re.match("^[0-9]*$", value):
                dizionario_entry[f"entry{z}"].set(value[:-1])
        else:
            value = dizionario_entry[f"entry{z}"].get()
            if len(value) > 3:
                dizionario_entry[f"entry{z}"].set(value[:3])
            elif not re.match("^[0-9]*$", value):
                dizionario_entry[f"entry{z}"].set(value[:-1])

        #TODO: limitare il massimo di valore dei secondi a 59


def elenco_gare():
    conn = sqlite3.connect('formula1.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Circuito FROM Gare")
    elenco_gare = [row[0] for row in cursor.fetchall()]
    conn.close()
    return elenco_gare


def elenco_piloti():
    conn = sqlite3.connect('formula1.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Piloti")
    elenco_piloti = [row[0] for row in cursor.fetchall()]
    conn.close()
    return elenco_piloti


def leggi_risultati(piloti_comboboxes, circuito, best_laps):
    circuito_gara = circuito.get()
    ordine_di_arrivo = [pilota_combobox.get() for pilota_combobox in piloti_comboboxes]

    # Estrai i giri veloci dalle caselle di testo
    migliori_giri = []
    for entry in best_laps:
        min_miglior_giro = entry[0].get()
        sec_miglior_giro = entry[1].get()
        mill_miglior_giro = entry[2].get()
        miglior_giro = f"{min_miglior_giro}:{sec_miglior_giro}.{mill_miglior_giro}"
        migliori_giri.append(miglior_giro)

    # Registra i risultati con i giri veloci
    registra_risultati(ordine_di_arrivo, migliori_giri, circuito_gara)

finestra = tk.Tk()
finestra.title("Registra Risultati")

# Label per la selezione della gara
gara_label = ttk.Label(finestra, text="Circuit:")
gara_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

gara_var = tk.StringVar()
gara_combobox = ttk.Combobox(finestra, textvariable=gara_var, width=20, state="readonly")
gara_combobox.grid(row=0, column=1, padx=5, pady=5)
gara_combobox['values'] = elenco_gare()

# Label e Combobox per l'ordine di arrivo dei piloti
piloti_comboboxes = []
giri_migliori = []
dizionario_entry = {}
z = 0

for i in range(1, 11):  # Supponendo che ci siano al massimo 10 piloti in una gara

    z += 1

    pilota_label = ttk.Label(finestra, text=f"{i} place:")
    pilota_label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

    pilota_combobox = ttk.Combobox(finestra, width=20, state="readonly")
    pilota_combobox.grid(row=i, column=1, padx=5, pady=5)
    piloti_comboboxes.append(pilota_combobox)
    piloti_comboboxes[i-1]['values'] = elenco_piloti()

    giro_label1 = ttk.Label(finestra, text="Best Lap:")
    giro_label1.grid(row=i, column=2, padx=5, pady=5, sticky="w")

    dizionario_entry[f"entry{z}"] = tk.StringVar()
    dizionario_entry[f'entry{z}'].trace('w', limit_input)

    dizionario_entry[f"entry_box{z}"] = tk.Entry(finestra, textvariable=dizionario_entry[f'entry{z}'], width=4)
    dizionario_entry[f"entry_box{z}"].grid(row=i, column=3, padx=5, pady=5)

    giro_label2 = ttk.Label(finestra, text=":")
    giro_label2.grid(row=i, column=4, padx=5, pady=5, sticky="w")

    z += 1
    dizionario_entry[f"entry{z}"] = tk.StringVar()
    dizionario_entry[f'entry{z}'].trace('w', limit_input)

    dizionario_entry[f"entry_box{z}"] = tk.Entry(finestra, textvariable=dizionario_entry[f'entry{z}'], width=4)
    dizionario_entry[f"entry_box{z}"].grid(row=i, column=5, padx=5, pady=5)

    # entry2 = tk.StringVar()
    # entry2.trace('w', limit_input)
    #
    # entry_box2 = tk.Entry(finestra, textvariable=entry2, width=4)
    # entry_box2.grid(row=i, column=5, padx=5, pady=5)

    giro_label3 = ttk.Label(finestra, text=".")
    giro_label3.grid(row=i, column=6, padx=5, pady=5, sticky="w")

    z += 1
    dizionario_entry[f"entry{z}"] = tk.StringVar()
    dizionario_entry[f'entry{z}'].trace('w', limit_input)

    dizionario_entry[f"entry_box{z}"] = tk.Entry(finestra, textvariable=dizionario_entry[f'entry{z}'], width=4)
    dizionario_entry[f"entry_box{z}"].grid(row=i, column=7, padx=5, pady=5)
    # entry3 = tk.StringVar()
    # entry3.trace('w', limit_input)
    #
    # entry_box3 = tk.Entry(finestra, textvariable=entry3, width=4)
    # entry_box3.grid(row=i, column=7, padx=5, pady=5)

    giri_migliori.append(
        [dizionario_entry[f"entry_box{z-2}"],
         dizionario_entry[f"entry_box{z-1}"],
         dizionario_entry[f"entry_box{z}"]])

# Bottone per confermare e registrare i risultati
conferma_button = ttk.Button(finestra, text="Conferma",
                             command=lambda: leggi_risultati(piloti_comboboxes, gara_combobox, giri_migliori))
conferma_button.grid(row=13, columnspan=2, padx=5, pady=10)

finestra.mainloop()

