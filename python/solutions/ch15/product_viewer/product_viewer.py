from objects import Product, Media, Book, Movie, Album

def show_products(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print(str(i+1) + ".", product.getDescription())
    print()

def show_product(product):
    print("PRODUCT DATA")
    print("Name:            ", product.name)
    if isinstance(product, Book):
        print("Author:          ", product.author)
    if isinstance(product, Movie):
        print("Year:            ", product.year)
    if isinstance(product, Album):
        print("Artist:          ", product.artist)
    if isinstance(product, Media):
        print("Format:          ", product.format)        
    print("Discount price:   {:.2f}".format(product.getDiscountPrice()))
    print()

def main():
    print("The Product Viewer program")
    print()
    
    # a tuple of Product objects
    products = (Product('Stanley 13 Ounce Wood Hammer', 12.99, 62),
                Book("The Big Short", 15.95, 34, "Michael Lewis", "Paperback"),
                Movie("The Holy Grail", 14.99, 68, 1975, "DVD"),
                Album("Rubber Soul", 10.00, 0, "The Beatles", "CD"))
    show_products(products)

    while True:
        number = int(input("Enter product number: "))
        print()
    
        product = products[number-1]
        show_product(product)

        choice = input("Continue? (y/n): ")
        print()
        if choice != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
