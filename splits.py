import re
class split_files:
    def split_file_with_line(self,file_path):
        with open(file_path, 'r', encoding='utf-16') as file:
            content = file.read()
        lines = content.splitlines()
        cleaned_lines = []
        for line in lines:
            trimmed_line = line.strip()
            cleaned_line = re.sub(r'\s+', ' ', trimmed_line)
            cleaned_lines.append(cleaned_line)
        return cleaned_lines