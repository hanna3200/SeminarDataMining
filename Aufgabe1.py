# Block 4: Einarbeitung in Knime – Iris Flower Dataset

# Teil 1: Kombination der beiden Datensätze (Insgesamt 100 Datenreihen in 5 Spalten)

#Teil 1.1: Daten einlesen
# Einlesen von Dateien funktioniert mit pandas
import pandas as pd

# Excel-Datei einlesen (am besten Dateien dort ablegen, wo Python-Arbeitsdatei abliegt)
# Tabelle1 = pd.read_excel("Dateipfad")
Tabelle1 = pd.read_excel("/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/00_Block4_Iris Flower DataSet/Iris_01.xlsx")

# Eingelesene Daten anzeigen lassen
print("Teil 1.1 Tabelle 1")
print (Tabelle1)

# csv-Datei einlesen (am besten Dateien dort ablegen, wo Python-Arbeitsdatei abliegt)
# Tabelle2 = pd.read_csv("Dateipfad")
Tabelle2 = pd.read_csv("/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/00_Block4_Iris Flower DataSet/Iris_02.csv")

# Eingelesene Daten anzeigen lassen
print("Teil 1.1 Tabelle 2")
print (Tabelle2)


# Teil 1.2: Spaltennamen angleichen
# Spaltenname 1 in Tabelle 1 anpassen
# Tabelle1.rename(columns={'AlteSpalte1': 'NeueSpalte', 'AlteSpalte2': 'AndereSpalte'}, inplace=True)
Tabelle1.rename(columns={'Sepal Länge': 'sepal length'}, inplace=True)

# Eingelesene Daten anzeigen lassen
print("Teil 1.2 Tabelle 1")
print (Tabelle1)
print("Teil 1.2 Tabelle 2")
print (Tabelle2)


#Teil 1.3: Tabellen kombinieren, also untereinader schreiben
#kombinierte_tabelle = pd.concat([Tabelle1, Tabelle2], ignore_index=True)
kombinierte_tabelle = pd.concat([Tabelle1, Tabelle2], ignore_index=True)

# Ergebnis anzeigen
print("Teil 1.3 kombinierte Tabelle")
print(kombinierte_tabelle)



# Teil 2: Visualisierung der Klassifikation (3 verschiedene Spezien der Schwertlilien)
