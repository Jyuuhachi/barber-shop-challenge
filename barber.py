from appointment import Appointment

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