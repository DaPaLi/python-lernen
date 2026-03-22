# 🐍 Python Lernen

Ein interaktives Python-Lernprogramm direkt im Browser — mit echtem Code-Editor, automatischer Prüfung und Fortschrittsanzeige.

---

## ✨ Features

- 📖 **8 Lektionen** — von „Hallo Welt" bis zu Funktionen und Listen
- 💻 **Echter Code-Editor** mit Python-Syntax-Highlighting (CodeMirror)
- ▶️ **Code ausführen** — siehst sofort die Ausgabe deines Codes
- ✅ **Automatische Prüfung** — das Programm prüft ob deine Lösung richtig ist
- 🏆 **Fortschrittsanzeige** — wird lokal gespeichert, bleibt auch nach Neustart
- 🎉 **Auto-Weiter** — nach jeder richtigen Lösung geht es automatisch zur nächsten Lektion

---

## 📚 Lektionen

| # | Thema |
|---|-------|
| 1 | Hallo Welt! – `print()` |
| 2 | Variablen |
| 3 | Rechnen mit Python |
| 4 | if / else – Entscheidungen |
| 5 | Schleifen – `for` |
| 6 | Funktionen |
| 7 | Listen |
| 8 | String-Methoden |

---

## 🚀 Installation & Start

### Voraussetzungen
- Python 3.10 oder neuer → [python.org](https://python.org)

### 1. Repository klonen
```bash
git clone https://github.com/DaPaLi/python-lernen.git
cd python-lernen
```

### 2. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 3. Starten
```bash
python main.py
```

### 4. Im Browser öffnen
```
http://localhost:8000
```

---

## 🛠️ Tech Stack

| Bereich | Technologie |
|---------|-------------|
| Backend | Python + FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Code-Editor | CodeMirror 5 |
| Markdown | marked.js |

---

## 📁 Projektstruktur

```
python-lernen/
├── main.py          # FastAPI Backend (Server + Code-Ausführung)
├── lessons.py       # Alle Lektionen & Aufgaben
├── requirements.txt # Python-Abhängigkeiten
└── static/
    ├── index.html   # Benutzeroberfläche
    ├── style.css    # Design
    └── app.js       # Frontend-Logik
```

---

## 🔒 Sicherheit

Der Code wird in einem separaten Subprocess mit einem **5-Sekunden-Timeout** ausgeführt. Für Produktionseinsatz empfiehlt sich eine stärkere Sandbox (z.B. Docker).

---

## 📄 Lizenz

MIT License — frei verwendbar, veränderbar und weitergegeben.
