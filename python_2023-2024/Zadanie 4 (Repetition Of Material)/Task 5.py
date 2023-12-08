#5. Przeszukiwanie bazy danych.
import random


def baza_danych(names, surnames, num_records):
    data_list = []

    for _ in range(num_records):
        record = {
            'name': random.choice(names),
            'surname': random.choice(surnames),
            'age': random.randint(18, 70),
            'phone': random.randint(5000000, 8000000)
        }
        data_list.append(record)

    return data_list

def search_data(data_list, key, value):
    results = [record for record in data_list if record[key] == value]
    return results

if __name__ == "__main__":
    names = ['John', 'Jane', 'Bob', 'Alice', 'Charlie']
    surnames = ['Smith', 'Doe', 'Johnson', 'Brown', 'Taylor']

    num_records = 10
    data_list = baza_danych(names, surnames, num_records)

    print("Generated data:")
    for record in data_list:
        print(record)

    search_key = 'age'  # Możesz to zmienić na dowolny klucz, który chcesz wyszukać
    search_value = 30    # Możesz zmienić tę wartość na dowolną wartość, którą chcesz wyszukać

    results = search_data(data_list, search_key, search_value)

    print(f"\nSearch results for {search_key}={search_value}:")
    for result in results:
        print(result)