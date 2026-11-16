Python: Helpdesk Ticket Tracker

**Version:** 1.0.0

## Project Overview:
  This is an interactive program that allows you to view and update the status of existing tickets. The purpose of coding this program, is to further understand concepts such as for loops, boolean expressions, if/elif/else, etc.

## Features:
  - Display all existing tickets and its information (ticket_id, user, issue, etc.)
  - Search function to find a specific ticket
  - Update a ticket's status (ex. Open, Pending, Resolved)
  - Display a ticket summary that tells you the number of tickets based on the total tickets and status

## Requirements:
  - Python 3.x
  - Any Python-compatible IDE or code editor (ex. Intellij)

## How to Run:
  1. Clone or download the repository.
  2. Open the project in an IDE or terminal.
  3. Navigate to the project directory
  4. Run 'helpdesk-ticket-tracker.py'

## Example Output:
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
    
## What I learned:
  - How to create an interactive menu with if/elif/else statements
  - Nesting for loops into each of the "choices" to perform a specific function
  - Briefly touched on how to save ticket information in a .json file, but that'll come out in the next update. Stay tuned ;)

## Future Improvements:
  - Loading existing tickets when the program starts
  - Handle missing or invalid JSON files
  - Improve input validation
  - Refactor code into reusable functions
