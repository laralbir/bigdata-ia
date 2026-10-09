import os

def get_markdown_title(filepath, fallback_name):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('# '):
                    return line[2:].strip()
    except Exception:
        pass
    return fallback_name

def format_name(name):
    mapping = {
        "introduccion_a_python": "Intro a Python",
        "tfm": "TFM",
        "masterclasses": "Masterclasses",
        "modelos_de_inteligencia_artificial": "Modelos IA",
        "sistemas_de_aprendizaje_automatico": "Aprendizaje Automático",
        "sistemas_de_big_data": "Sistemas de Big Data",
        "programacion_de_inteligencia_artificial": "Programación IA",
        "big_data_aplicado": "Big Data Aplicado",
        "aws_e_ia": "AWS e IA",
        "presentacion": "Presentación del Curso",
        "anotaciones": "📝 Apuntes y Teoría",
        "presentaciones": "📊 Presentaciones",
        "grabaciones": "🎥 Grabaciones",
        "entregables": "💻 Entregables",
        "examenes": "📈 Exámenes"
    }
    if name in mapping:
        return mapping[name]
    return name.replace("_", " ").title().replace(".Md", "")

def generate_sidebar():
    sidebar = [
        "- [🏠 Inicio](README.md)",
        "- [📅 Calendario Interactivo](calendario.md)",
        "",
        "- **📚 Asignaturas**"
    ]
    
    clases_dir = "clases"
    if os.path.exists(clases_dir):
        order = [
            "presentacion",
            "sistemas_de_big_data",
            "big_data_aplicado",
            "introduccion_a_python",
            "sistemas_de_aprendizaje_automatico",
            "programacion_de_inteligencia_artificial",
            "modelos_de_inteligencia_artificial",
            "aws_e_ia",
            "masterclasses",
            "tfm"
        ]
        
        subjects = [d for d in os.listdir(clases_dir) if os.path.isdir(os.path.join(clases_dir, d))]
        subjects.sort(key=lambda x: order.index(x) if x in order else len(order))
        
        for subject in subjects:
            subject_path = os.path.join(clases_dir, subject)
            readme_path = os.path.join(subject_path, "README.md")
            
            subject_title = get_markdown_title(readme_path, format_name(subject)) if os.path.exists(readme_path) else format_name(subject)
            
            if os.path.exists(readme_path):
                sidebar.append(f"  - [{subject_title}]({readme_path})")
            else:
                sidebar.append(f"  - {subject_title}")
                
            subdirs = ["anotaciones", "presentaciones", "grabaciones", "entregables", "examenes"]
            for subdir in subdirs:
                subdir_path = os.path.join(subject_path, subdir)
                if os.path.exists(subdir_path):
                    files = sorted([f for f in os.listdir(subdir_path) if f.endswith('.md')])
                    if files:
                        # Append the category folder as a non-clickable title or clickable if it has README
                        subdir_readme = os.path.join(subdir_path, "README.md")
                        category_name = format_name(subdir)
                        if "README.md" in files:
                            sidebar.append(f"    - [{category_name}]({subdir_readme})")
                        else:
                            sidebar.append(f"    - **{category_name}**")
                            
                        for f in files:
                            if f == "README.md":
                                continue
                            
                            filepath = os.path.join(subdir_path, f)
                            fallback = "Enlaces a Grabaciones" if f == "enlaces_drive.md" else format_name(f[:-3])
                            name = get_markdown_title(filepath, fallback)
                                
                            sidebar.append(f"      - [{name}]({filepath})")

    sidebar.append("")
    sidebar.append("- **👨‍💻 Cursos Extras**")
    cursos_dir = "cursos"
    if os.path.exists(cursos_dir):
        cursos = sorted([d for d in os.listdir(cursos_dir) if os.path.isdir(os.path.join(cursos_dir, d))])
        for curso in cursos:
            curso_path = os.path.join(cursos_dir, curso)
            main_file = None
            if os.path.exists(os.path.join(curso_path, "00-indice.md")):
                main_file = "00-indice.md"
            elif os.path.exists(os.path.join(curso_path, "README.md")):
                main_file = "README.md"
            
            if main_file:
                filepath = os.path.join(curso_path, main_file)
                curso_title = get_markdown_title(filepath, format_name(curso))
                sidebar.append(f"  - [{curso_title}]({filepath})")
            
    with open("_sidebar.md", "w", encoding="utf-8") as f:
        f.write("\n".join(sidebar) + "\n")

if __name__ == "__main__":
    generate_sidebar()
