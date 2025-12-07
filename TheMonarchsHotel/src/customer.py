
from datetime import datetime, timedelta

class Customer:
    def __init__(self, first_name, last_name, email, phone_number):
        if first_name.strip() and last_name.strip() and email.strip() and len(phone_number.strip()) == 11:
            self.__customer_id = ""
            self.__first_name = first_name.strip()
            self.__last_name = last_name.strip()
            self.__email = email.strip()
            self.__phone_number = phone_number.strip()
            self.__roomNumber = ""
            self.__payment_status = False
            self.__payment_due = 0
            self.__total_paid = 0
            self.__reference_number = ""
            self.__check_in_date = ""
            self.__checkout_date = ""


    @property
    def customer_id(self):
        return self.__customer_id
    @customer_id.setter
    def customer_id(self,value : str):
        self.__customer_id = value

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self,first_name):
        if first_name.strip():
            self.__first_name = first_name.strip()

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self,last_name):
        if last_name.strip():
            self.__last_name = last_name.strip()

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        if email.strip():
            self.__email = email.strip()

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self,phone_number):
        if len(phone_number.strip()) == 11:
            self.__phone_number = phone_number.strip()

    def get_payment_due(self):
        return self.__payment_due

    def get_total_paid(self):
        return self.__total_paid

    def get_reference_number(self):
        return self.__reference_number

    def get_check_in_date(self):
        return self.__check_in_date

    def get_checkout_date(self):
        return self.__checkout_date

    def set_check_in_date(self,value):
        self.__check_in_date = value

    def set_checkout_date(self,value):
        self.__checkout_date = value

    def get_payment_status(self):
        return self.__payment_status

    def get_room_number(self):
        return self.__roomNumber

    def book_a_room(self,customer_id, check_in_date, number_of_nights):
        if customer_id == self.__customer_id and number_of_nights.strip().isdigit():
            self.__check_in_date = check_in_date
            self.__check_out_date = check_in_date + timedelta(days=int(number_of_nights.strip()))


    def cancel_booking(self,customer_id, reference_number):
        if customer_id == self.__customer_id and reference_number == self.__reference_number:
            self.__roomNumber = ""
            self.__payment_status = False
            self.__payment_due = 0
            self.__total_paid = 0
            self.__check_in_date = ""
            self.__checkout_date = ""
            self.__reference_number = ""

    def get_customer_id(self):
        return self.__customer_id

    def make_payment(self,amount):
        if amount > self.__payment_due or amount <= 0:
            return "Invalid"
        self.__payment_due -= amount
        self.__total_paid += amount
        if self.__payment_due == 0:
            self.__payment_status = True

    def set_reference_number(self,reference_number):
        self.__reference_number = reference_number

    def set_room_number(self, number):
        self.__roomNumber = number

    def set_payment_due(self, amount):
        self.__payment_due = amount