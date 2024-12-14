# Block 5 und 6: Arbeit an den Produktionsdaten

# Block 7: Arbeitspaket 1 bearbeiten

# Block 7: Arbeitspaket 1.1 – Gesamtstatistik Prüfresultat

import datenimport
import pandas as pd
import matplotlib.pyplot as plt

# Excel-Datei einlesen
dateipfad_excel = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/01_Block5_Produktionstag 1/Dezember_Produktionstag1.xlsx"
Produktionstag1 = datenimport.importiere_excel_datei(dateipfad_excel)

# Spaltenname anpassen
ergebnis = Produktionstag1['Prüfresultat']

# Zählen der Fehler (Prüfresultat ist 2) und Nicht-Fehler (Prüfresultat ist 1)
fehler_anzahl = ergebnis[ergebnis == 2].count()
keine_fehler_anzahl = ergebnis[ergebnis == 1].count()

# Gesamtzahl der geprüften Werte
gesamt_anzahl = len(ergebnis)

# Berechnung der Fehlerquote
fehler_quote = fehler_anzahl / gesamt_anzahl
keine_fehler_quote = 1 - fehler_quote

# Erstellen des Pie Charts
labels = ['Fehler (Prüfresultat ist 2)', 'Keine Fehler (Prüfresultat ist 1)']
sizes = [fehler_quote, keine_fehler_quote]
colors = ['red', 'green']
explode = (0.1, 0)  # Ein leichtes Herausheben des Anteils "Fehler"

# Plot erstellen
plt.figure(figsize=(10, 7)) # Schaubildgröße
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%.2f%%', startangle=140) # durch autopct lassen sich bsw. die Nachkommastellen anpassen
plt.title('Fehlerquote Prüfresultat Tag 1')
plt.axis('equal')  # Sicherstellen, dass der Kreis rund ist
plt.show()




# Block 7: Arbeitspaket 1.2 – Prüfstandstatistik

# Gruppieren nach Prüfstand
gruppen = Produktionstag1.groupby('Prüfstand')

# Initialisiere Listen für die Ergebnisse
pruefstand_liste = []
anzahl_gepruefter_teile = []
anzahl_fehler = []
fehler_anteil = []

# Durch die Gruppen iterieren und Berechnungen durchführen
for pruefstand, gruppe in gruppen:
    gesamt = len(gruppe)  # Anzahl geprüfter Teile
    fehler = gruppe[gruppe['Prüfresultat'] == 2].shape[0]  # Anzahl der Fehler
    fehlerquote = fehler / gesamt if gesamt > 0 else 0  # Anteil der Fehler

    # Ergebnisse speichern
    pruefstand_liste.append(pruefstand)
    anzahl_gepruefter_teile.append(gesamt)
    anzahl_fehler.append(fehler)
    fehler_anteil.append(fehlerquote)

# DataFrame für die Übersichtstabelle erstellen
uebersicht = pd.DataFrame({
    'Prüfstand': pruefstand_liste,
    'Anzahl geprüfter Teile': anzahl_gepruefter_teile,
    'Anzahl der Fehler': anzahl_fehler,
    'Anteil der Fehler (%)': [round(quote * 100, 2) for quote in fehler_anteil]  # Fehleranteil in Prozent
})

# Tabelle ausgeben
print(uebersicht)



# Block 7: Arbeitspaket 1.3 – größter Fehler

# Fehlercodes aus der Excel-Datei extrahieren
fehlercodes = Produktionstag1['Fehlercode']

# Herausfiltern von Eintrag "0", da dieser kein richtiger Fehlercode ist
fehlercodes = fehlercodes[fehlercodes != 0]

# Häufigkeiten der Fehlercodes zählen
fehlercode_counts = fehlercodes.value_counts()

# Prozentuale Häufigkeit berechnen
fehlercode_percent = fehlercode_counts / fehlercode_counts.sum() * 100

# Daten für das Diagramm vorbereiten
labels = [f"{code}" for code in fehlercode_counts.index]  # Nur den Fehlercode
sizes = fehlercode_counts
colors = plt.cm.tab10.colors  # Farben aus einer vordefinierten Farbpallette

# Erstellen der Labels, die die Anzahl und den Prozentsatz enthalten
def make_label(count, percent):
    return f'{count} ({percent:.2f}%)'

# Pie Chart erstellen
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct=lambda p: make_label(int(p * sum(sizes) / 100), p), startangle=140)
plt.title('Verteilung der Häufigkeiten der Fehlercodes')
plt.axis('equal')  # Sicherstellen, dass der Kreis rund ist
plt.show()
