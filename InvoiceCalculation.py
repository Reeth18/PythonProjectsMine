'''Problem Statement: Create a command-line program in Python to Calculate the total invoice amount for the below purchases - 

Book - Introduction to Python Programming: Rs 499.00
Book - Python Libraries Cookbook: Rs. 855.00
Book - Data Science in Python: Rs. 645.00


Taxes and additional charges are described as details - 

GST: 12%
Delivery Charges: Rs. 250.00'''


Books = ["Introduction to Python Programming", "Python Libraries Cookbook", "Data Science in Python"]
Price = [499, 855, 645]
GST = 12
deliveryCharges = 250.00
totalInvoiceAmount = 0
amountWithoutExtraCharges = 0

#Calulating the cost of the books without taxes and other charges
for index in range(0, len(Price)):
    amountWithoutExtraCharges += Price[index]
print ("The Amount of Books without Extra Charges is: ",amountWithoutExtraCharges)

#Calulating the cost of the books with taxes and delivery charges
totalInvoiceAmount = amountWithoutExtraCharges + (amountWithoutExtraCharges * (GST/100)) + deliveryCharges
print ("The Invoice Amount of the Books purchased is: ", totalInvoiceAmount)