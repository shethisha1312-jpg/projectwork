# Personal Journal Manager

from datetime import datetime
import os


class JournalManager:
    """
    Manages the journal file.
    It provides functions to add, display, search and delete
    journal records and also handles file-related errors.
    """

    def __init__(self, journal_file="journal.txt"):
        """
        Initializes the journal manager.

        Attributes:
            journal_file (str): Name of the text file used for journal data.
        """
        self.journal_file = journal_file

    def add_record(self):
        """
        Adds a new journal record to the end of the file.
        The record contains the current timestamp and user text.
        """
        try:
            note = input("Enter your journal entry: ").strip()

            if note == "":
                print("Journal entry cannot be empty.")
                return

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.journal_file, "a") as journal:
                journal.write("[" + current_time + "]\n")
                journal.write(note + "\n")
                journal.write("\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Permission denied. Cannot write to the journal file.")
        except OSError:
            print("An error occurred while adding the entry.")

    def display_records(self):
        """
        Displays all records stored in the journal file.
        """
        try:
            with open(self.journal_file, "r") as journal:
                data = journal.read()

            if data.strip() == "":
                print("No journal entries found. Start by adding a new entry!")
                return

            print("\nYour Journal Entries:")
            print("-" * 35)
            print(data.strip())

        except FileNotFoundError:
            print("The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Permission denied. Cannot read the journal file.")
        except OSError:
            print("An error occurred while reading the file.")

    def search_records(self):
        """
        Searches the journal for a keyword or date.
        The search is case-insensitive.
        """
        try:
            with open(self.journal_file, "r") as journal:
                data = journal.read()

            search_value = input(
                "Enter a keyword or date to search: "
            ).strip()

            if search_value == "":
                print("Search value cannot be empty.")
                return

            records = data.strip().split("\n\n")
            results = []

            for record in records:
                if search_value.lower() in record.lower():
                    results.append(record)

            if results:
                print("\nMatching Entries:")
                print("-" * 35)

                for item in results:
                    print(item)
                    print("-" * 35)
            else:
                print(
                    "No entries were found for the keyword: "
                    + search_value + "."
                )

        except FileNotFoundError:
            print("The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Permission denied. Cannot search the journal file.")
        except OSError:
            print("An error occurred while searching the file.")

    def remove_all_records(self):
        """
        Deletes all journal records after asking for confirmation.
        """
        try:
            if not os.path.exists(self.journal_file):
                print("No journal entries to delete.")
                return

            confirmation = input(
                "Are you sure you want to delete all entries? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                with open(self.journal_file, "w") as journal:
                    journal.write("")

                print("All journal entries have been deleted.")
            elif confirmation == "no":
                print("Deletion cancelled.")
            else:
                print("Invalid input. Please enter yes or no.")

        except PermissionError:
            print("Permission denied. Cannot modify the journal file.")
        except OSError:
            print("An error occurred while deleting the entries.")


def main():
    """
    Controls the Personal Journal Manager.
    Displays the menu and performs the selected operation.
    """

    journal = JournalManager()

    print("Welcome to Personal Journal Manager!")

    while True:

        print("\nPlease select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            journal.add_record()

        elif choice == "2":
            journal.display_records()

        elif choice == "3":
            journal.search_records()

        elif choice == "4":
            journal.remove_all_records()

        elif choice == "5":
            print(
                "Thank you for using Personal Journal Manager. Goodbye!"
            )

            print("\n------ Journal Manager Documentation ------")
            print(JournalManager.__doc__)

            print("------ Add Record Documentation ------")
            print(JournalManager.add_record.__doc__)

            print("------ Display Records Documentation ------")
            print(JournalManager.display_records.__doc__)

            print("------ Search Records Documentation ------")
            print(JournalManager.search_records.__doc__)

            print("------ Remove Records Documentation ------")
            print(JournalManager.remove_all_records.__doc__)

            break

        else:
            print("Invalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()