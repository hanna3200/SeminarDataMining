# Block 4: Einarbeitung in Knime – Iris Flower Dataset

# Teil 1: Kombination der beiden Datensätze (Insgesamt 100 Datenreihen in 5 Spalten)

# Teil 1.1: Daten importieren aus File "datenimport"
import datenimport
import pandas as pd

# Excel-Datei importieren
dateipfad_excel = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/00_Block4_Iris Flower DataSet/Iris_01.xlsx"
Tabelle1 = datenimport.importiere_excel_datei(dateipfad_excel)

# Eingelesene Daten anzeigen lassen
print("Teil 1.1 Tabelle 1")
print (Tabelle1)


# csv-Datei importieren
dateipfad_csv = "/Users/hannaweinmann/PycharmProjects/SeminarDataMining/Produktionsdaten/DatenTag1/00_Block4_Iris Flower DataSet/Iris_02.csv"
Tabelle2 = datenimport.importiere_csv_datei(dateipfad_csv)

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

# Teil 2.1 Scatterplot erstellen mit matplotlib
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
palette={'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'},  # Farben für jede Kategorie
)

# Titel und Achsenbeschriftung hinzufügen
plt.title("Sepal Length vs. Sepal Width nach Arten")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

# Plot anzeigen
plt.show()


# Teil 2.2 Scatterplot erstellen zu Petal Länge und Weite, Farben nach "Art"
plt.figure(figsize=(10, 6))     # Legt die Größe des Diagramms fest
sns.scatterplot(
data=kombinierte_tabelle,
x="petal length",           # X-Achse: Sepal Length
y="petal width",            # Y-Achse: Sepal Width
hue="Art",                  # Farbliche Trennung nach Arten
style="Art",                # Punktform für jede Art
palette={'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'},  # Farben für jede Kategorie
)

# Titel und Achsenbeschriftung hinzufügen
plt.title("Petal Length vs. Petal Width nach Arten")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

# Plot anzeigen
plt.show()



# Teil 2.3 Scatter Matrix mit allen möglichen Scatter Plots
import seaborn as sns
import matplotlib.pyplot as plt

# Scatter-Matrix mit Scatterplots auf der Diagonale
scatter_matrix = sns.pairplot(
    kombinierte_tabelle,        # Die kombinierte Tabelle
    hue="Art",                  # Farbliche Unterscheidung nach "Art"
    palette={'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'},  # Farben für jede Kategorie
    diag_kind="auto",           # Scatterplots auch auf der Diagonale
    markers=["o", "s", "D"],    # Punktmarker für jede Kategorie
    plot_kws={'s': 50}          # Anpassung der Punktgröße im Scatterplot
)

# Titel hinzufügen
scatter_matrix.fig.suptitle("Scatter-Matrix: Paarweise Darstellung der Merkmale", y=1.02)

# Größe des Plots anpassen - bei Bedarf
scatter_matrix.fig.set_size_inches(12, 7)  # Breite und Höhe in Zoll festlegen

# Plot anzeigen
plt.show()



# Teil 2.4 3D Scatterplot mit Sepal Länge, Sepal Weite und Petal Länge
import matplotlib.pyplot as plt
# Farben für die Kategorien definieren
farbe_mapping = {'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'}

# Daten vorbereiten
x = kombinierte_tabelle["sepal length"]  # x-Achse
y = kombinierte_tabelle["sepal width"]   # y-Achse
z = kombinierte_tabelle["petal length"]  # z-Achse
kategorie = kombinierte_tabelle["Art"]   # Kategorische Variable

# Farben zuordnen basierend auf der Kategorie
farben = kategorie.map(farbe_mapping)

# 3D-Plot vorbereiten
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 3D-Scatterplot erstellen
scatter = ax.scatter(x, y, z, c=farben, s=50)  # 'c=farben' sorgt für Farbcodierung

# Achsenbeschriftung hinzufügen
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')

# Titel hinzufügen
plt.title('3D Scatterplot mit Kategorien (farblich codiert)')

# Legende hinzufügen
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label)
           for label, color in farbe_mapping.items()]
ax.legend(handles=handles, title="Art", loc='upper left')

# Plot anzeigen
plt.show()
