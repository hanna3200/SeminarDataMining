
# Block 10

import pandas as pd
import matplotlib.pyplot as plt
from Task_3 import Produktionsdaten_gesamt

#  Durchführen der gleichen Analysen wie in Task 2 und Task 8, lediglich mit dem neuen Datensatz

# Arbeitspaket 1 erneut bearbeiten

# Arbeitspaket 1.1 – Gesamtstatistik Prüfresultat

# Spaltenname anpassen
ergebnis = Produktionsdaten_gesamt['Prüfresultat']

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

# Arbeitspaket 1.2 – Prüfstandstatistik

# Gruppieren nach Prüfstand
gruppen = Produktionsdaten_gesamt.groupby('Prüfstand')

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
fehlercodes = Produktionsdaten_gesamt['Fehlercode']

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

# Arbeitspaket 2 erneut machen, diesmal erneut mit gesamtem Datenbestand

# Kopie des gesamten Datenbestands machen, mit der wir arbeiten
df_gesamt = Produktionsdaten_gesamt

# Taktzeit der Prüfstände für weitere Planung ermitteln

# Schritt 1: Wandle den Zeitstempel von einem String in eine Recheneinheit
df_gesamt["Zeitstempel"] = pd.to_datetime(df_gesamt["Zeitstempel"])

# Schritt 1: Sortiere die Daten nach der Spalte "Prüfstand" und danach nach der Spalte "Zeitstempel"
df_gesamt_sortiert = df_gesamt.sort_values(by=["Prüfstand", "Zeitstempel"], ascending=[True, True])

# Daten anzeigen lassen
df_gesamt_sortiert

# Jetzt möchten wir die Zeitdifferenz zwischen den jeweiligen Zeilen berechnen

# Zeitdifferenzen berechnen
df_gesamt_sortiert["Zeitdifferenz"]= df_gesamt_sortiert["Zeitstempel"].diff()

# Zeitdifferenzen in Sekunden angeben
df_gesamt_sortiert["Zeitdifferenz_in_Sekunden"]= df_gesamt_sortiert["Zeitdifferenz"].dt.total_seconds()


# Daten gruppieren nach der Spalte "Prüfstand"
gruppen = df_gesamt_sortiert.groupby("Prüfstand")

# Iteration über die Gruppen und Anzeige der Zeilen
for pruefstand, gruppe in gruppen:
    print(f"Gruppe: {pruefstand}")
    print(gruppe)
    print("-" * 40)  # Trennt jede Gruppe


# Alle Zeitdifferenzen plotten (für jede Gruppe separat) und dabei zunächst die erste Zeile rausschmeißen (da kein gültiger Wert für Zeitdifferenz)

for pruefstand, gruppe in gruppen:
    # Entferne die erste Zeile aus der Gruppe
    gruppe = gruppe.iloc[1:].reset_index(drop=True)

    # Plotten
    plt.figure(figsize=(8,4))
    plt.plot(gruppe.index, gruppe["Zeitdifferenz_in_Sekunden"], marker="o", label=f"Prüfstand {pruefstand}")
    plt.title(f"Zeitdifferenzen für Prüfstand {pruefstand}")
    plt.xlabel("Index")
    plt.ylabel("Zeitdifferenz (Sekunden)")
    plt.grid(True)
    plt.legend()
    plt.show()


# Berechnung der arithmetischen Mittelwerte der Zeitdifferenzen der einzelnen Gruppen
mittelwerte = gruppen.apply(lambda x: x.iloc[1:]["Zeitdifferenz_in_Sekunden"].mean(), include_groups=False)

# Mittelwerte plotten
plt.figure(figsize=(8, 5))
mittelwerte.plot(kind="bar", color="lightgreen", edgecolor="black")

# Diagramm formatieren
plt.title("Arithmetisches Mittel der Zeitdifferenzen pro Prüfstand", fontsize=14)
plt.xlabel("Prüfstand", fontsize=12)
plt.ylabel("Arithmetisches Mittel der Zeitdifferenz (Sekunden)", fontsize=12)
plt.xticks(rotation=0)  # x-Achsen-Beschriftung horizontal halten
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Werte über den Balken anzeigen
for i, value in enumerate(mittelwerte):
    plt.text(i, value + 1, f"{value:.1f}", ha='center', fontsize=10, color="black")

plt.show()

# Berechnung der Mediane der Zeitdifferenzen der einzelnen Gruppen
mediane = gruppen.apply(lambda x: x.iloc[1:]["Zeitdifferenz_in_Sekunden"].median(), include_groups=False) # Gruppierungsspalten werden in der Berechnung nicht berücksichtigt

# Mediane plotten
plt.figure(figsize=(8, 5))
mediane.plot(kind="bar", color="skyblue", edgecolor="black")

# Diagramm formatieren
plt.title("Median der Zeitdifferenzen pro Prüfstand", fontsize=14)
plt.xlabel("Prüfstand", fontsize=12)
plt.ylabel("Median der Zeitdifferenz (Sekunden)", fontsize=12)
plt.xticks(rotation=0)  # x-Achsen-Beschriftung horizontal halten
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Werte über den Balken anzeigen
for i, value in enumerate(mediane):
    plt.text(i, value + 1, f"{value:.1f}", ha='center', fontsize=10, color="black")

plt.show()

