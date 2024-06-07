products = {
    "product1":{
        "brand":"A",
        "price":5.40
    },
    "product2":{
        "brand":"B",
        "price":7.35
    },

    "product3":{
        "brand":"C",
        "price":2.24
    }
}
print("======= Welcome to our Catalog =======")


for product, data in products.items():
    print(f"Product: {product}")
    #print("-->Outer Loop")    

    for category,value in data.items():
     #   print("-->Nested Loop")
        print(f"{category.capitalize()}: {value}")
    print()





