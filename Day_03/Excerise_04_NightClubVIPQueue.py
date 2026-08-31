VIP_guest_list = ["Guido", "Esha", "Rajan", "Kishori"]

while True:
    print(f"Current VIP queue: {VIP_guest_list}")

    bouncer = input("Enter guest name: ")

    if bouncer == "exit":
        break

    if bouncer in VIP_guest_list:
        VIP_guest_list.remove(bouncer)
        VIP_guest_list.insert(0, bouncer)
        print(f"{bouncer} moved to the front!")
    else:
        print("Access denied. Not on the VIP list.")

    print()
