import os
import subprocess
from pathlib import Path

# 1. Rename directories using git mv
dirs_to_rename = [
    'clases/presentacion',
    'clases/sistemas_de_big_data',
    'clases/big_data_aplicado'
]

for d in dirs_to_rename:
    old_path = os.path.join(d, 'calificaciones')
    new_path = os.path.join(d, 'examenes')
    if os.path.isdir(old_path):
        subprocess.run(['git', 'mv', old_path, new_path])

# 2. Update markdown files
md_files = list(Path('.').rglob('*.md'))
for file in md_files:
    if '.git' in file.parts:
        continue
    content = file.read_text(encoding='utf-8')
    
    if 'calificaciones' in content.lower() or 'calificaciones/' in content.lower():
        # Replace occurrences in paths
        content = content.replace('calificaciones/', 'examenes/')
        content = content.replace('`calificaciones/`', '`examenes/`')
        content = content.replace('Calificaciones', 'Exámenes')
        content = content.replace('calificaciones', 'exámenes')
        file.write_text(content, encoding='utf-8')

print("Renamed and replaced successfully.")
