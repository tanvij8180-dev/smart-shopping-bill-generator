print("=" * 50)
print("        🛒 SMARTMART SHOPPING SYSTEM")
print("        SMART BILL GENERATOR")
print("=" * 50)

customer_name = input("Enter customer name: ")

items = []
subtotal = 0

while True:
    print("\n--- ADD PRODUCT ---")

    item = input("Enter item name (or 'done' to finish): ")

    if item.lower() == "done":
        break

    price = float(input("Enter price: ₹"))
    quantity = int(input("Enter quantity: "))

    item_total = price * quantity
    subtotal += item_total

    items.append((item, price, quantity, item_total))

    print("✓ Product added successfully!")
    print("Item total: ₹", item_total)

# Discount calculation
if subtotal >= 2000:
    discount_rate = 0.15
elif subtotal >= 1000:
    discount_rate = 0.10
else:
    discount_rate = 0.05

discount = subtotal * discount_rate
after_discount = subtotal - discount

# GST calculation
gst_rate = 0.18
gst = after_discount * gst_rate

final_amount = after_discount + gst

# Final bill
print("\n")
print("=" * 50)
print("                 FINAL BILL")
print("=" * 50)

print("Customer:", customer_name)
print("-" * 50)

print(f"{'Item':<15}{'Qty':<8}{'Price':<10}{'Total':<10}")
print("-" * 50)

for item, price, quantity, item_total in items:
    print(f"{item:<15}{quantity:<8}₹{price:<9.2f}₹{item_total:<9.2f}")

print("-" * 50)

print(f"Subtotal:              ₹{subtotal:.2f}")
print(f"Discount:              ₹{discount:.2f}")
print(f"GST (18%):             ₹{gst:.2f}")
print("-" * 50)
print(f"FINAL AMOUNT:          ₹{final_amount:.2f}")
print("=" * 50)

print("       Thank you for shopping with SmartMart!")
print("=" * 50)
