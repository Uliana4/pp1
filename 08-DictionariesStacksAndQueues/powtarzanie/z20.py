import json

with open("euro.json", "r") as euro_file:
    euro_data = json.load(euro_file)

print("Date            Buying Rate     Selling Rate")
print("=" * 44)

for rate in euro_data['rates']:
    date = rate['effectiveDate']
    buying_rate = rate['bid']
    selling_rate = rate['ask']
    print(f"{date}      {buying_rate:.4f}          {selling_rate:.4f}")