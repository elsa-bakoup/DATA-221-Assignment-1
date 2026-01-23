threshold = 100
product = 1
current_multiplier = 1

while product <= threshold:
    product *= current_multiplier
    current_multiplier += 1

print(f"The final product is {product} and the integer that caused the product to exceed the threshold is {current_multiplier-1}.")