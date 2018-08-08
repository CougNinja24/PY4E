

def computepay(h, r):
    gross_initial = h * r
    if h > 40:
        extra_pay = (h - 40) * ((r * 1.50) - r)
        return gross_initial + extra_pay
    else:
        return gross_initial


hours, rate = 40, 10.50
#hours = float(input("Hours Worked ? "))
#rate = float(input("Rate of Pay? "))

# run and print the results
grosspay = computepay(hours, rate)
#grosspaytest = computepay(45, 10.50)
print(grosspay)
