from src.admin import Admin

admin = Admin("admin123")

menu =  """
    Welcome to The Monarchs Hotel!
    1. Login as Admin
    2. Login as Customer
    3. Register
    4. Exit
    """
checker = True
while checker:
    print(menu)
    choice = input("Enter your choice: ")
    match choice:
        case "2":
            customer_id = input("Enter customer id: ")
            if admin.check_customers(customer_id):
                customer = admin.find_customer(customer_id)
                customer_menu = """
                Welcome, Our Esteemed Customer!
                    Options:
                        1. Book Room
                        2. View Booking
                        3. Edit Profile
                        4. Check Room Availability
                        5. Payment Status
                        6. Cancel Booking
                        7. View All Available Room
                        8. View Notification
                        9. Log out
                        Enter your choice:
                    """
                checkers = True
                while checkers:
                    print(customer_menu)
                    operation = input("Enter your choice: ")
                    match operation:
                        case "1":
                            room_type = input("Enter room type: ")
                            if admin.give_customer_a_room(customer_id, room_type) != "No room of selected type available":
                                admin.give_customer_a_room(customer_id, room_type)
                                check_in = input("Enter check-in date: ")
                                number_of_nights = input("Enter number of nights: ")
                                customer.book_room(customer_id,check_in, number_of_nights)
                                customer.set_reference_number(admin.generate_reference_number())
                        case "2":
                            print("Room number: " +customer.get_room_number())
                            print("Payment Due: " +str(customer.get_payment_due()))
                            print("Payment status: " +str(customer.get_payment_status()))
                            print("Payment Paid: " +str(customer.get_payment_paid()))
                            print("Check-in-date: " +str(customer.get_check_in_date()))
                            print("Check-out-date: " +str(customer.get_check_out_date()))
                            print("Booking reference Number: " +customer.get_reference_number())
                        case "9":
                            checkers = False
                        case "7":
                            rooms = admin.get_rooms()
                            for room in rooms:
                                if room.get_is_available():
                                    print(room.get_number() + room.get_room_type())
                        case "6":
                            reference_number = input("Enter reference number: ")
                            admin.make_room_available(customer_id,reference_number)
                            customer.cancel_booking(customer_id,reference_number)
                        case "4":
                            number = input("Enter room number: ")
                            if admin.check_rooms(number):
                                room = admin.get_room(number)
                                if room.get_is_available():
                                    print("Available")
                                else:
                                    print("Unavailable")
                        case "5":
                            if customer.get_payment_status():
                                print("Paid")
                            else:
                                print("Unpaid!")
                        case "3":
                            menu = """"
                            1. First name
                            2. Last name
                            3. Phone number
                            4. Email
                            5. back
                            """
                            cheek = True
                            while cheek:
                                print(menu)
                                pick = input("Enter your choice: ")
                                match pick:
                                    case "1":
                                        new_first_name = input("Enter first name: ")
                                        customer.first_name = new_first_name
                                    case "2":
                                        new_last_name = input("Enter last name: ")
                                        customer.last_name = new_last_name
                                    case "3":
                                        new_phone_number = input("Enter phone number: ")
                                        customer.phone_number = new_phone_number
                                    case "4":
                                        new_email = input("Enter email: ")
                                        customer.email = new_email
                                    case "5":
                                        cheek = False
                                    case _: print("Invalid input")


        case "3":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            print("Your id is: " +str(admin.register_a_customer(first_name, last_name, email, phone_number)))
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
                                if room.get_is_available():
                                    print("Room status: Available")
                                else:
                                    print("Room status: Unavailable")
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
                        case _:
                            print("Invalid input")
