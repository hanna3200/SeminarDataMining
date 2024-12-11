# Block 9: Zusammenführen von Daten - Informationssammlung

import datenimport
import pandas as pd


# Teil 1: Produktionsdaten Dezember
# Excel-Datei der Produktionsdaten von Dezember Tag 1 importieren
dateipfad_excel = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/01_Block5_Produktionstag 1/Dezember_Produktionstag1.xlsx"
Dezember_Tag1 = datenimport.importiere_excel_datei(dateipfad_excel)

# Excel-Datei der Produktionsdaten von Dezember ohne Tag 1 importieren
dateipfad_excel = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/02_Block9_Zusammenführung/Dezember_ohne_Tag1.xlsx"
Dezember_ohneTag1 = datenimport.importiere_excel_datei(dateipfad_excel)

# Manuelle Fehlerbehebung im Datensatz "Dezember_ohneTag1": Ersetzen von 11 durch 1 in Spalte "Prüfresultat"
Dezember_ohneTag1['Prüfresultat'] = Dezember_ohneTag1['Prüfresultat'].replace(11, 1)

# Fehlerbehebung kontrollieren
einzigartige_werte = Dezember_ohneTag1['Prüfresultat'].unique()
print("Einzigartige Werte in der Spalte 'Prüfresultat' im Datensatz 'Dezember_ohneTag1':", einzigartige_werte)

# Datensätze von Dezember zusammenführen
Produktionsdaten_Dezember = pd.concat([Dezember_Tag1, Dezember_ohneTag1], ignore_index=True)

# Ergebnis anzeigen (es sollten 91447 Datenreihen sein)
print("Produktionsdaten_Dezember")
print(Produktionsdaten_Dezember)



# Teil 2: Produktionsdaten Januar
# Excel-Datei der Produktionsdaten von Januar importieren
dateipfad_excel = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/02_Block9_Zusammenführung/Januar.xlsx"
Produktionsdaten_Januar = datenimport.importiere_excel_datei(dateipfad_excel)

# Ergebnis anzeigen (es sollten 109479 Datenreihen sein)
print("Produktionsdaten_Januar")
print(Produktionsdaten_Januar)



# Teil 3: Produktionsdaten Februar

# Teil 3.1: Übertragungsunterbrechung korrigieren

# Ordnerpfad, in dem sich die Excel-Dateien von Februar (erste Teile) befinden
ordner_pfad = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/02_Block9_Zusammenführung/Februar/erste_Teile"

# Alle Excel-Dateien in diesem Ordner importieren und zusammenführen
kombinierte_daten_Februar_ersteTeile = datenimport.importiere_und_zusammenfuehren_excel_dateien(ordner_pfad)

# Ergebnis anzeigen (es sollten 99 Datenreihen sein)
print("Kombinierte Daten Februar erste Teile:")
print(kombinierte_daten_Februar_ersteTeile)



# Teil 3.2: Zeitstempel korrigieren

# Excel-Datei der restlichen Produktionsdaten von Februar importieren
dateipfad_excel = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/02_Block9_Zusammenführung/Februar/Februar_Rest.xlsx"
Produktionsdaten_Februar_Rest = datenimport.importiere_excel_datei(dateipfad_excel)

# Kombinieren der beiden Spalten "Datumsstempel" und "Uhrzeit"
Produktionsdaten_Februar_Rest['Zeitstempel'] = Produktionsdaten_Februar_Rest['Datumsstempel'].astype(str) + ' ' + Produktionsdaten_Februar_Rest['Uhrzeit'].astype(str)

# Löschen der ursprünglichen Spalten
Produktionsdaten_Februar_Rest.drop(['Datumsstempel', 'Uhrzeit'], axis=1, inplace=True)

# Ausgabe der ersten paar Zeilen des geänderten DataFrames
print(Produktionsdaten_Februar_Rest.head())



# Teil 3.3: Datensätze von Februar zusammenführen (unterschiedliche Reihenfolge der Spaltenüberschriften ist kein Problem)
Produktionsdaten_Februar = pd.concat([kombinierte_daten_Februar_ersteTeile, Produktionsdaten_Februar_Rest], ignore_index=True)

# Ergebnis anzeigen (es sollten 83863 Datenreihen sein)
print(Produktionsdaten_Februar)


# Teil 4: Produktionsdaten gesamt
# alle Datensätze zusammenführen
Produktionsdaten_gesamt= pd.concat([Produktionsdaten_Dezember, Produktionsdaten_Februar, Produktionsdaten_Januar], ignore_index=True)

# Ergebnis anzeigen (es sollten 284789 Datenreihen sein)
print(Produktionsdaten_gesamt)