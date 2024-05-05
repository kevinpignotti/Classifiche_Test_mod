import sqlite3
import pandas as pd

# Funzione per inserire i dati nel database evitando duplicati
def inserisci_dati(nome_tabella, dataframe):
    colonne_chiave = []
    if nome_tabella == 'Piloti':
        colonne_chiave = ['ID_Pilota']
    elif nome_tabella == 'Gare':
        colonne_chiave = ['ID_Gara']
    elif nome_tabella == 'Risultati':
        colonne_chiave = ['ID_Risultato']
    elif nome_tabella == 'Team':
        colonne_chiave = ['ID_Squadra']

    # Connessione al database SQLite
    conn = sqlite3.connect('formula1.db')
    cursor = conn.cursor()

    for _, row in dataframe.iterrows():
        # Controlla se le colonne chiave sono già presenti nella tabella
        condizioni = ' AND '.join([f"{colonna} = ?" for colonna in colonne_chiave])
        cursor.execute(f"SELECT * FROM {nome_tabella} WHERE {condizioni}", tuple(row[colonna] for colonna in colonne_chiave))
        existing_row = cursor.fetchone()
        if existing_row is None:
            # Inserisce la riga solo se non è già presente
            cursor.execute(f"INSERT INTO {nome_tabella} VALUES ({','.join(['?']*len(row))})", tuple(row))
            print(f"Dati inseriti nella tabella {nome_tabella}")
    conn.commit()

    # Chiudere la connessione al database
    conn.close()

# Lettura dei file CSV e inserimento dei dati nel database
def main():
    gare_df = pd.read_csv('gare.csv')
    inserisci_dati('Gare', gare_df)

    team_df = pd.read_csv('team.csv')
    inserisci_dati('Team', team_df)

    piloti_df = pd.read_csv('piloti.csv')
    inserisci_dati('Piloti', piloti_df)

    risultati_df = pd.read_csv('risultati.csv')
    inserisci_dati('Risultati', risultati_df)

if __name__ == "__main__":
    main()

