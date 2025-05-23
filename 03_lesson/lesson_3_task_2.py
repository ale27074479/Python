from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S23", "+79123456789"),
    Smartphone("Apple", "iPhone 16", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"),
    Smartphone("Google", "Pixel 7", "+79456789012"),
    Smartphone("OnePlus", "11 Pro", "+79567890123")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")