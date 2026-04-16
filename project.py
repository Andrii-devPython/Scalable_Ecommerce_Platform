def main():

    items = []
    my_cart = []
    add_product(items, "Laptop", 2000)
    add_product(items, "Phone", 1000)
    add_product(items, "Computer", 3000)
    show_products(items)
    add_to_cart(items, my_cart, 1, 6)
    add_to_cart(items, my_cart, 2, 4)
    show_cart(my_cart)
    remove_product(items, 1)
    show_products(items)
    total_value = calculate_total(my_cart)
    show_total(total_value)
    
    

def add_product(products, name, price):
    if not name:
        return False
    
    if price <= 0:
        return False
    
    product_id = len(products) + 1
    
    product = {
        "id" : product_id,
        "name" : name,
        "price" : price,
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
    for product in products :
        if product["id"] == product_id:
            item = {
                "product" : product,
                "quantity" : quantity,
                "product_id" : product_id
            }
            cart.append(item)
            return True
    return False
        

def show_cart(cart):
    print(cart)
    
def show_products(products):
    print(products)
    
def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["product"] ["price"] * item["quantity"]
        
    return total

def show_total(total):
    print(f"Total of your cart is : {total}!")
        

if __name__ == "__main__":
    main()