# Integer

black_tea_grams = 14
ginger_grams=3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of tea: {total_grams}")

remaining_grams = black_tea_grams - ginger_grams
print(f"Remaining grams of tea: {remaining_grams}")

milk_litres = 7
serving = 4
milk_per_serving = milk_litres / serving
print(f"Milk per serving: {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots # Not worried about the decimal part
print(f"Bags per pot: {bags_per_pot}")

total_cadamon_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamon_pods % pods_per_cup
print(f"Leftover pods: {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3

powerful_flavor = base_flavor_strength ** scale_factor
print(f"Powerful flavor strength: {powerful_flavor}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Total Tea leaves harvested: {total_tea_leaves_harvested}")