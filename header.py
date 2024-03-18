import re
class Item:
    def __init__(self, item_name="Default Item", price=0, quantity=0):
        self._item_name = item_name
        self._price = price
        self._quantity = quantity   
    def get_total(self):
        return self._quantity*self._price
    def print_information(self):
        print(f"Item Name: {self._item_name}, Price: ${self._price}, Quantity: {self._quantity}, Total: {self._quantity*self._price}$")

def split_file(file_path):
    rows = []
    try:
        with open(file_path, 'r', encoding='utf-16') as file:
            for line in file:
                row = line.strip().split(':')
                rows.append(row)
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    return rows

def extract_items(rows):
    price_pattern = r'\$(\d+)'
    quantity_pattern = r'\b(\d+)\s*x\b'
    index = 1
    start = 5
    step = 2
    number = 0
    list_of_items= []
    for i in range(start, len(rows), step):
        if 'Items count' in rows[i][number] or 'Items count' in rows[i-index][number]:
            break
        try:
            item_name = rows[i-index][number]
            price_match = re.search(price_pattern, rows[i][number])
            quantity_match = re.search(quantity_pattern, rows[i][number])
            price = float(price_match.group(index))
            quantity = int(quantity_match.group(index))
        except ValueError as e:
            print(f"Error converting price or quantity for item '{item_name}': {e}")
            price = None
            quantity = None
        list_of_items.append(Item(item_name=item_name, price=price, quantity=quantity))
    return list_of_items

def extract_general_information(rows):
    data = {}
    element = 2
    space_number = 3
    index = 1
    number = 0 
    colon_number = 3
    for i in range(len(rows)):
        if len(rows[i]) == element :
            space_count = rows[i][index].count(" ")
            if space_count >= space_number:
                cleaned_text = rows[i][index].lstrip()
                data[rows[i][number]] = cleaned_text
            else:
                data[rows[i][number]] = rows[i][index]
        if len(rows[i]) >= colon_number :
            value = ':'.join(rows[i])
            if "PM" or "AM" in value:
                data["data time"] = value
            else:
                data["default value"] = value
    return data

def insert_at_position(original_dict, position, key, value):
    items = list(original_dict.items())
    items.insert(position, (key, value))
    new_dict = dict(items)
    return new_dict