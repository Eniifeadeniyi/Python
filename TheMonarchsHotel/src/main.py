from src.admin import Admin

admin = Admin("admin123")

menu =  """
    Welcome to The Monarchs Hotel!
    1. Login as Admin
    2. Login as Customer
    3. Register
    4. Exit
    """
checker = False
while checker:
    print(menu)
    choice = input("Enter your choice: ")
    match choice:
        case "4":
            print("Goodbye")
            checker = False
        case "1":
            password = input("Enter your password: ")
            if admin.login(password):
                admin_menu = """
        Welcome, Madam Eniife!
            Options:
                1. View All Rooms
                2. Manage Reservations
                3. Generate Reports
                4. Mark Rooms for Maintenance
                5. Add rooms
                6. View guest Details
                7. Log out
            """
                check = True
                while check:
                    print(admin_menu)
                    option = input("Enter your choice: ")
                    match option:
                        case "1":
                            rooms = admin.get_rooms()
                            for room in rooms:
                                print("Room number: " + room.get_number())
                                print("Room type: " + room.get_room_type())
                                print("Room status: " + room.get_is_available())
                                print()
                        case "4":
                            number = input("Enter room number: ")
                            if admin.check_rooms(number):
                                admin.put_room_for_maintenance(number)
                        case "5":
                            number = input("Enter room number: ")
                            room_type = input("Enter room type: ")
                            admin.add_a_room(number,room_type)
                        case "7":
                            check = False
                        case "6":
                            number = input("View details of customer in room: ")
                            room = admin.get_room(number)
                            if room is not None and room.get_is_booked() == True:
                                customer = admin.find_customer_by_room_number(number)
                                print("First Name: " + customer.get_first_name())
                                print("Last Name: " + customer.get_last_name())
                                print("Phone Number: " + customer.get_phone_number())
                                print("Email: " + customer.get_email())
                                print("Reservation Details:")
                                print("Room Number: " +customer.get_room_number())
                                print("Check-in-date: " + customer.get_check_in_date())
                                print("Check-out-date: " + customer.get_check_out_date())
                                print("Booking Reference Number: " +customer.get_reference_number())



