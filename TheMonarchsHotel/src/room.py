class Room:
    def __init__(self, number, room_type):
        if len(number.strip()) == 3 and(room_type.strip().lower() == "single" or room_type.strip().lower() == "double" or room_type.strip().lower() == "suite"):
            self.__number = number
            self.__room_type = room_type.lower()
            if self.__room_type == "single":
                self.__price = 10000
            elif self.__room_type == "double":
                self.__price = 12000
            elif self.__room_type == "suite":
                self.__price = 15000
            self.__is_available = True
            self.__is_under_maintenance = False
            self.__is_booked = False

    def get_number(self):
        return self.__number
    def get_room_type(self):
        return self.__room_type

    @property
    def price(self):
        return self.__price

    def get_is_available(self):
        return self.__is_available

    def get_is_under_maintenance(self):
        return self.__is_under_maintenance

    def get_is_booked(self):
        return self.__is_booked

    def get_is_festive_period(self):
        return self.__is_festive_period

    def set_is_available(self):
        if self.__is_booked == True or self.__is_under_maintenance == True:
            self.__is_available = False
        if self.__is_booked == False and self.__is_under_maintenance == False:
            self.__is_available = True

    def set_is_booked(self, input):
        self.__is_booked = input
        self.set_is_available()

    def set_is_festive_period(self, input):
        self.__is_festive_period = input

    def set_is_under_maintenance(self, input):
        self.__is_under_maintenance = input
        self.set_is_available()




