# name = "Ada"
# age = 30
# city = "Berlin"
# print(f"{name} is {age} years old and lives in {city}.")

def area_of_rectangle(width, height):
    area = width * height
    return area
result1 = area_of_rectangle(4, 5)
result2 = area_of_rectangle(3, 7)

print(f"A 4 by 5 rectangle has an area of {result1}.")
print(f"A 3 by 7 rectangle has an area of {result2}.")
print(f"Together they cover {result1 + result2} square meters.")