import sqlite3
import re
import tkinter as tk
from tkinter import ttk


# def on_option_selected():
#     # Funzione chiamata quando viene selezionata un'opzione
#     selected_option = gioco.get()
#
#     # # Rimuovere i radiobutton precedentemente creati
#     # for widget in options_frame.winfo_children():
#     #     widget.destroy()
#
#     # Creare i nuovi radiobutton in base all'opzione selezionata
#     if selected_option == 1:
#         categoria_f1.grid(row=1, column=0, sticky="w")
#         categoria_moto.grid_forget()  # Nascondere l'altro frame
#     elif selected_option == 2:
#         categoria_moto.grid(row=1, column=0, sticky="w")
#         categoria_f1.grid_forget()  # Nascondere l'altro frame

def limit_input(dizionario_entry, *args):
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

        # TODO: limitare il massimo di valore dei secondi a 59


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


def registra_risultati(classifica_di_arrivo, best_lap, circuito):
    # Ottieni l'ordine di arrivo dei piloti

    # Connessione al database SQLite
    conn = sqlite3.connect('formula1.db')
    cursor = conn.cursor()

    # Inserisci i risultati nel database
    cursor.execute("SELECT MAX(ID_Risultato) FROM Risultati")
    max_id = cursor.fetchone()[0] or 0

    # Cerca l'ID_Gara corrispondente al nome del circuito fornito
    cursor.execute("SELECT ID_Gara FROM Gare WHERE Circuito = ?", (circuito,))
    circuito_id = cursor.fetchone()[0] or 0

    # Cerca l'ID_Pilota corrispondente al nome del pilota fornito
    lista_id_piloti = []
    for nome in classifica_di_arrivo:
        cursor.execute("SELECT ID_Pilota FROM Piloti WHERE Nome = ?", (nome,))
        pilota_id_ricerca = cursor.fetchone()[0] or 0
        lista_id_piloti.append(pilota_id_ricerca)

    # Cerca l'ID_Squadra corrispondente al nome del pilota fornito
    lista_id_team = []
    for id_pilota in lista_id_piloti:
        cursor.execute("SELECT ID_Squadra FROM Piloti WHERE ID_Pilota = ?", (id_pilota,))
        pilota_id_ricerca = cursor.fetchone()[0] or 0
        lista_id_team.append(pilota_id_ricerca)

    for posizione, pilota_id in enumerate(lista_id_piloti, start=1):
        id_pilota = lista_id_piloti[posizione - 1]
        id_team = lista_id_team[posizione - 1]
        miglior_giro = best_lap[posizione - 1]
        cursor.execute("INSERT INTO Risultati VALUES (?, ?, ?, ?, ?, ?)",
                       (max_id + posizione, circuito_id, id_pilota, posizione, miglior_giro, id_team))

    # Chiudi la connessione al database
    conn.commit()
    conn.close()

    # TODO: una volta registrati i dati deve comparire una finestra di conferma
    print('Risultati inseriti correttamente')


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


def inserisci():
    finestra = tk.Tk()
    finestra.title("Registra Risultati")

    # # Radiobutton per scelta gioco
    # gioco = tk.IntVar()
    # r1_1 = ttk.Radiobutton(finestra, text="Opzione A1", variable=gioco, value=1, command=on_option_selected)
    # r1_1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    # r1_2 = ttk.Radiobutton(finestra, text="Opzione B1", variable=gioco, value=2, command=on_option_selected)
    # r1_2.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    #
    # # Radiobutton per scelta categoria
    # categoria_f1 = tk.IntVar()
    # r2_1 = ttk.Radiobutton(finestra, text="Opzione A1_1", variable=categoria_f1, value=1)
    # r2_1.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    # r2_2 = ttk.Radiobutton(finestra, text="Opzione A1_2", variable=categoria_f1, value=2)
    # r2_2.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    # r2_3 = ttk.Radiobutton(finestra, text="Opzione A1_3", variable=categoria_f1, value=3)
    # r2_3.grid(row=1, column=2, padx=5, pady=5, sticky="w")
    #
    # categoria_moto = tk.IntVar()
    # r2_1 = ttk.Radiobutton(finestra, text="Opzione A1_1", variable=categoria_moto, value=1)
    # r2_1.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    # r2_2 = ttk.Radiobutton(finestra, text="Opzione A1_2", variable=categoria_moto, value=2)
    # r2_2.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    # r2_3 = ttk.Radiobutton(finestra, text="Opzione A1_3", variable=categoria_moto, value=3)
    # r2_3.grid(row=1, column=2, padx=5, pady=5, sticky="w")


    # Label per la selezione del circuito
    gara_label = ttk.Label(finestra, text="Circuit:")
    gara_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    gara_var = tk.StringVar()
    gara_combobox = ttk.Combobox(finestra, textvariable=gara_var, width=20, state="readonly")
    gara_combobox.grid(row=2, column=1, padx=5, pady=5)
    gara_combobox['values'] = elenco_gare()

    # Label e Combobox per l'ordine di arrivo dei piloti
    piloti_comboboxes = []
    giri_migliori = []
    dizionario_entry = {}

    z = 0
    max_piloti = 4

    for i in range(1, max_piloti + 1):  # Supponendo che ci siano al massimo 4 piloti in una gara

        z += 1

        pilota_label = ttk.Label(finestra, text=f"{i} place:")
        pilota_label.grid(row=i + 2, column=0, padx=5, pady=5, sticky="w")

        pilota_combobox = ttk.Combobox(finestra, width=20, state="readonly")
        pilota_combobox.grid(row=i + 2, column=1, padx=5, pady=5)
        piloti_comboboxes.append(pilota_combobox)
        piloti_comboboxes[i - 1]['values'] = elenco_piloti()

        giro_label1 = ttk.Label(finestra, text="Best Lap:")
        giro_label1.grid(row=i + 2, column=2, padx=5, pady=5, sticky="w")

        dizionario_entry[f"entry{z}"] = tk.StringVar()
        dizionario_entry[f'entry{z}'].trace('w', lambda *args, entry=dizionario_entry: limit_input(entry))

        dizionario_entry[f"entry_box{z}"] = tk.Entry(finestra, textvariable=dizionario_entry[f'entry{z}'], width=4)
        dizionario_entry[f"entry_box{z}"].grid(row=i + 2, column=3, padx=5, pady=5)

        giro_label2 = ttk.Label(finestra, text=":")
        giro_label2.grid(row=i + 2, column=4, padx=5, pady=5, sticky="w")

        z += 1
        dizionario_entry[f"entry{z}"] = tk.StringVar()
        dizionario_entry[f'entry{z}'].trace('w', lambda *args, entry=dizionario_entry: limit_input(entry))

        dizionario_entry[f"entry_box{z}"] = tk.Entry(finestra, textvariable=dizionario_entry[f'entry{z}'], width=4)
        dizionario_entry[f"entry_box{z}"].grid(row=i + 2, column=5, padx=5, pady=5)

        giro_label3 = ttk.Label(finestra, text=".")
        giro_label3.grid(row=i + 2, column=6, padx=5, pady=5, sticky="w")

        z += 1
        dizionario_entry[f"entry{z}"] = tk.StringVar()
        dizionario_entry[f'entry{z}'].trace('w', lambda *args, entry=dizionario_entry: limit_input(entry))

        dizionario_entry[f"entry_box{z}"] = tk.Entry(finestra, textvariable=dizionario_entry[f'entry{z}'], width=4)
        dizionario_entry[f"entry_box{z}"].grid(row=i + 2, column=7, padx=5, pady=5)

        giri_migliori.append(
            [dizionario_entry[f"entry_box{z - 2}"],
             dizionario_entry[f"entry_box{z - 1}"],
             dizionario_entry[f"entry_box{z}"]])

    # Bottone per confermare e registrare i risultati
    conferma_button = ttk.Button(finestra, text="Conferma",
                                 command=lambda: leggi_risultati(piloti_comboboxes, gara_combobox, giri_migliori))
    conferma_button.grid(row=max_piloti + 3, columnspan=2, padx=5, pady=10)

    finestra.mainloop()


if __name__ == "__main__":
    inserisci()


