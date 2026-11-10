#1. ticket list that contains dictionaries
tickets = []


#2. dictionaries that holds ticket info, each dictionary = a ticket
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

#3. adding tickets to the list
tickets.append(ticket_1001)
tickets.append(ticket_1002)
tickets.append(ticket_1003)

#4. initializing ticket counters
open_tickets = 0
pending_tickets = 0
resolved_tickets = 0

#5. display tickets and count statuses
print("=== Helpdesk Ticket Tracker ===")
for ticket in tickets:
    if ticket["status"] == "Open":
        open_tickets += 1
    elif ticket["status"] == "Pending":
        pending_tickets += 1
    elif ticket["status"] == "Resolved":
        resolved_tickets += 1
    print(f"\nTicket ID: {ticket['ticket_id']}\nUser: {ticket['user']}\nIssue: {ticket['issue']}\nPriority: {ticket['priority']}\nStatus: {ticket['status']}")

#6. display ticket summary
print("\n=== Ticket Summary ===")
print(f"Total tickets: {len(tickets)}")
print(f"Total open tickets: {open_tickets}")
print(f"Total pending tickets: {pending_tickets}")
print(f"Total resolved tickets: {resolved_tickets}")

#7. search for a ticket
print("\n=== Ticket Search ===")
search_id = input("Enter ticket ID to search: ")

ticket_found = False

for ticket in tickets:
    if ticket["ticket_id"] == search_id:
        print("ticket found")

#8. Update a ticket status
print("\n=== Update Ticket Status ===")
search_id = input("\nEnter ticket ID :")

ticket_found = False

for ticket in tickets:
    if ticket["ticket_id"] == search_id:
        ticket_found = True
        print(f"\nCurrent status: {ticket["status"]}")

        new_status = input("\nEnter new status: ")

        if new_status == "Open":
            ticket["status"] = new_status
        elif new_status == "Pending":
            ticket["status"] = new_status
        elif new_status == "Resolved":
            ticket["status"] = new_status
        else:
            print("Enter a valid status. [Open, Pending, Resolved]")

        print(f"\nTicket {ticket["ticket_id"]} successfully updated!")
        print(f"New status: {ticket["status"]}")
