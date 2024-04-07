"""
Email Simulator:

This Python script simulates a basic email application. It allows users to interact with a simulated inbox,
including reading emails, marking them as read, and viewing unread emails. The program initialises with a
pre-defined set of sample emails for demonstration purposes.

Classes:
- Email: Represents an email with attributes such as email address, subject line, and content. Provides methods
         for marking an email as read.
         
Functions:
- populate_inbox(): Populates the inbox with sample email objects at program startup.
- list_emails(): Lists unread emails in the inbox along with their subject lines.
- read_email(index): Reads an email at the specified index, displaying its details and marking it as read.
"""

class Email:
    # Class variable to track whether an email has been read
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        # Constructor to initialise an email object with email_address, subject_line, and email_content
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        # Instance variable to track whether this specific email has been read
        self.has_been_read = Email.has_been_read  # Initialise instance variable with class variable

    def mark_as_read(self):
        # Method to mark an email as read by setting has_been_read to True
        self.has_been_read = True

    @classmethod
    def mark_all_as_read(cls, emails):
        # Class method to mark all emails in a list as read
        for email in emails:
            email.mark_as_read()

def populate_inbox():
    # Function to populate the inbox with sample emails
    # Create 3 sample emails and add them to the Inbox list
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Hello, welcome to HyperionDev!")
    email2 = Email("sender2@example.com", "Great work on the bootcamp!", "Keep up the great work!")
    email3 = Email("sender3@example.com", "Your excellent marks!", "Congratulations on your excellent marks!")
    
    # Add the emails to the inbox list
    inbox.extend([email1, email2, email3])

def list_emails():
    # Function to list all unread emails
    # Loop through the inbox and print each email's subject line along with a corresponding number
    print("\nUnread Emails:")
    for i, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{i}. {email.subject_line}")

def read_email(index):
    # Function to read an email at a specified index
    if 0 <= index < len(inbox):
        email = inbox[index]
        # Display email details
        print(f"\nEmail from {email.email_address}:\n")
        print("Subject:", email.subject_line)
        print("Content:", email.email_content)
        # Mark the email as read
        email.mark_as_read()
        print(f"\nEmail from {email.email_address} marked as read.\n")
    else:
        print("\nInvalid index. Please select a valid index from the list.")

# Initialise empty inbox list
inbox = []

# Populate the inbox with sample emails
populate_inbox()

# Main program loop
while True:
    # Display menu options and prompt user for choice
    user_choice = input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: ''')
    
    # Handle user choice
    if user_choice == '1':
        # Read an email
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
        
    elif user_choice == '2':
        # View unread emails
        list_emails()
            
    elif user_choice == '3':
        # Quit application
        print("\nExiting application...")
        break

    else:
        # Invalid input
        print("\nOops - incorrect input. Please enter a valid option.")
