class Parking_Garage():
    tickets = ['Open'] * 100
    parking_spaces = ['Open'] * 100
    current_ticket = {"paid": False}

    def takeTicket(self):
        Parking_Garage.tickets.pop()
        Parking_Garage.parking_spaces.pop()


    def payForParking(self):
        payment = input("Please input payment amount: ")
        if payment != '':
            print("Your ticket is paid, please leave the garage within 15 minutes.")
            Parking_Garage.current_ticket['paid'] = True


    def leaveGarage(self):
        if Parking_Garage.current_ticket['paid'] == True:
            print("Thank you, have a nice day!")
        else:
            payment = input("Please input payment amount: ")
            if payment != '':
                print("Thank you, have a nice day!")
        Parking_Garage.tickets.append("Open")
        Parking_Garage.parking_spaces.append("Open")



garage = Parking_Garage()

def run():
    while True:
        question = input("Please enter: Take Ticket, Pay for Parking, or Leave Garage: ")
        if question.lower() == 'take ticket':
            garage.takeTicket()
        elif question.lower() == 'pay for parking':
            garage.payForParking()
        elif question.lower() == 'leave garage':
            garage.leaveGarage()
            break

run()