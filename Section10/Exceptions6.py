# file handling

# Traditional way of handling files

# try:
#     file = open("order.txt","w")
#     file.write("Masala Chai - cups")
# finally:
#     file.close()

with open("order.txt","w") as file:
    file.write("Ginger Tea - 4 cups")

# Behind the scenes it execute file.__enter__() and file.__exit__() methods to 
# handle the file closing automatically


