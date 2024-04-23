import os
from Behavior.item_extract_strategy import item_extract_strategy
from Behavior.date_extract_strategy import date_extract_strategy
class factory_parser():

    @staticmethod
    def get_strategy(file_name,parser_name):
        _, file_extension = os.path.splitext(file_name)

        if parser_name == "Receipt" and file_extension == '.txt':  
            return item_extract_strategy(), date_extract_strategy()
        else:    
            raise ValueError('Unknown Strategy Type')