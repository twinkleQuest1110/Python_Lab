
# Project 3: Smart Shopping Cart Optimizer

print("===== SMART SHOPPING CART =====")

# Taking customer details
customer_name = input("Enter customer name: ")
budget = float(input("Enter your budget: "))

# Taking item details
n = int(input("Enter number of items: "))

subtotal = 0

for i in range(n):
    print(f"\nItem {i + 1}")

    item_name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    item_total = price * quantity
    subtotal += item_total

    print(item_name, "=", item_total)

# Discount and delivery details
discount_percentage = float(input("\nEnter discount percentage: "))
minimum_purchase = float(input("Enter minimum purchase for discount: "))

delivery_limit = float(input("Enter minimum purchase for free delivery: "))
delivery_charge = float(input("Enter delivery charge: "))

# Calculate discount
discount = 0

if subtotal >= minimum_purchase:
    discount = (subtotal * discount_percentage) / 100

# Calculate delivery charges
if subtotal >= delivery_limit:
    delivery_fee = 0
else:
    delivery_fee = delivery_charge

# Calculate final bill
final_amount = subtotal - discount + delivery_fee

# Compare bill with budget
difference = budget - final_amount

# Display bill
print("\n========== FINAL BILL ==========")
print("Customer Name:", customer_name)
print("Subtotal: Rs.", subtotal)
print("Discount: Rs.", discount)
print("Delivery Fee: Rs.", delivery_fee)
print("--------------------------------")
print("Final Amount: Rs.", final_amount)

if difference >= 0:
    print("Remaining Budget: Rs.", difference)
    print("Status: Within Budget")
else:
    print("Extra Amount Required: Rs.", abs(difference))
    print("Status: Budget Exceeded")

print("================================")
