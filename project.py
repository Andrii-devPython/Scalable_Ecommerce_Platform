def main():
    
    products = []
    cart = []
    add_product(products, "Laptop", 2000)
    add_product(products, "Phone", 1000)
    add_product(products, "Computer", 3000)
    
    add_to_cart(products, cart, 1, 6)
    add_to_cart(products, cart, 2, 4)
    
    
    
    while True:
        print("\nMenu:")
        print("1 - Show products")
        print("2 - Add to cart")
        print("3 - Remove from cart")
        print("4 - Show cart")
        print("5 - Show total")
        print("0 - Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            show_products(products)
        elif choice == "2":
            product_id = int(input("Enter product id:"))
            quantity = int(input("Enter quntity:"))
            add_to_cart(products, cart, product_id, quantity)
        elif choice == "3":
            product_id = int(input("Enter product id:"))
            remove_from_cart(cart, product_id)
        elif choice == "4":
            show_cart(cart)
        elif choice == "5":
            total_value = calculate_total(cart)
            show_total(total_value)
        elif choice == "0":
            break
        else:
            print("Wrong number. Please choose from 0 to 5")
       
    
    

def add_product(products, name, price):
    if not name:
        return False
    
    if price <= 0:
        return False
    
    product_id = len(products) + 1
    
    product = {
        "id": product_id,
        "name": name,
        "price": price,
    }
    
    products.append(product)
        
def remove_product(products, product_id):
    if product_id < 1:
        return False
    
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return True
    return False

def add_to_cart(products, cart, product_id, quantity):
    if quantity <= 0:
        return False
    if product_id < 1:
        return False
    for product in products:
        if product["id"] == product_id:
            item = {
                "product": product,
                "quantity": quantity
            }
            cart.append(item)
            return True
    return False

def remove_from_cart(cart, product_id):
    if product_id < 1: 
        return False
    
    for item in cart:
        if item["product"]["id"] == product_id:
            cart.remove(item)
            return True
    return False

        

def show_cart(cart):
    for item in cart:
        print(f"{item['product']['name']} x{item['quantity']} = {item['quantity']*item['product']['price']}")
    
def show_products(products):
    for product in products:
        print(f"ID: {product['id']} | {product['name']} | {product['price']}")
    
def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["product"]["price"] * item["quantity"]
        
    return total

def show_total(total):
    print(f"Total: {total}!")
        

if __name__ == "__main__":
    main()