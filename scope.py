def add_tax(price):
    total = price * 1.13
    return total

# total only exists inside the function — this would error:
# print(total)  ->  name 'total' is not defined

# the returned value works, though:
print(add_tax(100))