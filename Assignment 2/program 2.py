number = int(input("enter the number of products :"))
dictionary = {}
for i in range (number):
    product_name = input(f"enter the name of product {i+1} :")
    price = int(input(f"enter the price of the product {i+1} :"))
    dictionary.update({product_name:price})

while(i):
    print("enter -1 to exit")
    search = input("enter the product :")
    if search in dictionary:
        print("price :",dictionary[search])
    if search == '-1':
        print("exiting...")
        exit(1)
    if not(search in dictionary):
        print("product not found ")
    