from project import view_contact, add_contact, update_contact, delete_contact, search_contact, load_csv_contact, write_csv

def main():
    test_view_contact()
    test_add_contact()
    test_update_contact()
    test_delete_contact()
    test_search_contact()

def test_view_contact():
    contacts = []
    view_contact(contacts)
    assert contacts == []

def test_add_contact():
    contacts = []
    name = "John Harvard"
    phone = "457-235-5667"
    add_contact(contacts, name, phone)
    assert contacts == [{"name": "John Harvard", "phone_number": "457-235-5667"}]

def test_update_contact():
    contacts = [{"name": "John Harvard", "phone_number": "564-748-9090"}]
    name = "John Harvard"
    new_number = "767-786-7777"
    update_contact(contacts, name, new_number)
    assert contacts == [{"name": "John Harvard", "phone_number": "767-786-7777"}]

def test_delete_contact():
    contacts = [{"name": "John Harvard", "phone_number": "457-235-5667"}]
    name = "John Harvard"
    delete_contact(contacts, name)
    assert contacts == []

def test_search_contact():
    contacts = []
    name = "Megan White"
    search_contact(contacts, name)
    assert contacts == []



if __name__ == "__main__":
    main()