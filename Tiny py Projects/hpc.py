#Get the loan info from the user
loan = int(input("Please enter loan amount: "))
term = int(input("Please enter loan term: "))
rate = float(input("Please enter the loan rate: "))
down = int(input("Please enter down payment: "))

#Calculate loan 

months = term * 12

rate_monthly = rate / 100 / 12 

payment = (rate_monthly / (1- (1+ rate_monthly) ** (-months))) * (loan - down)

#Return monthly payment 

print("Your monthly payment is: " + "$" + str(round(payment,2)))
