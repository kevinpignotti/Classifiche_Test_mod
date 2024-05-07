import sqlite3

import re

# def registra_risultati(classifica_di_arrivo, best_lap, circuito):
#     # Ottieni l'ordine di arrivo dei piloti
#
#     # Connessione al database SQLite
#     conn = sqlite3.connect('formula1.db')
#     cursor = conn.cursor()
#
#     # Inserisci i risultati nel database
#     cursor.execute("SELECT MAX(ID_Risultato) FROM Risultati")
#     max_id = cursor.fetchone()[0] or 0
#
#     # Cerca l'ID_Gara corrispondente al nome del circuito fornito
#     cursor.execute("SELECT ID_Gara FROM Gare WHERE Circuito = ?", (circuito,))
#     circuito_id = cursor.fetchone()[0] or 0
#
#     # Cerca l'ID_Pilota corrispondente al nome del pilota fornito
#     lista_id_piloti = []
#     for nome in classifica_di_arrivo:
#         cursor.execute("SELECT ID_Pilota FROM Piloti WHERE Nome = ?", (nome,))
#         pilota_id_ricerca = cursor.fetchone()[0] or 0
#         lista_id_piloti.append(pilota_id_ricerca)
#
#     # Cerca l'ID_Squadra corrispondente al nome del pilota fornito
#     lista_id_team = []
#     for id_pilota in lista_id_piloti:
#         cursor.execute("SELECT ID_Squadra FROM Piloti WHERE ID_Pilota = ?", (id_pilota,))
#         pilota_id_ricerca = cursor.fetchone()[0] or 0
#         lista_id_team.append(pilota_id_ricerca)
#
#     for posizione, pilota_id in enumerate(lista_id_piloti, start=1):
#         id_pilota = lista_id_piloti[posizione - 1]
#         id_team = lista_id_team[posizione - 1]
#         miglior_giro = best_lap[posizione - 1]
#         cursor.execute("INSERT INTO Risultati VALUES (?, ?, ?, ?, ?, ?)",
#                        (max_id + posizione, circuito_id, id_pilota, posizione, miglior_giro, id_team))
#
#     # Chiudi la connessione al database
#     conn.commit()
#     conn.close()
#
#     #TODO: una volta registrati i dati deve comparire una finestra di conferma
#     print('Risultati inseriti correttamente')

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


# Radiobutton per scelta gioco
    # gioco = IntVar()
    # r1_1 = Radiobutton(finestra, text="MotoGP", variable=gioco, value=1, command=stampa)
    # r1_1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    # r1_2 = Radiobutton(finestra, text="F1", variable=gioco, value=2, command=stampa)
    # r1_2.grid(row=0, column=1, padx=5, pady=5, sticky="w")


    # Radiobutton per scelta categoria
    # categoria = IntVar()
    # r2_1 = Radiobutton(finestra, text="PC", variable=categoria, value=1, command=stampa)
    # r2_1.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    # r2_2 = Radiobutton(finestra, text="Play Station - MotoGP", variable=categoria, value=2, command=stampa)
    # r2_2.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    # r2_3 = Radiobutton(finestra, text="Play Station - Moto2", variable=categoria, value=3, command=stampa)
    # r2_3.grid(row=1, column=2, padx=5, pady=5, sticky="w")
    # Radiobutton per scelta stagione
