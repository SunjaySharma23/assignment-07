# Module 7 Assignment: Organizing Data with Lists and Tuples
# TechElectronics Inventory Tracking System

# Welcome message
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
# Each product is a tuple: (product_id, name, price, quantity, category)
# Create at least 5 product tuples
# Example: product1 = ("P001", "Smartphone X", 799.99, 10, "Mobile Phones")
product1 = ("P001", "Smartphone X", 799.99, 12, "Mobile Phones")
product2 = ("P002", "Laptop Pro", 1299.99, 8, "Laptops")
product3 = ("P003", "Wireless Earbuds", 149.99, 20, "Audio")
product4 = ("P004", "Tablet Air", 799.99, 12, "Tablets")
product5 = ("P005", "Gaming Laptop", 1599.99, 3, "Laptops")
# TODO 2: Create an inventory list containing all product tuples
# Example: inventory = [product1, product2, ...]
inventory = [product1, product2, product3, product4, product5]
# TODO 3: Display all products
# Use a print statement to show each product in the inventory
print("\nCurrent Inventory:")
print("-" * 60)
# Add your code here to display all products
for product in inventory:
    print(
        f"ID: {product[0]}, Name {product[1]}, Price: ${product[2]:.2f},"
        f"Quantity: {product[3]}, Category: {product[4]}"
        )
# TODO 4: Access specific elements
# Use indexing to:
# - Get and display the first product (store in first_product)
# - Get and display the last product (store in last_product)
# - Get and display the third product's name only (store in third_product_name)
# - Get and display the second product's price and quantity (store in second_price, second_quantity)
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]

print("\n\nAccessing Specific Products:")
print("-" * 60)
# Add your code here
print(f"First product: {first_product}")
print(f"Last product: {last_product}")
print(f"Third product name: {third_product_name}")
print(f"Second product price: {second_price:.2f}")
print(f"Second product quantity: {second_quantity}")
# TODO 5: Use slicing to get subsets
# - Get and display the first 3 products (store in first_three)
# - Get and display products from index 2 to 4 (store in middle_products)
# - Get and display all products except the first one (store in all_except_first)
first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)
print(f"First three products: {first_three}")
print(f"Products from index 2 to 4: {middle_products}")
print(f"All products except first: {all_except_first}")
# Add your code here

# TODO 6: Add new products to inventory
# Create 2 new product tuples and add them to the inventory list
# Use the .append() method
new_product1 = ("P006", "Bluetooth Speaker", 89.99, 15, "Audio")
new_product2 = ("P007", "Budget Smartphone", 299.99, 4, "Mobile Phones")
        
inventory.append(new_product1)
inventory.append(new_product2)

print("\n\nAdding New Products:")
print("-" * 60)
# Add your code here
print("Added products:")
print(new_product1)
print(new_product2)
        
print("\nUpdated Inventory:")
for product in inventory:
        print(
            f"ID: {product[0]}, Name: {product[1]}, Price: ${product[2]:.2f},"
            f"Quantity: {product[3]}, Category: {product[4]}"
            )
# TODO 7: Remove a product
# Remove the product at index 2 using .pop()
# Display what was removed and show the updated inventory
removed_product = inventory.pop(2)

print("\n\nRemoving a Product:")
print("-" * 60)
# Add your code here
print(f"Removed product: {removed_product}")

print("\nUpdated inventory:")
for product in inventory:
        print(
            f"ID: {product[0]}, Name: {product[1]}, Price: ${product[2]:.2f},"
            f"Quantity: {product[3]}, Category: {product[4]}"
        )

# TODO 8: Insert a product at a specific position
# Create a new product tuple and insert it at index 1
# Use the .insert() method
inserted_product = ("P008", "Noise Cancelling Headphones", 249.99, 7, "Audio")
inventory.insert(1, inserted_product)

print("\n\nInserting a Product:")
print("-" * 60)
# Add your code here
print(f"Inserted product at index 1: {inserted_product}")
        
print("\nUpdated Inventory:")
for product in inventory:
    print(
        f"ID: {product[0]}, Name: {product[1]}, Price: ${product[2]:.2f},"
            f"Quantity: {product[3]}, Category: {product[4]}"
        )

# REDO TODO 4 and 5: Please recalculate all access and sliced variables from todos 4 and 5, as the code grader checks these variables against the final state of the inventory.
# Add your code here
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]
        
first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]
# TODO 9: Create category lists
# Create separate lists for different categories
# For example: mobile_phones = [], laptops = [], audio = []
# Go through your inventory and add products to appropriate category lists
mobile_phones = []
laptops = []
audio = []
tablets = []
    
# Add your code here
for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_phones.append(product)
    elif product[4] == "Laptops":
        laptops.append(product)
    elif product[4] == "Audio":
        audio.append(product)
    elif product[4] == "Tablets":
        tablets.append(product)

print("\n\nProducts by Category:")
print("-" * 60)
print(f"Mobile Phones: {mobile_phones}")
print(f"Mobile Phones: {mobile_phones}")
print(f"Laptops: {laptops}")
print(f"Audio: {audio}")
print(f"Tablets: {tablets}")
# TODO 10: Calculate inventory statistics
# Calculate and display:
# - Total number of products in inventory (store in total_products)
# - Total value of all products (price * quantity for each product) (store in total_value)
# - List of all product names (store in product_names)
# - List of all product prices (store in product_prices)
total_products = len(inventory)
total_value = 0
        
for product in inventory:
        total_value += product[2] * product[3]
        
product_names = [product[1] for product in inventory]
product_prices = [product[2] for product in inventory]

print("\n\nInventory Statistics:")
print("-" * 60)
# Add your code here
print(f"Total number of products: {total_products}")
print(f"Total inventory value: {total_value:.2f}")
print(f"Product names: {product_names}")
print(f"Product prices: {product_prices}")
# TODO 11: Find expensive products using list comprehension
# Use a list comprehension to create a list of products that cost more than $500
# Store in variable: expensive_products
# Display these expensive products
# Hint: expensive_products = [product for product in inventory if product[2] > 500]
expensive_products = [product for product in inventory if product[2] > 500]

print("\n\nExpensive Products (> $500):")
print("-" * 60)
# Add your code here
for product in expensive_products:
        print(product)
# TODO 12: Low stock alert using list comprehension
# Use a list comprehension to create a list of products with quantity less than 5
# Store in variable: low_stock
# Display these low stock products
# Hint: low_stock = [product for product in inventory if product[3] < 5]
low_stock = [product for product in inventory if product[3] < 5]

print("\n\nLow Stock Alert (< 5 units):")
print("-" * 60)

# Add your code here
for product in low_stock:
        print(product)
# TODO 13: Create price list using list comprehension
# Use a list comprehension to create a list of all product prices (store in original_prices)
# Then use another comprehension to apply a 10% discount to all prices (store in discounted_prices)
# Display both the original and discounted price lists
original_prices = [product[2] for product in inventory]
discounted_prices = [round(price * 0.90, 2) for price in original_prices]

print("\n\nPrice Lists:")
print("-" * 60)
# Add your code here
print(f"Original prices: {original_prices}")
print(f"Discounted prices (10% off): {discounted_prices}")
# TODO 14: Product name formatting using list comprehension
# Use a list comprehension to create a list of all product names in uppercase (store in uppercase_names)
# Then create another list with product codes (first 3 chars of ID + first 3 chars of name) (store in product_codes)
# Display both lists
uppercase_names = [product[1].upper() for product in inventory]
product_codes = [product[0][:3] + product[1][:3].upper() for product in inventory]

print("\n\nFormatted Product Names:")
print("-" * 60)
# Add your code here
print(f"Uppercase product names: {uppercase_names}")
print(f"Product codes: {product_codes}")
# TODO 15: Using Loops to Process Inventory
# Use a for loop to:
# - Count how many products are in the "Mobile Phones" category (store in mobile_count)
# - Calculate the total value of all "Laptops" in stock (store in laptop_value)
# - Find the most expensive product in the inventory (store in most_expensive)
mobile_count = 0
laptop_value = 0
most_expensive = inventory[0]
                 
for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_count += 1
                 
    if product[4] == "Laptops":
        laptop_value += product[2] * product[3]
                 
    if product[2] > most_expensive[2]:
        most_expensive = product

print("\n\nLoop-Based Analysis:")
print("-" * 60)
# Add your code here
print(f"Number of Mobile Phones products: {mobile_count}")
print(f"Total value of all Laptops in stock: {laptop_value:.2f}")
print(f"Most expensive product: {most_expensive}")
# TODO 16: Using Conditionals with Lists
# Use loops and conditionals to:
# - Create a list of products that need restocking (quantity < 5) (store in restock_list)
# - Create a list of high-value items (price > $500 AND quantity > 10) (store in high_value_items)
# - Count products in different price ranges: under $100, $100-$500, over $500 (store counts in price_ranges dictionary)
restock_list = []
high_value_items = []
price_ranges = {
    "under_100": 0,
    "100_to_500": 0,
    "over_500": 0
    }
                 
for product in inventory:
    if product[3] < 5:
        restock_list.append(product)
                 
    if product[2] > 500 and product[3] > 10:
        high_value_items.append(product)
                 
    if product[2] < 100:
        price_ranges["under_100"] += 1
    elif 100 <= product[2] <= 500:
        price_ranges["100_to_500"] += 1
    else:
        price_ranges["over_500"] += 1

print("\n\nConditional Analysis:")
print("-" * 60)
# Add your code here
print(f"Products needing restocking: {restock_list}")
print(f"High-vale items: {high_value_items}")
print(f"Price ranges: {price_ranges}")
# TODO 17: Define and Use Functions
# Define these functions:
# - calculate_product_value(product): returns price * quantity for a product tuple
# - find_products_by_category(inventory, category): returns list of products in given category
# - apply_discount(inventory, discount_percent): returns new inventory with discounted prices
# Then use these functions to:
# - Calculate total inventory value
# - Find all "Audio" products
# - Create a new inventory with 15% discount applied
def calculate_product_value(product):
    return product[2] * product[3]
                 
def find_products_by_category(inventory, category):
    return [product for product in inventory if product[4] == category]
                 
def apply_discount(inventory, discount_percent):
    discounted_inventory = []
    for product in inventory:
        discounted_price = round(product[2] * (1 - discount_percent / 100), 2)
        discounted_product = (
            product[0],
            product[1],
            discounted_price,
            product[3],
            product[4]
        )
        discounted_inventory.append(discounted_product)
    return discounted_inventory
                 
function_total_value = 0
for product in inventory:
    function_total_value += calculate_product_value(product)
                 
audio_products = find_products_by_category(inventory, "Audio")
discounted_inventory_15 = apply_discount(inventory, 15)

print("\n\nFunction-Based Operations:")
print("-" * 60)
# Add your code here
print(f"Total inventory value using function: {function_total_value:.2f}")
print(f"Audio products: {audio_products}")
print(f"Inventory with 15% discount: {discounted_inventory_15}")
# TODO 18: Combine Loops, Functions, and List Operations
# Create a function generate_inventory_report(inventory) that:
# - Uses loops to analyze the inventory
# - Returns a dictionary with:
#   - 'total_products': total number of products
#   - 'total_value': sum of all (price * quantity)
#   - 'categories': list of unique categories
#   - 'low_stock': list of products with quantity < 5
#   - 'average_price': average price of all products
# Call the function and display the report
def generate_inventory_report(inventory):
    total_products_report = len(inventory)
    total_value_report = 0
    categories = []
    low_stock_report = []
    total_price = 0
                 
    for product in inventory:
        total_value_report += product[2] * product[3]
        total_price += product[2]
                 
    if product[4] not in categories:
                categories.append(product[4])
                 
    if product[3] < 5:
                low_stock_report.append(product)
                 
    average_price = total_price / len(inventory)
                 
    report = {
        "total_products": total_products_report,
        "total_value": total_value_report,
        "categories": categories,
        "low_stock": low_stock_report,
        "average_price": average_price,
    }
    
    return report

inventory_report = generate_inventory_report(inventory)

print("\n\nComprehensive Inventory Report:")
print("-" * 60)
# Add your code here
for key, value in inventory_report.items():
    if key == "total_value" or key == "average_price":
        print(f"{key}: ${value:.2f}")
    else:
        print(f"{key}: {value}")
# TODO When calculating laptop_value, make sure to use the category name exactly "Laptops" (plural).