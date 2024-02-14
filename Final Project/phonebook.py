from tabulate import tabulate
import sys
import csv
import re

def main():
    contact = []

    try:
        if len(sys.argv) == 2:
            csv_contacts = load_csv_contact(sys.argv[1])
            if csv_contacts is not None:
                contact.extend(csv_contacts)
            else:
                print("Failed to load CSV from file")

        while True:
            print("PHONEBOOK OPTION")
            print("1. View contacts")
            print("2. Add a contact")
            print("3. Update a contact")
            print("4. Remove a contact")
            print("5. Search for a contact")
            print("6. Save contacts to CSV")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                view_contact(contact)
            elif choice == '2':
                name = input("Name: ")
                phone = input("Phone number: ")
                add_contact(contact, name, phone)
            elif choice == '3':
                name = input("Name: ")
                new_number = input("Enter new phone number: ")
                update_contact(contact, name, new_number)
            elif choice == '4':
                name = input("Name: ")
                delete_contact(contact, name)
            elif choice == '5':
                name = input("Name: ")
                search_contact(contact, name)
            elif choice == '6':
                filename = input("Enter filename to save: ")
                write_csv(contact, filename)
            elif choice == '7':
                sys.exit("Exit program successful")
            else:
                print("Invalid input - Enter a number from 1 to 6\n")

    except KeyboardInterrupt:
        sys.exit("\nExit program due to KeyboardInterrupt")


def view_contact(contacts):
    count = 0
    if contacts:
        table_data = []
        for i, contact in enumerate(contacts):
            count += 1
            table_data.append([i + 1, contact['name'], contact['phone_number']])
        print(tabulate(table_data, headers=["", "Name", "Phone Number"], tablefmt="grid"))
        print(f"You have {count} contact(s)\n")
    else:
        print("\nNo contact found\n")

def add_contact(contacts, name, phone):
    if re.search(r"[A-Za-z]+ [A-Za-z]+", name):
        if re.search(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", phone):
            contacts.append({"name": name, "phone_number": phone})
            print("\nContact added successfully\n")
        else:
            print("Invalid phone number format\n")
    else:
        print("Invalid name format\n")

def update_contact(contact_list, name, new_number):
    updated = False
    for contact in contact_list:
        if contact["name"] == name:
            contact["phone_number"] = new_number
            if re.search(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", new_number):
                updated = True
                print(f"Phone number updated for {name}\n")
                break
            else:
                print("Invalid phone number format\n")
    if not updated:
        print(f"No contact found with the name {name}\n")

def delete_contact(contact_list, name):
    for contact in contact_list:
        if contact["name"] == name:
            contact_list.remove(contact)
            print(f"{contact['name']} deleted successfully\n")

def search_contact(contact_list, name):
    found = False
    for contact in contact_list:
        if contact["name"] == name:
            print()
            print("Contact found...")
            print(f"Name: {contact['name']}")
            print(f"Number: {contact['phone_number']}\n")
            found = True
            break
    if not found:
        print("Contact not found!\n")

def load_csv_contact(filename):
    contacts = []
    count = 0
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:
                count += 1
                name, phone_number = row
                contacts.append({"i": i, "name": name, "phone_number": phone_number})
        print(f"\n{count} Contact added successfully\n")
    return contacts

def write_csv(contacts, filename):
    if ".csv" not in filename:
        print("Filename must have a .csv extension.\n")
        return

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'phone_number'])
        for contact in contacts:
            writer.writerow([contact["name"], contact["phone_number"]])
        print("\nContact saved to a file\n")


if __name__ == "__main__":
    main()