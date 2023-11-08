#Request User Input for Amount Borrowed for Mortgage
principle = float(input("Enter Original Mortgage Amount "))

#Request Length of Mortgage in Years
mortgage_length = int(input("Enter Number Of Years for Mortgage "))

#Enter Mortgage Intrest Rate
mortgage_rate = float(input("Enter the Mortgage Rate "))

#Change Mortgage Timeframe from Years to Months
mortgage_length =  mortgage_length * 12

#Change Intrest Rate to Decimal
mortgage_rate = mortgage_rate/100

#Calculate Monthly Rate
monthly_rate = mortgage_rate /12

#Calculate Monthly Payment
monthly_payment = (principle * monthly_rate * ((1 + monthly_rate)**mortgage_length)) / (((1 + monthly_rate)**mortgage_length) - 1)
monthly_payment = round(monthly_payment, 2)

#Output Amortization Schedule
count = 0
month = mortgage_length
intrest = 0

while(count < mortgage_length):
    intrest = round((principle * mortgage_rate /12),2)
    principle = round(principle - (monthly_payment - intrest),2)
    month = mortgage_length - count
    print("Payment Month: " + str(month) + "     Monthly Payment: $" + str(monthly_payment) +"     Current Principle: $" + str(principle) + "     Paid Intrest: $" + str(intrest))
    count = count + 1