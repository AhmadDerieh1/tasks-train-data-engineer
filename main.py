import json
from factory_parser import factory_parser
from splits import split_files
def convert_list_to_json(rows):
    receipt_dict = {}
    for item in rows:
        if isinstance(item, str):
            key, value = item.split(':', 1)
            receipt_dict[key] = value
        elif isinstance(item, dict):
            receipt_dict.update(item)
    json_data = json.dumps(receipt_dict, indent=4)
    return json_data

if __name__ == "__main__":
    file_path = 'Receipt.txt'
    parser_name = "Receipt"

    split_file = split_files()
    
    data = split_file.split_file_with_line(file_path)
    
    factory = factory_parser()
    
    strategy_item ,strategy_date = factory.get_strategy(file_path,parser_name)
    
    data_without_date,date = strategy_date.parser_data(data)
   
    data_without_items, items = strategy_item.parser_data(data_without_date)

    new_data = data_without_items.copy()
    new_data.pop(len(new_data)-1)
    new_data.append(date)  
    new_data.append(items)
    print(new_data)
    data_json = convert_list_to_json(new_data)
    print(data_json)