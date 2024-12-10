
# Daten importieren mit pandas
import pandas as pd

# Importiere Excel-Datei (Block 4, 7, 9)

# Parameter ist der Pfad zur Datei; zurückgegeben wird ein DataFrame mit den Daten der Datei
def importiere_excel_datei(dateipfad):
    daten = pd.read_excel(dateipfad)
    return daten


# Importiere csv-Datei (Block 4)

# Parameter ist der Pfad zur Datei; zurückgegeben wird ein DataFrame mit den Daten der Datei
def importiere_csv_datei(dateipfad):
    daten = pd.read_csv(dateipfad)
    return daten


# Importieren und Zusammenführen von Excel-Dateien aus einem Ordner (Block 9)
import os

def importiere_und_zusammenfuehren_excel_dateien(ordner_pfad):
    alle_daten = []  # Liste für die DataFrames der Excel-Dateien

    # Durch alle Dateien im Ordner iterieren
    for datei_name in os.listdir(ordner_pfad):
        # Der Pfad zur Excel-Datei
        datei_pfad = os.path.join(ordner_pfad, datei_name)

        # Excel-Datei importieren
        daten = importiere_excel_datei(datei_pfad)

        # DataFrame in die Liste der DataFrames einfügen
        alle_daten.append(daten)

    # Alle DataFrames zusammenführen
    kombinierte_daten = pd.concat(alle_daten, ignore_index=True)

    return kombinierte_daten