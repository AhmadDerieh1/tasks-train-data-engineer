from header import split_file, extract_general_information,extract_items,insert_at_position
file_path = 'Receipt.txt'
try:
    rows = split_file(file_path)
    general_information = extract_general_information(rows)
    items = extract_items(rows)
    data = insert_at_position(general_information, 4, "items", items)
    print(data)
except Exception as e:
    print(f"An error occurred: {e}")
