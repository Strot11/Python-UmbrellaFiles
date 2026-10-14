# Function Reduces code Duplication

def print_order(name, chai_type): # parameters
    print(f"{name} ordered {chai_type} chai!")

print_order("Strot","Masala")
print_order("Aman","Ginger")
print_order("Nayan","Clove")
# print("hitesh")  arguments

# Splitting the Complex Task
def fetch_sales():
    print("Fetching the sales Datas")

def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is Generated Congratulations !!!")

generate_report()

