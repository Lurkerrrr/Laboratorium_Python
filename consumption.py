x = float(input("Введіть відстань автомобіля: "))
y = float(input("Введіть споживання палива на 100 км: "))
consumption = (x * y) / 100
price = (x * y * 6.5) / 100
print("Орієнтовна витрата палива: ", consumption)
print("Орієнтована витрата на проїзд: ", price)