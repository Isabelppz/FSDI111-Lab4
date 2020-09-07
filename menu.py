import os

def menu():
    print("/n/n")
    print("-" * 30)
    print("Warehouse Control")
    print("-" * 30)

    print('[1] Register Items')
    print('[2] Display Catalog')
    print('[3] Display Out of stock')
    print('[4] Update item stock')
    print('[5] Calculate Stock value')
    print('[6] Remove item from catalog')
    print('[7] Register a sale')
    print('[8] Display log')

    print("[x] Exit")

def header(title):
    clear()
    print("-" * 70)
    print(" " + title)
    print("-" * 70)

def clear():
    return os.system('cls' if os.name == 'nt' else' clear')