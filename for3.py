prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for k, v in prices.items():
    prices[k] = round(v * 0.3, 1)  # Apply a 10% discount

print(prices)


prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for value in list(prices.keys()):  #Use a list instead of a view
    if value == '0.40':
        del prices[value]  # Delete a key from prices

print(prices)