class PhoneNumber:
    def __init__(self, phoneNumber):
        self.PhoneNumber = phoneNumber
    
    def phoneNumberConditions(self):
        phoneNumberList = []
        counter = 0
        for num in self.PhoneNumber:
            if "0" <= num <= "9":
                phoneNumberList.append(num)
                counter = counter + 1 
            else:
                return False    
        if (len(phoneNumberList) == 8 and phoneNumberList[0] != "0") or (counter != 0 and len(phoneNumberList) == 11 and phoneNumberList[0] == "0"):
            return True
        else:
            return False