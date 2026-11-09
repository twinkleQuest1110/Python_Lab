# Smart Electricity Bill Estimator
# input from the user
name = input("Enter consumer name: ")
previous_reading = int(input("Enter previous meter reading: "))
current_reading = int(input("Enter current meter reading: "))
rate = float(input("Enter price per unit (₹): "))

if current_reading < previous_reading:
    print("Error: Current reading cannot be less than previous reading.")

else:
    units = current_reading - previous_reading
    bill = units * rate
    average = units / 30

    print("\n----- Electricity Bill -----")
    print("Consumer Name:", name)
    print("Previous Reading:", previous_reading)
    print("Current Reading:", current_reading)
    print("Units Consumed:", units)
    print("Price Per Unit: ₹{:.2f}".format(rate))
    print("Energy Charge: ₹",bill)
    print("Average Daily Consumption: {:.2f} units".format(average))
