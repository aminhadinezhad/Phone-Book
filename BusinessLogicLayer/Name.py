class Name:
    def __init__(self, firstName, lastName):
        self.FirstName = firstName
        self.LastName = lastName
        
    def nameConditions(self):
        nameList = [] 
        counter = 0 
        for char in self.FirstName or self.LastName:
            if "A" <= char <= "Z" or "a" <= char <= "z" or char == " ":
                nameList.append(char)
                counter = counter + 1
            else:
                return False 
        if counter != 0 and counter == len(nameList):
            return True
        else:
            return False