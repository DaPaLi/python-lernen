from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import subprocess
import sys
import os
import json

from lessons import lessons

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return FileResponse("static/index.html")


@app.get("/api/lessons")
def get_lessons():
    return [{"id": l["id"], "title": l["title"]} for l in lessons]


@app.get("/api/lesson/{lesson_id}")
def get_lesson(lesson_id: int):
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            return {
                "id": lesson["id"],
                "title": lesson["title"],
                "explanation": lesson["explanation"],
                "task": lesson["task"],
                "starter_code": lesson["starter_code"],
            }
    return {"error": "Lektion nicht gefunden"}


class CodeSubmit(BaseModel):
    lesson_id: int
    code: str


@app.post("/api/run")
def run_code(data: CodeSubmit):
    # Code sicher ausführen mit Timeout
    try:
        result = subprocess.run(
            [sys.executable, "-c", data.code],
            capture_output=True,
            text=True,
            timeout=5,
            encoding="utf-8"
        )
        output = result.stdout.strip()
        error = result.stderr.strip()
    except subprocess.TimeoutExpired:
        return {"success": False, "output": "", "error": "Timeout: Dein Code hat zu lange gebraucht (max. 5 Sekunden)."}
    except Exception as e:
        return {"success": False, "output": "", "error": str(e)}

    if error:
        return {"success": False, "output": output, "error": error}

    return {"success": True, "output": output, "error": ""}


@app.post("/api/check")
def check_code(data: CodeSubmit):
    lesson = next((l for l in lessons if l["id"] == data.lesson_id), None)
    if not lesson:
        return {"correct": False, "feedback": "Lektion nicht gefunden."}

    # Code ausführen
    try:
        result = subprocess.run(
            [sys.executable, "-c", data.code],
            capture_output=True,
            text=True,
            timeout=5,
            encoding="utf-8"
        )
        output = result.stdout.strip()
        error = result.stderr.strip()
    except subprocess.TimeoutExpired:
        return {"correct": False, "feedback": "Timeout: Dein Code hat zu lange gebraucht."}
    except Exception as e:
        return {"correct": False, "feedback": f"Fehler: {str(e)}"}

    if error:
        return {"correct": False, "feedback": f"Fehler in deinem Code:\n{error}"}

    check = lesson["check"]

    if check["type"] == "output":
        if output == check["expected"]:
            return {"correct": True, "feedback": "Perfekt! Das ist richtig!"}
        else:
            return {
                "correct": False,
                "feedback": f'Nicht ganz. Deine Ausgabe: "{output}"\nErwartet: "{check["expected"]}"'
            }

    elif check["type"] == "output_contains":
        missing = [e for e in check["expected"] if e not in output]
        if not missing:
            return {"correct": True, "feedback": "Super gemacht!"}
        else:
            return {
                "correct": False,
                "feedback": f'Folgende Zahlen fehlen in der Ausgabe: {", ".join(missing)}'
            }

    elif check["type"] == "has_variable":
        var = check["variable"]
        if var in data.code:
            if output:
                return {"correct": True, "feedback": "Gut gemacht! Variable erstellt und ausgegeben."}
            else:
                return {"correct": False, "feedback": f'Variable `{var}` gefunden, aber nichts ausgegeben. Vergiss print() nicht!'}
        else:
            return {"correct": False, "feedback": f'Variable `{var}` nicht gefunden.'}

    return {"correct": False, "feedback": "Unbekannter Check-Typ."}


if __name__ == "__main__":
    import uvicorn
    print("Starte Python-Lernprogramm...")
    print("Öffne im Browser: http://localhost:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
