# Smart Shopping Bill Generator
# Supporting funtions 

def calculate_item_total(quantity,price):
    return quantity * price

def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        subtotal += item["amount"]

    return subtotal


def calculate_discount(subtotal, discount):
    return subtotal - discount


def calculate_gst(amount, gst_rate):
    return amount * gst_rate / 100


def calculate_final_total(amount, gst):
    return amount + gst


# Sample items
items = [
    {
        "name": "Notebook",
        "quantity": 2,
        "price": 50,
        "amount": calculate_item_total(2, 50)
    },
    {
        "name": "Pen",
        "quantity": 5,
        "price": 10,
        "amount": calculate_item_total(5, 10)
    }
]

subtotal = calculate_subtotal(items)
discount = 10
amount_after_discount = calculate_discount(subtotal, discount)

gst_rate = 12
gst = calculate_gst(amount_after_discount, gst_rate)

final_total = calculate_final_total(amount_after_discount ,gst )

print("Subtotal:", subtotal)
print("Discount:", discount)
print("GST:", gst)
print("Final Total:", final_total)
