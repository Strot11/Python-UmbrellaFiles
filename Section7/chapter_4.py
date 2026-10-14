# Generator Comprehension

daily_sales = [5,10,12,7,3,8,9,10]

# total_cups = [sale for sale in daily_sales if sale > 5] runs as it is since full memory allocation
# total_cups = (sale for sale in daily_sales if sale > 5) <generator object <genexpr> at 0x000001D7FE731220>
# it needs operation to be perform on stream of data coming for memory efficient systems

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)