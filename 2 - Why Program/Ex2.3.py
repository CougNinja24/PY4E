# This first line is provided for you

hrs = input("Enter Hours:")
hrs_rate = input("Hourly pay rate? : ")

# put the inputs into strings
gross_pay = float(hrs) * float(hrs_rate)

assert type(gross_pay) == float, "Input cannot be a string"

print("Pay is expected to be : {}".format(gross_pay))