print("\nHello, welcome to the store!")

cart = []
while True:
    item = input("\nType in your item, then hit 'enter'. To delete an item, hit 'x'. To end shopping, hit 'q'. ").lower()
    if item != 'x' and item != 'q':
        cart.append(item)
        print("\nYour shopping cart: ")
        for i in cart:
            print("\t" + i.title() )
    elif item == 'x':
        delete = input("\nType in an item you would like to delete. ").lower()
        cart.remove(delete)
        print("\nYour shopping cart: ")
        for i in cart:
            print("\t" + i.title() )
    elif item == 'q':
        break
print("\nYour shopping cart: ")
for i in cart:
    print("\t" + i.title())