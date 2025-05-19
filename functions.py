from classes import Owner, Pet, Consultation

# Lists to store Owner and Pet objects
owners = []
pets = []

def register_owner():
    """Registers a new owner and adds them to the owners list."""
    print("=== Register Owner ===")
    name = input("Owner's name: ")
    phone = input("Phone: ")
    address = input("Address: ")
    owner = Owner(name, phone, address)
    owners.append(owner)
    print("Owner successfully registered.")
    return owner

def find_owner_by_name(name):
    """Searches for an owner by name."""
    for o in owners:
        if o.name.lower() == name.lower():
            return o
    return None

def register_pet():
    """Registers a new pet and assigns it to an owner."""
    print("=== Register Pet ===")
    name = input("Pet's name: ")
    species = input("Species: ")
    breed = input("Breed: ")
    age = input("Age: ")
    owner_name = input("Owner's name: ")
    owner = find_owner_by_name(owner_name)
    if not owner:
        print("Owner not found. Please register them first.")
        owner = register_owner()
    pet = Pet(name, species, breed, age, owner)
    pets.append(pet)
    print("Pet successfully registered.")

def find_pet_by_name(name):
    """Searches for a pet by name."""
    for p in pets:
        if p.name.lower() == name.lower():
            return p
    return None

def register_consultation():
    """Registers a veterinary consultation for a specific pet."""
    print("=== Register Consultation ===")
    pet_name = input("Pet's name: ")
    pet = find_pet_by_name(pet_name)
    if not pet:
        print("Pet not found, please register it first.")
        return
    date = input("Date of consultation: ")
    reason = input("Reason: ")
    diagnosis = input("Diagnosis: ")
    consultation = Consultation(date, reason, diagnosis, pet)
    pet.add_consultation(consultation)
    print("Consultation successfully registered.")

def list_pets():
    """Displays all registered pets and their owners."""
    print("=== List of Pets ===")
    if not pets:
        print("No pets registered.")
    for p in pets:
        print(p)
        print("-" * 40)

def view_pet_history():
    """Displays the consultation history of a specific pet."""
    print("=== Consultation History ===")
    pet_name = input("Pet's name: ")
    pet = find_pet_by_name(pet_name)
    if pet:
        print(pet.show_consultations())
    else:
        print("Pet not found.")