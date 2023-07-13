from appointment import Appointment
from barber import Barber

class Client:
    id = 1
    all_clients = []

    def __init__(self, fname, lname, phone, email):
        self.id = Client.id
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        Client.id+=1
        Client.all_clients.append(self)

    def __str__(self):
        return f"Client #{self.id} first name: {self.fname} last name: {self.lname} email: {self.email} phone number: {self.phone}"

    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self, value):
        if type(value) == str:
            self._fname = value
        else:
            raise Exception("Must enter a string value")

    @property
    def lname(self):
        return self._lname
    
    @fname.setter
    def lname(self, value):
        if type(value) == str:
            self._lname = value
        else:
            raise Exception("Must enter a string value")
        
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self,value):
        if type(value) == str:
            self._phone = value

    def book_appointment(self, barber_id, date, cut_style, price):
        Appointment(barber_id, self.id, date, cut_style, price)

    def get_appointments(self):
        appointments = []
        for appointment in Appointment.all_appointments:
            if appointment.client_id == self.id:
                appointments.append(appointment)
        return appointments

    def get_barbers(self):
        id_list = []
        barbers = []
        for appointment in Appointment.all_appointments:
            if appointment.client_id == self.id:
                id_list.append(appointment.barber_id)
        for id in id_list:
            for barber in Barber.all_barbers:
                if barber.id == id:
                    barbers.append(barber)
        return barbers

    def get_details(self):
        print(self.id)
        print(self.fname)
        print(self.lname)
        print(self.phone)
        print(self.email)
