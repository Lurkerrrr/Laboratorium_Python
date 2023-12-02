#7. Napisz funkcję, która przyjmuje wartość temperatury w Kelvinach i zwraca wartość wyrażoną w stopniach Celsjusza: TC = TK − 272.15. W przypadku podania wartości ujemnej funkcja zwraca None. Przetestuj jej działanie.
def temp_change(kelvin):
    if kelvin < 0:
        return None
    else:
        celsius_temperature = kelvin - 272.15
        return celsius_temperature

kelvin_value = 273
celsius_result = temp_change(kelvin_value)

if celsius_result is not None:
    print(f"{kelvin_value} Kelvin is equal to {celsius_result:.2f} Celsius.")
else:
    print("Invalid input. Temperature cannot be negative.")