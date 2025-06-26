import os

def create_project_structure():
    # Setzt den Projektordnernamen
    project_name = "chromeExt"
    print(f"Erstelle Projektordner: {project_name}")
    
    # Erstellt den Projektordner
    os.makedirs(project_name, exist_ok=True)
    
    # Wechselt in den Projektordner
    os.chdir(project_name)
    
    # Erstellt die Dateien mit ihren Inhalten
    files = {
        "manifest.json": """{
    "manifest_version": 3,
    "name": "Chrome Extension Skeleton",
    "version": "1.0",
    "description": "Eine einfache Chrome Extension Skeleton.",
    "permissions": [],
    "background": {
        "service_worker": "background.js"
    },
    "action": {
        "default_popup": "popup.html",
        "default_icon": "icon.png"
    },
    "icons": {
        "16": "icon.png",
        "48": "icon.png",
        "128": "icon.png"
    }
}""",
        "background.js": """console.log("Hintergrund-Skript läuft!");""",
        "popup.html": """<!DOCTYPE html>
<html>
<head>
    <title>Popup</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 10px; }
    </style>
</head>
<body>
    <h1>Chrome Extension Skeleton</h1>
    <button id="clickMe">Click Me</button>
    <script src="popup.js"></script>
</body>
</html>""",
        "popup.js": """document.getElementById("clickMe").addEventListener("click", () => {
    alert("Button wurde geklickt!");
});""",
        "icon.png": ""  # Platzhalter für das Icon
    }
    
    # Erstellt die Dateien und schreibt die Inhalte hinein
    for filename, content in files.items():
        with open(filename, "w") as file:
            file.write(content)
        print(f"Erstellt: {filename}")
    
    print("Die Chrome Extension Skeleton wurde erfolgreich initialisiert!")

if __name__ == "__main__":
    create_project_structure()