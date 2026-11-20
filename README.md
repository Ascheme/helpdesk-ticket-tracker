Python: Helpdesk Ticket Tracker

**Version:** 1.1.0

## Project Overview:
  An interactive program that allows you to view and update the status of existing tickets. Tickets are now stored in a JSON file, as opposed to being hard coded.

## Features:
  - Display all helpdesk tickets.
  - Search for tickets by ID.
  - Update ticket statuses.
  - Display ticket summaries.
  - Save tickets to a JSON file.
  - Load previously saved tickets when the program starts.
  - Handle missing or invalid JSON files.
  - Validate user input.

## Requirements:
  - Python 3.x; no external packages required
  - Any Python-compatible IDE or code editor (ex. Intellij IDEA)

## How to Run:
  1. Download the latest release. *Note: tickets.json is created when the program saves tickets, if it doesn't already exist.*
  2. Open the project in an IDE or terminal.
  3. Navigate to the project directory
  4. Run 'helpdesk-ticket-tracker.py'

## Example Output:
```
=== Helpdesk Menu ===
1. Display All Tickets
2. Search for a Ticket
3. Update Ticket Status
4. Display Ticket Summary
5. Save and Exit

Enter your choice: 2

=== Ticket Search ===
Enter ticket ID to search: 1001
Ticket found!
-----------------------------------------------------
Ticket ID: 1001
User: John
Issue: Cannot connect to Wi-Fi
Priority: High
Status: Open
-----------------------------------------------------
```
    
## What I learned:
  - Loading and saving data to a JSON file
  - File and exception handling
  - Validating user input
  - How to refactor code into reusable functions

## Future Improvements
  - 
