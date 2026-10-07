import os
import re
import subprocess
from glob import glob

slide_dirs = [
    "clases/big_data_aplicado/presentaciones/2026_10_08_almacenamiento_y_procesamiento_de_datos",
    "clases/sistemas_de_big_data/presentaciones/2026_10_05_conceptos_basicos"
]

for d in slide_dirs:
    if not os.path.exists(d):
        continue
    
    # 1. Rename files from _1.png to _01.png
    files = os.listdir(d)
    for f in files:
        # Looking for pattern: ..._X.png where X is a single digit
        match = re.search(r'_(\d)\.png$', f)
        if match:
            num = match.group(1)
            new_name = f[:match.start(1)] + f"0{num}" + ".png"
            
            old_path = os.path.join(d, f)
            new_path = os.path.join(d, new_name)
            
            print(f"Renaming {f} to {new_name}")
            subprocess.run(["git", "mv", old_path, new_path])
            
    # Refresh list of files after renaming
    files = sorted([f for f in os.listdir(d) if f.endswith('.png') or f.endswith('.jpg')])
    
    # 2. Create README.md
    readme_path = os.path.join(d, "README.md")
    readme_content = f"# Diapositivas: {os.path.basename(d).replace('_', ' ')}\n\n"
    
    for slide in files:
        readme_content += f"## {slide}\n"
        # We use relative markdown link to image
        readme_content += f"![{slide}]({slide})\n\n"
        
    with open(readme_path, "w") as rf:
        rf.write(readme_content)
        
    subprocess.run(["git", "add", readme_path])

