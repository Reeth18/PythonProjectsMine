#Bikes and Cars are to be parked in the Parking Area of the Mall
#Bikes are charged Rs 10/hr
#Cars are charged Rs 50/hr
#User Input 1: No of Bikes, No of Hours to be parked
#User Input 2: No of Cars, No of Hours to be parked
#Output: Total Earning for the Owner at the day
#Build a Program using Python

#Taking the No of Bikes as Input
noOfBikes = int(input("Enter the No of Bikes parked in a Day: "))
print(noOfBikes)

#Hours for which the Bikes are Parked
hoursOfBikesParking = int(input("Enter the Hours of Bike Parking: "))
print(hoursOfBikesParking)

#Given the rate of Bikes parking per hour
rateOfBikesParking = 10

#Output for Amount earned through Bikes Parking
amountByBikesParking = (noOfBikes * hoursOfBikesParking * rateOfBikesParking)

#Taking the No of Cars as Input
noOfCars = int(input("Enter the Number of Cars parked in a Day:"))
print(noOfCars)

#Hours for which the Cars are Parked
hoursOfCarsParking = int(input("Enter the Number of Hours of Car Parkig: "))
print(hoursOfCarsParking)

#Given the rate of Cars parking per hour
rateOfCarsParking = 50

#Output for Amount earned through Cars Parking
amountByCarsParking = (noOfCars * hoursOfCarsParking * rateOfCarsParking)

#Final Output of Total Amount
amountEarnedPerDay = (amountByBikesParking + amountByCarsParking)
print("Amount Earned in One Day is: ",amountEarnedPerDay)

#User Input 3: The Owner has received some payment
#Check whether the Auditing is successful or not
#IF not so then how much is the difference

#Payment Received by the Owner
paymentReceivedByOwner = int(input("Enter the Amount Received By The Owner: "))

#Auditing Amount matches with the Amount Received by the Owner
if (paymentReceivedByOwner == amountEarnedPerDay):
    print("Everything is OK!!")

#Auditing Amount not matches with the Amount Received by the Owner    
else:
    differenceOfAmount = (amountEarnedPerDay - paymentReceivedByOwner)
    print("The Difference of the Amount is: ", differenceOfAmount) #The Amount Difference Received by the Owner
