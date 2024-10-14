class MobileNumber1:
    def __init__(self, mobileNumber1):
        self.MobileNumber1 = mobileNumber1
    
    def mobileNumber1Conditions(self):
        mobileNumber1List = []
        counter = 0
        for num in self.MobileNumber1:
            if "0" <= num <= "9":
                mobileNumber1List.append(num)
                counter = counter + 1 
            else:
                return False    
        if len(mobileNumber1List) == 11 and mobileNumber1List[0] == "0" and mobileNumber1List[1] == "9":
            return True
        else:
            return False