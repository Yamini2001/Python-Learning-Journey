class InvalidPhoneNumberError(Exception):
    """Raised when a phone number is not provided or is invalid."""
    def __init__(self, phone_number):
        super().__init__(f"{phone_number}")
        self.phone_number = phone_number

contacts = {}


def register_contact(phonebook, name, phone_input):
    # Validate the phone number
    cleaned_name = name.replace(" ", "")
    if not name or not isinstance(name, str) or not name.strip() or not name.replace(" ", "").isalpha():
        raise ValueError("Contact name must be a non-empty alphabetic string.")
    
    # 2. Validate the phone_input parameter
    try:
        int(phone_input)
    except ValueError:
        raise InvalidPhoneNumberError("Phone number must contain digits only.")
        
    # Step 5: Save data safely as a string and return
    phonebook[name] = phone_input
    return phonebook


contacts = register_contact(contacts, "Alice", "0987654321")
print(contacts)
try:
    contacts = register_contact(contacts, "Bob", "123-456-789")
except InvalidPhoneNumberError as e:
    print(e)
try:
    contacts = register_contact(contacts, "Bob123", "9876543210")
except ValueError as e:
    print(e) 
