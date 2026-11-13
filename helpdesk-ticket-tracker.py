# Ticket list that will contain dictionaries
tickets = []

# Dictionaries that holds ticket info, each dictionary = a ticket
ticket_1001 = {
    "ticket_id": "1001",
    "user": "John",
    "issue": "Cannot connect to Wi-Fi",
    "priority": "High",
    "status": "Open",
}
ticket_1002 = {
    "ticket_id": "1002",
    "user": "Sarah",
    "issue": "Printer not responding",
    "priority": "Normal",
    "status": "Pending",
}
ticket_1003 = {
    "ticket_id": "1003",
    "user": "Michael",
    "issue": "Password reset",
    "priority": "Low",
    "status": "Resolved",
}

# Tickets being added to the list
tickets.append(ticket_1001)
tickets.append(ticket_1002)
tickets.append(ticket_1003)

#Initializing ticket counters
open_tickets = 0
pending_tickets = 0
resolved_tickets = 0

# Calculating ticket count based on status
for ticket in tickets:
    if ticket["status"] == "Open":
        open_tickets += 1
    elif ticket["status"] == "Pending":
        pending_tickets += 1
    elif ticket["status"] == "Resolved":
        resolved_tickets += 1

# Helpdesk menu
while True:
    print("=== Helpdesk Menu ===")
    print(f"1. Display All Tickets\n2. Search for a Ticket\n3. Update Ticket Status\n4. Display Ticket Summary\n5. Exit")
    user_choice = input("\nEnter your choice: ")

    #Displays all tickets
    if user_choice == "1":
        print(f"\n=== All helpdesk tickets ===\n")

        for ticket in tickets:
            print(f"Ticket ID: {ticket['ticket_id']}\nUser: {ticket['user']}\nIssue: {ticket['issue']}\nPriority: {ticket['priority']}\nStatus: {ticket['status']}\n-----------------------------------------------------")
        print("--End of list--\n")

    #Intergrated search function
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

    #Update a ticket's status
    elif user_choice == "3":
        search_id = input("\nEnter ticket ID to search: ")
        ticket_found = False

        for ticket in tickets:
            if ticket["ticket_id"] == search_id:
                ticket_found = True
                print(f"\nTicket found!\nCurrent status: {ticket['status']}")

                new_status = input("\nEnter new status: ")

                #checks/updates status if valid status is entered
                if new_status == "Open":
                    ticket["status"] = new_status
                elif new_status == "Pending":
                    ticket["status"] = new_status
                elif new_status == "Resolved":
                    ticket["status"] = new_status
                else:
                    print("Invalid status. [Ex. Open, Pending, or Resolved]\n")

                    #when valid status is entered, a success message appears and displays new status
                if new_status in ["Open", "Pending", "Resolved"]:
                    print(f"\nTicket {ticket['ticket_id']} successfully updated!")
                    print(f"New status: {ticket['status']}\n")
                    break

        if not ticket_found:
            print("Ticket does not exist. Please enter a 4-digit ticket number.\n")

    elif user_choice == "4":
        print("\n=== Ticket Summary ===")
        print(f"Total tickets: {len(tickets)}")
        print(f"Total open tickets: {open_tickets}")
        print(f"Total pending tickets: {pending_tickets}")
        print(f"Total resolved tickets: {resolved_tickets}\n")

    elif user_choice == "5":
        print("\nExiting program...Good bye :)")
        break