
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


from datetime import datetime, timedelta


def show_tasklist():
    if not tasklist:
        print("Deine Aufgabenliste ist leer.")
    else:
        print("Deine Aufgabenliste:")
        today = datetime.now().date()
        for task in tasklist:
            task_str = f"- {task['Aufgabe']}"
            if task['Fälligkeitsdatum']:
                due_date = datetime.strptime(task['Fälligkeitsdatum'], "%d.%m.%Y").date()
                days_left = (due_date - today).days
                task_str += f" (Fällig am {task['Fälligkeitsdatum']})"
                # Markierung für Aufgaben die weniger als 48h Vorlauf haben
                if days_left <= 2:
                    task_str = f"\033[91m{task_str}\033[0m"  # wird Rot
            if task['Priorität']:
                task_str += f" [Priorität: {task['Priorität']}]"
            print(task_str)
