def find_best_discount(products):
    # Posortuj produkty według ceny
    sorted_products = sorted(products.items(), key=lambda x: x[1])
    sorted_products.reverse()

    print(sorted_products)
    
    # Dostępne opcje zniżek w kolejności rosnącej
    discounts = [0.0, 0.3, 0.55, 0.8]  # Dla pierwszych dwóch produktów nie ma zniżki

    if len(discounts) + 1 < len(sorted_products):
        inserts = len(sorted_products) - (len(discounts) + 1)
        while inserts > 1:
            discounts.insert(0, 0.0)
            inserts -= 1
    print(discounts)
    max_savings = 0
    best_option = None
    
    for i in range(0, len(sorted_products)):
        _, price = sorted_products[i]
        try:
            saving = price * discounts[i]
        except IndexError:
            saving = price - 0.01
        print(saving)
        # Jeśli oszczędność jest większa, zapisz wynik
        if saving > max_savings:
            max_savings = saving
            best_option = i
    
    return best_option + 1

# Przykład użycia
input_products = {'TV': 3000, 'sink': 350, 'computer': 4500, 'cup': 40, 'chair': 2000, 'disk': 5, 'room': 200000}
best_option = find_best_discount(input_products)
print("The best option is to get discount on the {}-th product.".format(best_option))