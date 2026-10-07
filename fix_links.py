import re
import urllib.parse
import os

files_to_check = ['README.md', 'clases/README.md']

def replace_link(match):
    text = match.group(1)
    path = match.group(2)
    # Don't double-encode
    if '%' not in path:
        encoded_path = urllib.parse.quote(path)
        # return without the <> if we are URL-encoding it
        return f"[{text}]({encoded_path})"
    return match.group(0)

for filepath in files_to_check:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Match [text](<path>)
        new_content = re.sub(r'\[(.*?)\]\(<(.*?)>\)', replace_link, content)
        
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

