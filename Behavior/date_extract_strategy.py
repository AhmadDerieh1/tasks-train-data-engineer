from Iextract_strategy import DataExtractionStrategy
import re
class DateExtractionStrategy(DataExtractionStrategy):
    def process_data(self, lines):
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
