import heapq
num_list = [1, 33, 3, 18, 7, -5, 18, 33, 51, -60, 5]
print(heapq.nlargest(3, num_list))
print(heapq.nsmallest(3, num_list))

offer_dict = [
    {'company_name': 'IBM', 'stock': 80, 'price': 81.1},
    {'company_name': 'AAPL', 'stock': 60, 'price': 113.22},
    {'company_name': 'FB', 'stock': 150, 'price': 91.09},
    {'company_name': 'HPQ', 'stock': 30, 'price': 79.75},
    {'company_name': 'YHOO', 'stock': 50, 'price': 85.35},
    {'company_name': 'ACME', 'stock': 100, 'price': 76.65}
]
cheapest = heapq.nsmallest(3, offer_dict, key=lambda s: s['price'])
max_stock = heapq.nlargest(2, offer_dict, key=lambda s: s['stock'])
print(cheapest)
print(max_stock)
