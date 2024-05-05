import sqlite3


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
    print('Risultati inseriti correttamente')
