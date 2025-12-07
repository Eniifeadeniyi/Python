import random
from src.customer import Customer
from src.room import Room

class Admin:
    def __init__(self,password):
        if password.strip() != "":
            self.__password = password
        else:
            self.__password = "admin123"
        self.__customers = []
        self.__rooms = []
        self.__expected_revenue = 0
        self.__actual_revenue = 0
        self.__count = 0

    def get_rooms(self):
        return self.__rooms

    def login(self, password):
        if self.__password == password:
            return True
        else:
            return False

    def __validate_customer_details(self,first_name,last_name,email,phone_number):
        if first_name.strip() != "" and last_name.strip() != "" and "@" in email.strip() and len(phone_number.strip()) == 11:
            return True
        else:
            return False

    def register_a_customer(self,first_name, last_name, email, phone_number):
        if self.__validate_customer_details(first_name,last_name,email,phone_number):
            customer = Customer(first_name, last_name, email, phone_number)
            self.__count += 1
            customer.customer_id = str(self.__count)
            self.__customers.append(customer)
            return customer.get_customer_id()

    def add_a_room(self,number,room_type):
        if room_type.lower() == "single" or room_type.lower() == "double" or room_type.lower() == "suite":
            room = Room(number, room_type.lower())
            self.__rooms.append(room)

    def check_rooms(self,number):
        for room in self.__rooms:
            if room.get_number() == number:
                return True
        return False

    def get_room(self,number):
        for room in self.__rooms:
            if room.get_number() == number:
                return room
        else:
           return None

    def find_customer(self,customer_id):
        for customer in self.__customers:
            if customer.customer_id == customer_id:
                return customer
        else:
            return None

    def find_customer_by_room_number(self,room_number):
        for customer in self.__customers:
            if customer.get_number() == room_number:
                return customer
        else:
            return None

    def check_customers(self,customer_id):
        for customer in self.__customers:
            if customer.customer_id == customer_id:
                return True
        return False

    def give_customer_a_room(self,customer_id,room_type):
        customer = self.find_customer(customer_id)
        if customer is None:
            return "Customer not found"
        for room in self.__rooms:
            if room.get_room_type() == room_type.lower() and room.get_is_available() == True:
                customer.set_room_number(room.get_number())
                customer.set_payment_due(room.get_price())

                room.set_is_booked(True)
            else:
                return "No room of selected type available"
        return None

    def generate_reference_number(self):
        reference = "RES"
        for count in range(4):
            reference += str(random.randint(0,10))
        return reference

    def make_room_available(self,customer_id, reference_number):
        customer = self.find_customer(customer_id)
        if customer is None:
            return "Customer not found"
        if customer.get_reference_number() == reference_number:
            number = customer.get_number()
            room = self.get_room(number)
            room.set_is_booked(False)
        return None

    def put_room_for_maintenance(self,number):
        room = self.get_room(number)
        if room is None:
            return "Room not found"
        else:
            room.set_is_under_maintenance(True)
            return None