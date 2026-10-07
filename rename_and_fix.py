import os
import re
import unicodedata
from glob import glob
import subprocess

def to_snake_case(name):
    # Separate extension
    name, ext = os.path.splitext(name)
    # Remove accents
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('utf-8')
    # Lowercase
    name = name.lower()
    # Replace non-alphanumeric (including spaces, #, -, commas) with underscores
    name = re.sub(r'[^a-z0-9]+', '_', name)
    # Remove leading/trailing underscores
    name = name.strip('_')
    return name + ext.lower()

directories_to_check = [
    "clases/big_data_aplicado/presentaciones",
    "clases/sistemas_de_big_data/presentaciones"
]

rename_map = {}

for d in directories_to_check:
    if not os.path.exists(d):
        continue
    
    # Process top-level items in these directories
    for item in os.listdir(d):
        if item in [".", "..", ".gitkeep", ".DS_Store"]:
            continue
        
        old_path = os.path.join(d, item)
        new_name = to_snake_case(item)
        new_path = os.path.join(d, new_name)
        
        if item != new_name:
            # We must rename
            print(f"Renaming: {item} -> {new_name}")
            subprocess.run(["git", "mv", old_path, new_path])
            rename_map[item] = new_name
            
            # If it's a directory, should we process its contents? 
            # The rule says folders should be snake_case. Files inside? 
            # Let's also do files inside the directories.
            if os.path.isdir(new_path):
                for subitem in os.listdir(new_path):
                    if subitem in [".", "..", ".gitkeep", ".DS_Store"]:
                        continue
                    old_sub_path = os.path.join(new_path, subitem)
                    new_sub_name = to_snake_case(subitem)
                    new_sub_path = os.path.join(new_path, new_sub_name)
                    if subitem != new_sub_name:
                        subprocess.run(["git", "mv", old_sub_path, new_sub_path])

# Now update READMEs
readme_files = ["README.md", "clases/README.md"]
for rf in readme_files:
    if os.path.exists(rf):
        with open(rf, "r") as f:
            content = f.read()
            
        import urllib.parse
        for old_name, new_name in rename_map.items():
            # The old name might be URL encoded in the markdown
            encoded_old = urllib.parse.quote(old_name)
            
            # Replace encoded old name
            content = content.replace(encoded_old, new_name)
            # Replace unencoded old name (just in case)
            content = content.replace(old_name, new_name)
            
        with open(rf, "w") as f:
            f.write(content)

