import csv
from BusinessLogicLayer.Name import Name
from BusinessLogicLayer.PhoneNumber import PhoneNumber
from BusinessLogicLayer.MobileNumber1 import MobileNumber1
from BusinessLogicLayer.MobileNumber2 import MobileNumber2
from BusinessLogicLayer.PostalCode import PostalCode

myFile = open("PhoneBook.csv", mode="w", newline="")
write = csv.writer(myFile)
write.writerow(["First Name", "Last Name", "Phone Number", "Mobile Number1", "Mobile Number2", "Address", "Postal Code"])

repeatOperation = "yes"
while repeatOperation == "yes":
    nameConditionsOutput = False
    while nameConditionsOutput == False:
        firstName = input("First Name*: ")
        nameObject = Name(firstName=firstName, lastName="")
        nameConditionsOutput = nameObject.nameConditions()
        if nameConditionsOutput == False:
            print("Please enter a valid First Name (Contains only letters and space character).")
        
    nameConditionsOutput = False
    while nameConditionsOutput == False:
        lastName = input("Last Name*: ")
        nameObject = Name(firstName="", lastName=lastName)
        nameConditionsOutput = nameObject.nameConditions()
        if nameConditionsOutput == False:
            print("Please enter a valid Last Name (Contains only letters and space character).")
    
    phoneNumberConditionsOutput = False
    while phoneNumberConditionsOutput == False:
        phoneNumber = input("Phone Number*: ")
        phoneNumberObject = PhoneNumber(phoneNumber=phoneNumber)
        phoneNumberConditionsOutput = phoneNumberObject.phoneNumberConditions()
        if phoneNumberConditionsOutput == False:
            print("Please enter a valid Phone Number (Contains only numeric characters with a length of 8 or 11 characters).")
    
    mobileNumber1ConditionsOutput = False
    while mobileNumber1ConditionsOutput == False:
        mobileNumber1 = input("Mobile Number1*: ")
        mobileNumber1Object = MobileNumber1(mobileNumber1=mobileNumber1)
        mobileNumber1ConditionsOutput = mobileNumber1Object.mobileNumber1Conditions()
        if mobileNumber1ConditionsOutput == False:
            print("Please enter a valid Mobile Number (Contains only numeric characters with a length of 11 characters and must start with '09').")
    
    mobileNumber2ConditionsOutput = False
    while mobileNumber2ConditionsOutput == False:
        mobileNumber2 = input("Mobile Number2: ")
        mobileNumber2Object = MobileNumber2(mobileNumber2=mobileNumber2)
        mobileNumber2ConditionsOutput = mobileNumber2Object.mobileNumber2Conditions()
        if mobileNumber2ConditionsOutput == False:
            print("Please enter a valid Mobile Number (Contains only numeric characters with a length of 11 characters and must start with '09').")
    
    address = input("Address: ")
    
    postalConditionsOutput = False
    while postalConditionsOutput == False:
        postalCode = input("Postal Code: ")
        postalCodeObject = PostalCode(postalCode=postalCode)
        postalConditionsOutput = postalCodeObject.postalConditions()
        if postalConditionsOutput == False:
            print("Please enter a valid Postal Code (Contains only numeric characters with a length of 10 characters).")
    
    write.writerows([
        [firstName, lastName, phoneNumber, mobileNumber1, mobileNumber2, address, postalCode]
    ])
    
    repeatOperation = input("Do you want to save another person information? ")
    if repeatOperation == "no":
        print("Your information has been successfully registered.")