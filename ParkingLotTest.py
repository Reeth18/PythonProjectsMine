#Declare 5 Lists 
#no of hours
#bikes numbers
#entry time
#exit time

bikeNumbers = []
entryTimes = []
exitTimes = []


rateOfBikePayments = 20 #Payments per hour 
bikePayments = []
noOfHours = []
maxNumberOfBikes = 5
totalPayments = 0
ownerReceivedInHand = int(input("Enter the Amount Received in Cash: "))

for index in range (maxNumberOfBikes):
    userInput = input ("IS this an entry or exit or end of the day?")
    if (userInput == "Y"):
        #print("Enter the remarks: ")
        userInput2 = input("IS this an Entry or an Exit?")
        if (userInput2 == "Y"):
            print ("This is An Entry Case.")
            entryBikeNumber = input("Enter This Bike's Number: ")
            bikeNumbers.append(entryBikeNumber)
            
            entryTime = int(input("Enter the Entry Time of This Bike: "))
            entryTimes.append(entryTime)
            
            exitTimes.append(0)
            
            bikePayments.append(0)
            
            noOfHours.append(0)
        elif(userInput2 == "N"):
            print ("This is an Exit Case.")
            exitBikeNumber = input("Enter This Bike's Number: ")
            exitTime = int(input("Enter the Exit Time of this Bike: "))
            #exitTimes.append(exitTime)
            
            if(exitBikeNumber == entryBikeNumber):
                print (exitBikeNumber)
            index1 = bikeNumbers.index(exitBikeNumber)                

            exitTimes[index1] = exitTime
            print("Exit Time for this Bike is: ", exitBikeNumber, exitTimes[index1])
            
            noOfHours[index1] = exitTime - entryTimes[index1]
            print("Hours until which this Bike was Parked: ",noOfHours[index1]) 
            
            bikePayments[index1] = rateOfBikePayments * noOfHours[index1]
            print("Parking Charge of this Bike: ", bikeNumbers[index1], bikePayments[index1])   
            
            totalPayments += bikePayments[index1]
            
    elif (userInput == "N"):
        print ("End of the Day Case..........")
        
        print("Total Earnings per day: ", totalPayments)
        
        if(ownerReceivedInHand == totalPayments):
            print("Owner is Satisfied")
        else:
            differenceAmount = totalPayments - ownerReceivedInHand
            
        break
        

print(bikeNumbers)
print(entryTimes)
print(exitTimes)
print(noOfHours)
print(bikePayments)
print("The Difference in Amount Received by the Owner is: ",differenceAmount)