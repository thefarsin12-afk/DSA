prices = [7,1,5,3,6,4]

buy_price = prices[0]

max_profit = 0

for price in prices:

    if price < buy_price:

        buy_price = price

    profit = price - buy_price

    if profit > max_profit:

        max_profit = profit

print(max_profit)            