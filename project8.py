customer = input("Enter customer name: ")
product = input("Enter product name: ")

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 5000:
    discount = total * 0.20
elif total >= 3000:
    discount = total * 0.10
elif total >= 1000:
    discount = total * 0.05
else:
    discount = 0

final_amount = total - discount

print("\n----- SHOPPING BILL -----")
print("Customer:", customer)
print("Product:", product)
print("Quantity:", quantity)
print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)