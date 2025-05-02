import requests

def convert_currency(amount, from_currency, to_currency):
    from_currency = from_currency.lower()
    to_currency = to_currency.lower()
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        # Check if the target currency exists in the response
        if to_currency in data[from_currency]:
            rate = data[from_currency][to_currency]
            converted_amount = amount * rate
            print(f"{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")
        else:
            print(f"Currency code '{to_currency.upper()}' not found.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
print("🌐 Currency Converter")
amount = float(input("Enter amount to convert: "))
from_curr = input("From Currency (e.g., USD): ")
to_curr = input("To Currency (e.g., INR): ")

convert_currency(amount, from_curr, to_curr)