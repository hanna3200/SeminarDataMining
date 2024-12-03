# Block 5 und 6: Arbeit an den Produktionsdaten

# Block 7: Arbeitspaket 1 bearbeiten

# Block 7: Arbeitspaket 1.1 – Gesamtstatistik Prüfresultat

import pandas as pd
import matplotlib.pyplot as plt

# Excel-Datei einlesen
Produktionstag1 = pd.read_excel("/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/01_Block5_Produktionstag 1/Dezember_Produktionstag1.xlsx")

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
