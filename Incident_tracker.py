# incident_tracker.py
# A basic incident tracking system using Python (run in terminal)

import datetime

incidents = []

class Incident:
    def __init__(self, title, description):
        self.id = len(incidents) + 1
        self.title = title
        self.description = description
        self.status = 'Open'
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def close(self):
        self.status = 'Closed'

    def __str__(self):
        return f"[{self.id}] {self.title} ({self.status})\n{self.description}\nReported at: {self.timestamp}\n"

def show_menu():
    print("\nIncident Tracker")
    print("1. Report new incident")
    print("2. View all incidents")
    print("3. Close an incident")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        title = input("Enter incident title: ")
        description = input("Enter incident description: ")
        new_incident = Incident(title, description)
        incidents.append(new_incident)
        print("Incident reported successfully.")

    elif choice == '2':
        if not incidents:
            print("No incidents reported yet.")
        else:
            for inc in incidents:
                print(inc)

    elif choice == '3':
        try:
            incident_id = int(input("Enter the ID of the incident to close: "))
            for inc in incidents:
                if inc.id == incident_id:
                    inc.close()
                    print(f"Incident {incident_id} closed.")
                    break
            else:
                print("Incident not found.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '4':
        print("Exiting incident tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
