class PostalCode:
    def __init__(self, postalCode):
        self.PostalCode = postalCode
    
    def postalConditions(self):
        postalCodeList = []
        counter = 0
        for num in self.PostalCode:
            if "0" <= num <= "9":
                postalCodeList.append(num)
                counter = counter + 1 
            else:
                return False    
        if len(postalCodeList) == 10:
            return True
        elif counter == 0:
            return True
        else: 
            return False