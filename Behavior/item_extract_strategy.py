from Iextract_strategy import data_extract_strategy
import re
class item_extract_strategy(data_extract_strategy):
    def parser_data(self, rows):
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
        return new_list, {"items": items}
