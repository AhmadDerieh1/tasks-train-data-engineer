from Iextract_strategy import data_extract_strategy
import re
class date_extract_strategy(data_extract_strategy):
    def parser_data(self, lines):
        new_rows = []
        found_date = None
        date_pattern = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4}) (\d{1,2}):(\d{2}):(\d{2}) (AM|PM)')
        for line in lines:
            match = date_pattern.search(line)
            if match:
                found_date = "time:" + match.group(0)
                continue
            new_rows.append(line)
        return new_rows, found_date