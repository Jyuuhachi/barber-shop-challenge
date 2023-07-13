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
        self.date = date
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
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if type(value) == int or type(value) == float:
            if value > 0:
                self._price = value
            else:
                raise ValueError("price must be at least $1")
        else:
            raise TypeError("price must be a integer or decimal number")



    @classmethod
    def get_barbers_with_appointments(cls):
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
    
    @classmethod
    def get_clients_with_appointments(cls):
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
    
    @lname.setter
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

class Barber:
    id = 1
    all_barbers = []

    def __init__(self, fname, lname, date_hired, phone):
        self.id = Barber.id
        self.fname = fname
        self.lname = lname
        self.date_hired = date_hired
        self.phone = phone
        Barber.id+=1
        Barber.all_barbers.append(self)

    def __str__(self):
        return f"Barber #{self.id} first name: {self.fname} last name: {self.lname} date hired: {self.date_hired} phone number: {self.phone}"

    def get_appointments(self):
        appointment_list = Appointment.get_appointments_by_id(self.id, False)
        print(appointment_list)

    def get_clients_by_hair_cut(self, hair_cut):
        appointments = []
        for appointment in Appointment.all_appointments:
            if appointment.cut_style == hair_cut:
                appointments.append(appointment)
        return appointments

    def get_appointments_by_date(self, search):
        appointments = []
        for appointment in Appointment.all_appointments:
            if appointment.date == search:
                appointments.append(appointment)
        return appointments


    def get_details(self):
        print(self.id)
        print(self.fname)
        print(self.lname)
        print(self.date_hired)
        print(self.phone)