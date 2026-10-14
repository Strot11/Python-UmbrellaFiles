is_boiling = True

stir_count= 5

total_actions = stir_count + is_boiling #upcasting to integer
print(f"Total actions: {total_actions}")

milk_present = 0 #no milk

print(f"Is there milk? {bool(milk_present)}");

water_hot = True
tea_added = False

can_serve = water_hot or tea_added
print(f"Can serve tea? {can_serve}")