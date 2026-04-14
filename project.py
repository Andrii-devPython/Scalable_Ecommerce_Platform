def main():
    products = []
    add_product(products, "Laptop", 2000)
    print(products)

def add_product(products, name, price):
    product_id = len(products) + 1
    
    product = {
        "id" : product_id,
        "name" : name,
        "price" : price,
    }
    
    products.append(product)
        
def remove_product(products, product_id):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return True
    return False

def add_to_cart(products, cart, product_id):
    pass

def show_cart(cart):
    pass

if __name__ == "__main__":
    main()