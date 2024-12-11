
# Import notwendiger Bibliotheken
import pandas as pd
import matplotlib.pyplot as plt

# Excel-File für Produktionstag 1 einlesen
excel_file_Dezember_Produktionstag_1 = r"C:\Users\fabia\OneDrive\Documents\Studium\KIT WING Master\Data Mining in der Produktion\01_Block5_Produktionstag 1\Dezember_Produktionstag1.xlsx"
df_Produktionstag_1 = pd.read_excel(excel_file_Dezember_Produktionstag_1)
df_Produktionstag_1.head()

# Block 8 Arbeitspaket 2

# Taktzeit der Prüfstände für weitere Planung ermitteln

# Schritt 1: Wandle den Zeitstempel von einem String in eine Recheneinheit
df_Produktionstag_1["Zeitstempel"] = pd.to_datetime(df_Produktionstag_1["Zeitstempel"])

# Schritt 1: Sortiere die Daten nach der Spalte "Prüfstand" und danach nach der Spalte "Zeitstempel"
df_Produktionstag_1_sortiert = df_Produktionstag_1.sort_values(by=["Prüfstand", "Zeitstempel"], ascending=[True, True])

# Daten anzeigen lassen
df_Produktionstag_1_sortiert

# Jetzt möchten wir die Zeitdifferenz zwischen den jeweiligen Zeilen berechnen

# Zeitdifferenzen berechnen
df_Produktionstag_1_sortiert["Zeitdifferenz"]= df_Produktionstag_1_sortiert["Zeitstempel"].diff()

# Zeitdifferenzen in Sekunden angeben
df_Produktionstag_1_sortiert["Zeitdifferenz_in_Sekunden"]= df_Produktionstag_1_sortiert["Zeitdifferenz"].dt.total_seconds()

df_Produktionstag_1_sortiert

# Daten gruppieren nach der Spalte "Prüfstand"
gruppen = df_Produktionstag_1_sortiert.groupby("Prüfstand")

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
