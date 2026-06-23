colors = ["red", "blue"]
obj = enumerate(colors)
print(list(obj))

# Desafío 
products = ["T-Shirt", "Jeans", "Hoodie"]
stock = [10, 15, 8]
prices = [19.99, 49.99, 39.99]

info_store = list(zip(products, stock, prices))
print("\n Inventory Information:")
for index,(pdt,stk,prc) in enumerate(info_store,1):
    print(f"Item N°{index}: {pdt}, price: ${prc}")
print("\n 3-day Flash-sale")
for day in range(3):
    for index, (pdt,stk,prc) in enumerate(info_store):
        reduction_amount = index + 1
        new_stk = stk - reduction_amount
        info_store[index] = (pdt, new_stk, prc)
print("--- Final Stock After 3 Days ---")
for index, (product, stk, price) in enumerate(info_store, start=1):
    print(f"{product} remaining stock: {stk}")