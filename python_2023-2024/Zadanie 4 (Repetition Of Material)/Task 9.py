#9.  Trzy najlepsze produkty w sklepie 

produkty = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

# Sortowanie produktów według cen w malejącej kolejności
posortowane_produkty = sorted(produkty.items(), key=lambda x: x[1], reverse=True)

# Wybieranie trzech najlepszych produktów
najlepsze_produkty = posortowane_produkty[:3]

# Wyświetlanie wyniku
print("Trzy najlepsze produkty:")
for produkt in najlepsze_produkty:
    print(f"{produkt[0]}: {produkt[1]}")