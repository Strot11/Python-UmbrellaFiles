# Static Methods

class ChaiUtils:
    @staticmethod
    def clean_ingridients(text):
        return [item.strip() for item in text.split(",")]

raw = "milk, sugar, tea leaves, water  "
x = ChaiUtils.clean_ingridients(raw)
print(x)