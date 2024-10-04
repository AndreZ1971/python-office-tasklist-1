
import csv
from datetime import datetime, timedelta


tasklist = []

# Erstellen der Aufgabe
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

# zum Anzeigen
def show_tasklist():
    if not tasklist:
        print("Du hast keine Aufgaben die erledigt werden müssen.")
    else:
        print("Deine Aufgabenliste:")
        # Sortier Funktion
        priority_order = {"hoch": 1, "mittel": 2, "niedrig": 3}
        sorted_tasklist = sorted(tasklist, key=lambda x: priority_order.get(x['Priorität'], 2))
        today = datetime.now().date()
        for task in sorted_tasklist:
            task_str = f"- {task['Aufgabe']}"
            if task['Fälligkeitsdatum']:
                due_date = datetime.strptime(task['Fälligkeitsdatum'], "%d.%m.%Y").date()
                days_left = (due_date - today).days
                task_str += f" (Fällig am {task['Fälligkeitsdatum']})"
                # Markiere Aufgaben, die in 2 Tagen oder weniger fällig sind
                if days_left <= 2:
                    task_str = f"\033[91m{task_str}\033[0m"  # Rot färben
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

# Exportieren in eine CSV-Datei
def export_tasklist():
    if not tasklist:
        print("Die Aufgabenliste ist leer. Nichts zu exportieren.")
    else:
        with open('aufgabenliste.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Aufgabe', 'Fälligkeitsdatum', 'Priorität']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasklist:
                writer.writerow(task)
        print("Aufgabenliste wurde erfolgreich in 'aufgabenliste.csv' exportiert.")

# Überprüfen
def check_due_tasks():
    today = datetime.now().date()
    due_tasks = [task for task in tasklist if task['Fälligkeitsdatum'] and datetime.strptime(task['Fälligkeitsdatum'], "%d.%m.%Y").date() == today]
    if due_tasks:
        print("\n*** Benachrichtigung: Folgende Aufgaben sind heute fällig! ***")
        for task in due_tasks:
            print(f"- {task['Aufgabe']} [Priorität: {task['Priorität']}]")


def main():
    check_due_tasks()
    while True:
        print("\n----- Aufgabenliste -----")
        print("1. Aufgabe erstellen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe entfernen")
        print("4. Aufgaben exportieren")
        print("5. Programm beenden")
        choice = input("Bitte wähle eine Option (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasklist()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            export_tasklist()
        elif choice == "5":
            print("Schluss für heute!")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle zwischen 1 und 5.")

if __name__ == "__main__":
    main()
