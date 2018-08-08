# Ex3.1
# Test Inputs "45 Hours" "rate = 10.50"
hrs = float(input("Enter Hours: "))
salary = float(input("Enter Rate: "))

if hrs > 40:

    extra_hrs = hrs - 40
        ot_diff = extra_hrs * ((1.5 * salary) - salary)
total_gross = ot_diff + (salary * hrs)

else:
    total_gross = salary * hrs


print("{}".format(total_gross))

""" 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly. """
