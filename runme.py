from ugly import Barber
from ugly import Appointment
from ugly import Client

new_barber = Barber("bob", "smith", "02/26/1990", "555-555-5555")
new_barber2 = Barber("vince", "powell", "03/25/1905", "555-525-5515")
new_barber3 = Barber("lionel", "reeds", "03/23/1967", "555-525-5575")
new_client = Client("dan", "johnson", "555-565-5455", "junk@testdata.net")
new_client2 = Client("jane", "mary", "555-545-5255", "junk@testdata.com")
new_client3 = Client("lelouche", "lamperouge", "555-555-5595", "junk@testdata.org")
new_appointment = new_client3.book_appointment(new_barber.id, "09/05/2023", "buzz cut", 49)
new_appointment2 = new_client3.book_appointment(new_barber2.id, "09/05/2023", "shape up", 15.34)
new_appointment3 = new_client2.book_appointment(new_barber3.id, "09/25/2023", "buzz cut", 34.63)


print(f"{new_barber}")
print(f"{new_barber2}")
print(f"{new_barber3}")
print(f"{new_client}")
print(f"{new_client2}")
print(f"{new_client3}")
booked_barbers = Appointment.get_barbers_with_appointments()
booked_clients = Appointment.get_clients_with_appointments()
print("booked barbers:")
for barber in booked_barbers:
    print(barber)
print("booked clients:")
for client in booked_clients:
    print(client)
