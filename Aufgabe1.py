# Block 4: Einarbeitung in Knime – Iris Flower Dataset

# Teil 1: Kombination der beiden Datensätze (Insgesamt 100 Datenreihen in 5 Spalten)

# Teil 1.1: Daten einlesen mit pandas
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


# Teil 1.3: Tabellen kombinieren, also untereinader schreiben
#kombinierte_tabelle = pd.concat([Tabelle1, Tabelle2], ignore_index=True)
kombinierte_tabelle = pd.concat([Tabelle1, Tabelle2], ignore_index=True)

# Ergebnis anzeigen
print("Teil 1.3 kombinierte Tabelle")
print(kombinierte_tabelle)

# Prüfen, ob alle Werte in den angegebenen Spalten Zahlenwerte sind - IST DAS HIER NÖTIG?
spalten = ["sepal length", "sepal width", "petal length", "petal width"]
sind_alle_zahlen = kombinierte_tabelle[spalten].apply(
    lambda col: col.map(lambda wert: isinstance(wert, (int, float))).all()
).all()
if sind_alle_zahlen:
    print("Alle Werte in den angegebenen Spalten sind Zahlen.")
else:
    print("Es gibt nicht-numerische Werte in den angegebenen Spalten.")



# Teil 2: Visualisierung der Klassifikation (3 verschiedene Spezies/Arten der Schwertlilien)

# Scatterplot erstellen mit matplotlib
import matplotlib.pyplot as plt

# Farbliche Unterscheidung der "Art" mit seaborn
import seaborn as sns

# Scatterplot erstellen zu Sepal Länge und Weite, Farben nach "Art"
plt.figure(figsize=(10, 6))     # Legt die Größe des Diagramms fest
sns.scatterplot(
data=kombinierte_tabelle,
x="sepal length",           # X-Achse: Sepal Length
y="sepal width",            # Y-Achse: Sepal Width
hue="Art",                  # Farbliche Trennung nach Arten
style="Art",                # Punktform für jede Art
palette="Set2"              # Farbpalette
)

# Titel und Achsenbeschriftung hinzufügen
plt.title("Sepal Length vs. Sepal Width nach Arten")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

# Plot anzeigen
plt.show()

# Scatterplot erstellen zu Petal Länge und Weite, Farben nach "Art"
plt.figure(figsize=(10, 6))     # Legt die Größe des Diagramms fest
sns.scatterplot(
data=kombinierte_tabelle,
x="petal length",           # X-Achse: Sepal Length
y="petal width",            # Y-Achse: Sepal Width
hue="Art",                  # Farbliche Trennung nach Arten
style="Art",                # Punktform für jede Art
palette="Set2"              # Farbpalette
)

# Titel und Achsenbeschriftung hinzufügen
plt.title("Petal Length vs. Petal Width nach Arten")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

# Plot anzeigen
plt.show()


# 3D Scatterplot mit Sepal Länge, Sepal Weite und Petal Länge
x = kombinierte_tabelle["sepal length"]  # x-Achse
y = kombinierte_tabelle["sepal width"]   # y-Achse
z = kombinierte_tabelle["petal length"]  # z-Achse
kategorie = kombinierte_tabelle["Art"]   # 4. Dimension (kategorische Variable)

# Umwandlung der kategorialen Daten (Strings) in numerische Werte (Index)
# keine gute Lösung, da Kategorie dann als Scala!
kategorie_num = pd.factorize(kategorie)[0]  # Wandelt die Kategorien in Indizes um

# 3D-Plot vorbereiten
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 3D-Scatterplot erstellen mit Farbzuweisung basierend auf der Kategorie
scatter = ax.scatter(x, y, z, c=kategorie_num, cmap='viridis', s=50)  # c=kategorie_num für die Farbkodierung

# Achsenbeschriftung hinzufügen
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')

# Farbskala hinzufügen
fig.colorbar(scatter, label="Species (as Category)")

# Titel hinzufügen
plt.title('3D Scatterplot mit Kategorien (farblich codiert)')

# Plot anzeigen
plt.show()
