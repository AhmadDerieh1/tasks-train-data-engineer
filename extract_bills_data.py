from header import split_file,extract_items,extract_date,convert_list_to_dict
import json
file_path = 'Receipt.txt'
cleaned_lines = split_file(file_path)
value = "items"
try:
    rows = split_file(file_path)
    rows,date = extract_date(rows)
    rows,items =extract_items(rows)
    rows.pop(len(rows)-1)
    print(date)
    rows.append(date)
    rows.append(items)
    rows=convert_list_to_dict(rows)
    data_json = json.dumps(rows, indent=4)
    print(data_json)
except Exception as e:
    print(f"An error occurred: {e}")