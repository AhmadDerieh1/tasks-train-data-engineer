import re
def split_file(file_path):
    with open(file_path, 'r', encoding='utf-16') as file:
        content = file.read()
    lines = content.splitlines()
    cleaned_lines = []
    for line in lines:
        trimmed_line = line.strip()
        cleaned_line = re.sub(r'\s+', ' ', trimmed_line)
        cleaned_lines.append(cleaned_line)
    return cleaned_lines
def extract_date(lines):
    new_rows = []
    found_date = None  
    date_pattern = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4}) (\d{1,2}):(\d{2}):(\d{2}) (AM|PM)')
    for line in lines:
        match = date_pattern.search(line)
        if match:
            found_date = "time:"+ match.group(0)              
            continue 
        new_rows.append(line)  
    return new_rows, found_date
def extract_items(rows):
    pattern = re.compile(r'(\d+)\s*x\s*\$(\d+\.\d+)')  
    new_list = []
    items = []
    for index, row in enumerate(rows):
        if index + 1 < len(rows):
            check_match = pattern.search(rows[index + 1])
        else:
            check_match = None  
        match = pattern.search(row)
        if match:
            item_name = rows[index - 1]
            quantity, price = match.groups()
            items.append({"item_name": item_name, "price": price, "quantity": quantity})
            continue
        elif not check_match:
            new_list.append(row)
    return  new_list, {"items": items} 
def convert_list_to_dict(rows):  
    receipt_dict = {}
    for item in rows:
        if isinstance(item, str):
            key, value = item.split(':', 1)
            receipt_dict[key] = value
        elif isinstance(item, dict):
            receipt_dict.update(item)
    return receipt_dict