class MobileNumber2:
    def __init__(self, mobileNumber2):
        self.MobileNumber2 = mobileNumber2
    
    def mobileNumber2Conditions(self):
        mobileNumber2List = []
        counter = 0
        for num in self.MobileNumber2:
            if "0" <= num <= "9":
                mobileNumber2List.append(num)
                counter = counter + 1 
            else:
                return False    
        if len(mobileNumber2List) == 11 and mobileNumber2List[0] == "0" and mobileNumber2List[1] == "9":
            return True
        elif counter == 0:
            return True
        else: 
            return False