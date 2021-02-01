```
shopping_dict = {
    "warzywniak": ["marchew", "seler", "rukola"],
    "piekarnia": ["bułki", "chleb", "pączek"]
}

print("Lista Zakupów:")
licznik = 0

for shop in shopping_dict.keys():
    value =[]
    for produkt in shopping_dict[shop]:
        value.append(produkt.capitalize())
        licznik = licznik + 1
    print(f"Idę do {shop.capitalize()}, kupuję tu następujące rzeczy: {value}") 
#print(type(shopping_dict[shop]))
#print(type(shop))
print(f"W sumie kupuję {licznik} produktów.")