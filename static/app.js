let lessons = [];
let currentLesson = null;
let completedLessons = JSON.parse(localStorage.getItem("completed") || "[]");
let starterCode = "";
let editor;

// CodeMirror Editor initialisieren
window.addEventListener("DOMContentLoaded", () => {
    editor = CodeMirror.fromTextArea(document.getElementById("code-editor"), {
        mode: "python",
        theme: "dracula",
        lineNumbers: true,
        indentUnit: 4,
        tabSize: 4,
        indentWithTabs: false,
        lineWrapping: true,
        extraKeys: {
            "Tab": (cm) => cm.replaceSelection("    ")
        }
    });

    loadLessons();
});

async function loadLessons() {
    const res = await fetch("/api/lessons");
    lessons = await res.json();
    renderLessonList();
    loadLesson(1);
}

function renderLessonList() {
    const list = document.getElementById("lesson-list");
    list.innerHTML = "";
    lessons.forEach(l => {
        const done = completedLessons.includes(l.id);
        const div = document.createElement("div");
        div.className = `lesson-item ${done ? "done" : ""} ${currentLesson?.id === l.id ? "active" : ""}`;
        div.innerHTML = `<span class="check-icon">${done ? "✅" : "○"}</span> Lektion ${l.id}: ${l.title}`;
        div.onclick = () => loadLesson(l.id);
        list.appendChild(div);
    });
    updateProgress();
}

function updateProgress() {
    const total = lessons.length;
    const done = completedLessons.length;
    document.getElementById("progress-text").textContent = `${done} / ${total}`;
    const pct = total > 0 ? (done / total) * 100 : 0;
    document.getElementById("progress-fill").style.width = pct + "%";
}

async function loadLesson(id) {
    const res = await fetch(`/api/lesson/${id}`);
    currentLesson = await res.json();
    starterCode = currentLesson.starter_code;

    document.getElementById("lesson-number").textContent = `Lektion ${currentLesson.id}`;
    document.getElementById("lesson-title").textContent = currentLesson.title;
    document.getElementById("explanation").innerHTML = marked.parse(currentLesson.explanation);
    document.getElementById("task-text").innerHTML = marked.parseInline(currentLesson.task);

    editor.setValue(starterCode);
    editor.refresh();

    clearOutput();
    hideFeedback();
    renderLessonList();

    // Nav Buttons
    document.getElementById("btn-prev").disabled = id <= 1;
    document.getElementById("btn-next").disabled = id >= lessons.length;

    // Scroll to top
    document.querySelector(".content").scrollTop = 0;
}

function resetCode() {
    editor.setValue(starterCode);
    clearOutput();
    hideFeedback();
}

async function runCode() {
    const code = editor.getValue();
    const outputEl = document.getElementById("output");
    outputEl.textContent = "Läuft...";

    const res = await fetch("/api/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ lesson_id: currentLesson.id, code })
    });
    const data = await res.json();

    if (data.error) {
        outputEl.style.color = "#f87171";
        outputEl.textContent = "Fehler:\n" + data.error;
    } else {
        outputEl.style.color = "#4ade80";
        outputEl.textContent = data.output || "(keine Ausgabe)";
    }
}

async function checkCode() {
    const code = editor.getValue();
    const res = await fetch("/api/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ lesson_id: currentLesson.id, code })
    });
    const data = await res.json();

    showFeedback(data.correct, data.feedback);

    if (data.correct && !completedLessons.includes(currentLesson.id)) {
        completedLessons.push(currentLesson.id);
        localStorage.setItem("completed", JSON.stringify(completedLessons));
        renderLessonList();

        // Auto-weiter nach 1.5s
        setTimeout(() => {
            if (currentLesson.id < lessons.length) {
                loadLesson(currentLesson.id + 1);
            }
        }, 1500);
    }
}

function showFeedback(correct, text) {
    const box = document.getElementById("feedback-box");
    box.style.display = "block";
    box.className = "feedback-box " + (correct ? "correct" : "wrong");
    box.textContent = (correct ? "🎉 " : "❌ ") + text;
}

function hideFeedback() {
    const box = document.getElementById("feedback-box");
    box.style.display = "none";
}

function clearOutput() {
    const el = document.getElementById("output");
    el.textContent = "Hier erscheint deine Ausgabe...";
    el.style.color = "#4ade80";
}

function prevLesson() {
    if (currentLesson && currentLesson.id > 1) loadLesson(currentLesson.id - 1);
}

function nextLesson() {
    if (currentLesson && currentLesson.id < lessons.length) loadLesson(currentLesson.id + 1);
}
