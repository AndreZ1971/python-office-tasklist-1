
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
        print("Du hast keine Aufgaben.")
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


# Funktion zum löschen
def remove_task():
    if not tasklist:
        print("Die Aufgabenliste ist leer.")
    else:
        print("Welche Aufgabe möchtest du entfernen?")
        for idx, task in enumerate(tasklist, 1):
            print(f"{idx}. {task['Aufgabe']}")
        try:
            choice = int(input("Bitte gib die Nummer der zu entfernenden Aufgabe ein: "))
            if 1 <= choice <= len(tasklist):
                removed_task = tasklist.pop(choice - 1)
                print(f"Aufgabe '{removed_task['Aufgabe']}' wurde entfernt.")
            else:
                print("Ungültige Auswahl.")
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")


def main():
    while True:
        print("\n----- Aufgabenliste -----")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe entfernen")
        print("4. Programm beenden")
        choice = input("Bitte wähle eine Option (1-4): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasklist()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2, 3 oder 4.")
