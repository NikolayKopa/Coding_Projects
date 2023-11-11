personStock = { 'Joe' :{'AAPL':5, 'AMZN':2},  'Bill' :{'AAPL':2, 'AMZN' :5 }}
stockValue = {'AAPL' : 227, 'AMZN' :1721 , 'NFLX' : 267 , 'TSLA' : 244, 'FB' : 179 }
comparisonStocks = []
for person in personStock:
   totalStockValue = 0
   for stock in personStock[person]:
       totalStockValue += stockValue[stock]*personStock[person][stock]
       comparisonStocks.append(int(totalStockValue))
   print(person, ": ", totalStockValue)
if comparisonStocks[0] >= comparisonStocks[1]:
   print("Joe will earn more money.")
elif comparisonStocks[0] <= comparisonStocks[1]:
   print("Bill will earn more money.")
elif comparisonStocks[0] == comparisonStocks[1]:
   print("They will both earn the same amount.")
