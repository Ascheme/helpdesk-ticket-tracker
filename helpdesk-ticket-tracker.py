#ticket list that contains dictionaries
tickets = []

#dictionaries that holds ticket info, each dictionary = a ticket
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

#adding tickets to the ticket list
tickets.append(ticket_1001)
tickets.append(ticket_1002)
tickets.append(ticket_1003)

#setting ticket counters
open_tickets = 0
pending_tickets = 0
resolved_tickets = 0

while True:
    try:
        user_input = (input("Enter ticket ID to search: "))

        for ticket in tickets:
            if ticket["status"] == "Open":
                open_tickets += 1
            elif ticket["status"] == "Pending":
                pending_tickets += 1
            elif ticket["status"] == "Resolved":
                resolved_tickets += 1

        for ticket in tickets:
            if user_input == ticket["ticket_id"]:
                

    except ValueError:
        if (input("Enter ticket ID to search: ")) != tickets["ticket_id"]:
            print("Invalid ticket ID")

    (print(f"=== Ticket Found ==="))









# #displays ticket counts
# print("\n=== Ticket Summary ===")
# print(f"Total tickets: {len(tickets)}")
# print(f"Total open tickets: {open_tickets}")
# print(f"Total pending tickets: {pending_tickets}")
# print(f"Total resolved tickets: {resolved_tickets}")