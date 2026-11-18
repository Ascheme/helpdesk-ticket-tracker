import json
from json import JSONDecodeError

#ticket list that will contain dictionaries
tickets = []

def load_tickets():
    #checks if .json file exists, and continues to the menu if it does not
    try:
        #reads the tickets from a .json file and converts it back into python
        with open("tickets.json", "r") as file:
            tickets = json.load(file)
            return tickets

    except FileNotFoundError:
        print("No JSON file detected. Creating an empty list...\n")
        return []
    except JSONDecodeError:
        print("Invalid JSON format detected. Creating an empty list...\n")
        return []

def save_tickets(tickets):
    #writes the tickets to a file before exiting the program (converts it to json)
    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)

#calling the function after defining it
tickets = load_tickets()

#helpdesk menu
while True:
    print("=== Helpdesk Menu ===")
    print("1. Display All Tickets\n2. Search for a Ticket\n3. Update Ticket Status\n4. Display Ticket Summary\n5. Save and Exit")
    user_choice = input("\nEnter your choice: ")

    #Displays all tickets
    if user_choice == "1":
        print("\n=== All helpdesk tickets ===\n")

        for ticket in tickets:
            print(f"Ticket ID: {ticket['ticket_id']}\nUser: {ticket['user']}\nIssue: {ticket['issue']}\nPriority: {ticket['priority']}\nStatus: {ticket['status']}\n-----------------------------------------------------")
        print("--End of list--\n")

    #search function
    elif user_choice == "2":
        print("\n=== Ticket Search ===")
        search_id = input("Enter ticket ID to search: ")
        ticket_found = False

        for ticket in tickets:
            if ticket["ticket_id"] == search_id:
                ticket_found = True
                print("Ticket found!")
                print(f"-----------------------------------------------------\nTicket ID: {ticket['ticket_id']}\nUser: {ticket['user']}\nIssue: {ticket['issue']}\nPriority: {ticket['priority']}\nStatus: {ticket['status']}\n-----------------------------------------------------\n")
                break

        if not ticket_found:
            print("Ticket not found. :(\n")

    #update a ticket's status
    elif user_choice == "3":
        search_id = input("\nEnter ticket ID to search: ")
        ticket_found = False

        for ticket in tickets:
            if ticket["ticket_id"] == search_id:
                ticket_found = True
                print(f"\nTicket found!\nCurrent status: {ticket['status']}")

                #removes spaces before/after and capitalizes the first letter entered
                new_status = input("\nEnter new status: ").strip().title()

                #simplified way to determine the new status of a ticket, instead of repetitive if/elif statements
                if new_status in ["Open", "Pending", "Resolved"]:
                    ticket["status"] = new_status
                else:
                    print("Invalid status. Enter 'Open', 'Pending', or 'Resolved'.\n")

                #when valid status is entered, a success message appears and displays new status
                if new_status in ["Open", "Pending", "Resolved"]:
                    print(f"\nTicket {ticket['ticket_id']} successfully updated!")
                    print(f"New status: {ticket['status']}\n")
                    break

        if not ticket_found:
            print("Ticket does not exist. Please enter a 4-digit ticket number.\n")

    elif user_choice == "4":
        #reset ticket counters to 0
        open_tickets = 0
        pending_tickets = 0
        resolved_tickets = 0

        #counts tickets based on status
        for ticket in tickets:
            if ticket["status"] == "Open":
                open_tickets += 1
            elif ticket["status"] == "Pending":
                pending_tickets += 1
            elif ticket["status"] == "Resolved":
                resolved_tickets += 1

        print("\n=== Ticket Summary ===")
        print(f"Total tickets: {len(tickets)}")
        print(f"Total open tickets: {open_tickets}")
        print(f"Total pending tickets: {pending_tickets}")
        print(f"Total resolved tickets: {resolved_tickets}\n")

    elif user_choice == "5":
        save_tickets(tickets)
        print("\nExiting program...Good bye :)")
        break

    else:
        print("Invalid selection. Please choose 1-5.\n")