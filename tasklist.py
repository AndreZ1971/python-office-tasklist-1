
tasklist = []

# Funktionen beginnen mit def
def add_task():
    task = input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: ")
    due_date = input("Bitte gib ein Fälligkeitsdatum ein (TT.MM.JJJJ) oder drücke Enter, um keins anzugeben: ")
    priority = input("Bitte gib die Priorität an (hoch, mittel, niedrig) oder drücke Enter für 'mittel': ")
    
    if not priority:
        priority = "mittel"
    
    task_entry = {
        "Aufgabe": task,
        "Fälligkeitsdatum": due_date,
        "Priorität": priority
    }
    tasklist.append(task_entry)
    print(f"Aufgabe '{task}' wurde der Liste hinzugefügt.")
