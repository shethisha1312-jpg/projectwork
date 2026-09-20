class JournalManager:
    
    '''
    Handles basic journal file operations like adding, viewing,
    searching and deleting entries.
    '''

    def __init__(self, filename="journal.text"):

        '''
        Initializes the journal file.
        '''
        self.filename = filename

    def new_entry(self):

        '''
        Adds a new journal entry to the file.
        '''
        try:
            print("Enter your journal entry: ")
            entry_text = input()

            print("Enter current timestamp (YYYY-MM-DD HH:MM:SS)")
            print("Timestamp: ", end="")
            timestamp = input()

            f = open(self.filename, "a")
            print("[" + timestamp + "]", file=f)
            print(entry_text, file=f)
            print("", file=f)
            f.close()

            print("Entry added successfully!")

        except PermissionError:
            print("Permission denied. Cannot write to the journal file.")
        except Exception as e:
            print("An unexpected error occured.")

    def veiw_entry(self):

        '''
        Displays all journal entries saved in the file.
        '''
        try:
            f = open(self.filename, "r")
            data = f.read()
            f.close()

            data = data.strip()

            if not data:
                print("No journal entries found. Start by adding a new entry!")
                return

            print("Your Journal Entries: ")
            print(data)

        except FileNotFoundError:
            print("The Journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Permission denied. Cannot write to the journal file.")
        except Exception as e:
            print("An unexpected error occurred.")

    def search_entry(self):

        '''
        Searches the journal file for a keyword or date.
        Search is case-insensitive.
        '''
        try:
            f = open(self.filename, "r")
            data = f.read()
            f.close()

            print("Enter a keyword or date to search: ")
            key = input().strip()

            lines = data.splitlines()
            entries = []
            cur_entry = []

            for line in lines:
                if line.strip():
                    cur_entry.append(line)
                else:
                    if cur_entry:
                        entry = cur_entry[0]

                        for item in cur_entry[1:]:
                            entry = entry + " " + item

                        entries.append(entry)
                        cur_entry = []

            if cur_entry:
                entry = cur_entry[0]

                for item in cur_entry[1:]:
                    entry = entry + " " + item

                entries.append(entry)

            matches = []

            for entry in entries:
                if key.lower() in entry.lower():
                    matches.append(entry)

            if matches:
                print("Matching Entries: ")

                for entry in matches:
                    print(entry)
            else:
                print("No Entries were found for the keyword: " + key + ".")

        except FileNotFoundError:
            print("The Journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Permission denied. Cannot write to the journal file.")
        except Exception as e:
            print("An unexpected error occurred.")

    def delete_entries(self):

        '''
        Deletes all journal entries after confirmation.
        '''
        try:
            try:
                f = open(self.filename, "r")
                f.close()

            except FileNotFoundError:
                print("No journal entries to delete.")
                return

            print(
                "Are you sure you want to delete all entries? (yes/no):",
                end=""
            )

            ans = input().strip().lower()

            if ans == "yes":
                f = open(self.filename, "w")
                f.close()

                print("All journal entries have been deleted sucessfully!")
            else:
                print("Deletion Canceled.")

        except PermissionError:
            print("Permission denied. System lock prevents file mdifications.")
        except Exception as e:
            print("An unexpected error occured.")


def main():

    '''
    Controls the main working of the Personal Journal Manager.
    Displays the menu and allows the user to choose journal operations.
    '''

    jm = JournalManager()

    print("Welcome to the Personal Journal Manager!")

    while True:
        print("1.Add a new Entry")
        print("2.View all Entries")
        print("3.Search for an Entry")
        print("4.Delete all Entries")
        print("5.Exit")

        print("Enter your choice:")

        ch = input()

        if ch == "1":
            jm.new_entry()

        elif ch == "2":
            jm.veiw_entry()

        elif ch == "3":
            jm.search_entry()

        elif ch == "4":
            jm.delete_entries()

        elif ch == "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")

            print("------ Journal Manager Documentation ------")
            print(JournalManager.__doc__)

            print("------ New Entry Documentation ------")
            print(JournalManager.new_entry.__doc__)

            print("------ View all Entry Documentation ------")
            print(JournalManager.veiw_entry.__doc__)

            print("------ Search Entry Documentation ------")
            print(JournalManager.search_entry.__doc__)

            print("------ Delete all Entry Documentation ------")
            print(JournalManager.delete_entries.__doc__)

            break

        else:
            print("Invalid option.please select valid option from menu.")


if __name__ == "__main__":
    main()

