import sqlite3

# Connessione al database SQLite
conn = sqlite3.connect('formula1.db')
cursor = conn.cursor()

# Creazione della tabella "Gare"
cursor.execute('''CREATE TABLE Gare (
                ID_Gara INTEGER PRIMARY KEY,
                Circuito TEXT,
                Data DATE,
                Paese TEXT,
                NumeroGiri INTEGER
                )''')

# Creazione della tabella "Team"
cursor.execute('''CREATE TABLE Team (
                ID_Squadra INTEGER PRIMARY KEY,
                NomeSquadra TEXT,
                Nazionalita TEXT
                )''')

# Creazione della tabella "Piloti"
cursor.execute('''CREATE TABLE Piloti (
                ID_Pilota INTEGER PRIMARY KEY,
                Nome TEXT,
                Cognome TEXT,
                Nazionalita TEXT,
                DataNascita DATE,
                ID_Squadra INTEGER,
                FOREIGN KEY (ID_Squadra) REFERENCES Team(ID_Squadra)
                )''')

# Creazione della tabella "Punti"
cursor.execute('''CREATE TABLE Punti (
                Posizione INTEGER PRIMARY KEY,
                Punti INTEGER
                )''')

# Inserimento dei dati nella tabella "Punti"
punti_data = [(1, 25), (2, 18), (3, 15), (4, 12), (5, 10), (6, 8), (7, 6), (8, 4), (9, 2), (10, 1)]
cursor.executemany("INSERT INTO Punti VALUES (?, ?)", punti_data)

# Creazione della tabella "Risultati"
cursor.execute('''CREATE TABLE Risultati (
                ID_Risultato INTEGER PRIMARY KEY,
                ID_Gara INTEGER,
                ID_Pilota INTEGER,
                Posizione INTEGER,
                MigliorGiro TEXT,
                Scuderia_attuale INTEGER,
                FOREIGN KEY (ID_Gara) REFERENCES Gare(ID_Gara),
                FOREIGN KEY (ID_Pilota) REFERENCES Piloti(ID_Pilota)
                )''')

# Salvataggio dei cambiamenti e chiusura della connessione
conn.commit()
conn.close()
