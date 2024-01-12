#6. Szukanie liczb
count = 0  # Licznik spełniających warunek liczb

for i in range(1000, 10000):
    pdc = i // 100
    odc = i % 100

    if i == pdc + odc**2:
        print(i)
        count += 1

print(f"Ilość liczb spełniających warunek: {count}")