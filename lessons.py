lessons = [
    {
        "id": 1,
        "title": "Hallo Welt!",
        "explanation": """
In Python kannst du Text auf dem Bildschirm ausgeben mit dem Befehl `print()`.

**Beispiel:**
```python
print("Hallo Welt!")
```

Das gibt den Text `Hallo Welt!` aus. Der Text muss in Anführungszeichen stehen.
        """,
        "task": 'Schreib einen print()-Befehl der genau "Hallo Welt!" ausgibt.',
        "starter_code": '# Schreib deinen Code hier\n',
        "check": {
            "type": "output",
            "expected": "Hallo Welt!"
        }
    },
    {
        "id": 2,
        "title": "Variablen",
        "explanation": """
Eine **Variable** ist wie eine Schublade, in der du Werte speichern kannst.

**Beispiel:**
```python
name = "Max"
alter = 25
print(name)
print(alter)
```

Du kannst Zahlen und Text speichern. Text kommt in Anführungszeichen, Zahlen nicht.
        """,
        "task": 'Erstelle eine Variable namens `name` mit deinem Namen und gib sie mit print() aus.',
        "starter_code": '# Erstelle eine Variable und gib sie aus\n',
        "check": {
            "type": "has_variable",
            "variable": "name"
        }
    },
    {
        "id": 3,
        "title": "Rechnen mit Python",
        "explanation": """
Python kann wie ein Taschenrechner benutzt werden!

**Operatoren:**
- `+` Addition
- `-` Subtraktion
- `*` Multiplikation
- `/` Division

**Beispiel:**
```python
ergebnis = 10 + 5
print(ergebnis)  # gibt 15 aus
```
        """,
        "task": "Berechne 7 mal 8 und gib das Ergebnis aus. Das Ergebnis muss 56 sein.",
        "starter_code": '# Rechne 7 * 8 und gib das Ergebnis aus\n',
        "check": {
            "type": "output",
            "expected": "56"
        }
    },
    {
        "id": 4,
        "title": "if / else – Entscheidungen",
        "explanation": """
Mit `if` und `else` kann dein Programm Entscheidungen treffen.

**Beispiel:**
```python
alter = 18

if alter >= 18:
    print("Du bist volljährig!")
else:
    print("Du bist minderjährig.")
```

**Wichtig:** Die Zeile nach `if` muss eingerückt sein (4 Leerzeichen oder Tab).
        """,
        "task": 'Erstelle eine Variable `zahl = 10`. Wenn sie größer als 5 ist, gib "Groß" aus, sonst "Klein".',
        "starter_code": 'zahl = 10\n# Schreib dein if/else hier\n',
        "check": {
            "type": "output",
            "expected": "Groß"
        }
    },
    {
        "id": 5,
        "title": "Schleifen – for",
        "explanation": """
Mit einer `for`-Schleife kannst du Code mehrmals wiederholen.

**Beispiel:**
```python
for i in range(5):
    print(i)
```

Das gibt die Zahlen 0, 1, 2, 3, 4 aus. `range(5)` erzeugt eine Folge von 0 bis 4.
        """,
        "task": "Schreib eine for-Schleife die die Zahlen 1 bis 5 ausgibt (also 1, 2, 3, 4, 5).",
        "starter_code": '# Schreib deine for-Schleife hier\n',
        "check": {
            "type": "output_contains",
            "expected": ["1", "2", "3", "4", "5"]
        }
    },
    {
        "id": 6,
        "title": "Funktionen",
        "explanation": """
Eine **Funktion** ist ein wiederverwendbarer Code-Block.

**Beispiel:**
```python
def begruesse(name):
    print("Hallo, " + name + "!")

begruesse("Anna")
begruesse("Max")
```

`def` bedeutet "definiere eine Funktion". Du rufst sie dann mit ihrem Namen auf.
        """,
        "task": 'Schreibe eine Funktion namens `verdopple` die eine Zahl als Parameter nimmt und das Doppelte ausgibt. Rufe sie mit der Zahl 7 auf (Ergebnis: 14).',
        "starter_code": '# Definiere die Funktion verdopple\n\n# Rufe sie mit 7 auf\n',
        "check": {
            "type": "output",
            "expected": "14"
        }
    },
    {
        "id": 7,
        "title": "Listen",
        "explanation": """
Eine **Liste** speichert mehrere Werte auf einmal.

**Beispiel:**
```python
früchte = ["Apfel", "Banane", "Kirsche"]
print(früchte[0])  # gibt "Apfel" aus (Zählung beginnt bei 0!)
print(len(früchte))  # gibt 3 aus (Anzahl der Elemente)
```

Du kannst mit einer `for`-Schleife durch eine Liste gehen:
```python
for frucht in früchte:
    print(frucht)
```
        """,
        "task": 'Erstelle eine Liste namens `zahlen` mit den Werten [3, 7, 2, 9, 1] und gib die Summe aller Zahlen aus (Tipp: benutze `sum(zahlen)`).',
        "starter_code": '# Erstelle die Liste und berechne die Summe\n',
        "check": {
            "type": "output",
            "expected": "22"
        }
    },
    {
        "id": 8,
        "title": "String-Methoden",
        "explanation": """
Strings (Text) haben nützliche eingebaute Methoden:

```python
text = "hallo welt"
print(text.upper())      # HALLO WELT
print(text.capitalize()) # Hallo welt
print(text.replace("welt", "python"))  # hallo python
print(len(text))         # 10
```
        """,
        "task": 'Erstelle eine Variable `satz = "python ist super"` und gib ihn komplett in Großbuchstaben aus.',
        "starter_code": 'satz = "python ist super"\n# Gib den Satz in Großbuchstaben aus\n',
        "check": {
            "type": "output",
            "expected": "PYTHON IST SUPER"
        }
    },
]
