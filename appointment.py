from client import Client
from barber import Barber

class Appointment:

    id = 1
    all_appointments = []

    @classmethod
    def get_appointments_by_id(cls, search, barber_check):
        appointment_list = []
        if barber_check == True:
            for appointment in cls.all_appointments:
                if appointment.barber_id == search:
                    appointment_list.append(appointment)
        if barber_check == False:
            for appointment in cls.all_appointments:
                if appointment.client_id == search:
                    appointment_list.append(appointment)
        return appointment_list

    def __init__(self, barber_id, client_id, date, cut_style, price):
        self.id = Appointment.id
        self.barber_id = barber_id
        self.client_id = client_id
        self._date = date
        self.cut_style = cut_style
        self.price = price
        Appointment.id+=1
        Appointment.all_appointments.append(self)

    def __str__(self):
        return f"Appointment #{self.id} clientID: {self.client_id} barberID: {self.barber_id} date: {self.date} haircut style: {self.cut_style} price: {self.price}"

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if type(value) == str:
            self._date = value
        else:
            raise TypeError("date must be a string")


    def get_barbers_with_appointments(self):
        barber_ids = []
        barbers = []
        for appointment in Appointment.all_appointments:
            if appointment.barber_id not in barber_ids:
                barber_ids.append(appointment.barber_id)
        for barber in Barber.all_barbers:
            for id in barber_ids:
                if barber.id == id:
                    barbers.append(barber)
        return barbers

    def get_clients_with_appointments(self):
        client_ids = []
        clients = []
        for appointment in Appointment.all_appointments:
            if appointment.client_id not in client_ids:
                client_ids.append(appointment.client_id)
        for client in Client.all_clients:
            for id in client_ids:
                if client.id == id:
                    clients.append(client)
        return clients

    def get_details(self):
        print(self.barber_id)
        print(self.client_id)
        print(self.date)
        print(self.cut_style)
        print(self.price)
