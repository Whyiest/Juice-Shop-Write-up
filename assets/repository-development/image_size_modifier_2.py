import os
import re

# Chemin relatif vers le répertoire contenant les fichiers Markdown
directory = ''

# Expressions régulières pour trouver les balises d'image Markdown et HTML
markdown_image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
html_image_pattern = re.compile(r'<img src="([^"]+)" alt="([^"]*)" width="(?:400|600)px">')

def adjust_image_indentation(content):
    lines = content.split('\n')
    adjusted_lines = []

    for i, line in enumerate(lines):
        # Vérifiez si la ligne actuelle contient une image Markdown ou HTML
        if markdown_image_pattern.search(line) or html_image_pattern.search(line):
            if i > 0:
                # Obtenez l'indentation de la ligne précédente
                prev_line = lines[i - 1]
                indentation = len(prev_line) - len(prev_line.lstrip())
                # Ajustez l'indentation de la ligne actuelle
                adjusted_lines.append(' ' * indentation + line.lstrip())
            else:
                 adjusted_lines.append(line)
        else:
            adjusted_lines.append(line)

    return '\n'.join(adjusted_lines)

def replace_markdown_and_html_images(file_path):
    print(f"Traitement du fichier : {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remplacer chaque balise d'image Markdown par une balise HTML avec width=600px
        content, markdown_replacements = markdown_image_pattern.subn(r'<img src="\2" alt="\1" width="600px">', content)
        
        # Remplacer chaque balise d'image HTML existante avec width=400px par width=600px
        content, html_replacements = html_image_pattern.subn(r'<img src="\1" alt="\2" width="600px">', content)
        
        # Ajuster l'indentation des images
        content = adjust_image_indentation(content)

        total_replacements = markdown_replacements + html_replacements

        if total_replacements > 0:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"{total_replacements} images redimensionnées et ré-indentées dans le fichier : {file_path}")
        else:
            print(f"Aucune image trouvée dans le fichier : {file_path}")
    except Exception as e:
        print(f"Erreur lors du traitement du fichier {file_path} : {e}")

def process_directory(directory):
    absolute_directory = os.path.abspath(directory)
    print(f"Chemin absolu du répertoire : {absolute_directory}")
    
    if not os.path.exists(absolute_directory):
        print(f"Le répertoire spécifié n'existe pas : {absolute_directory}")
        return
    
    for root, dirs, files in os.walk(absolute_directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                replace_markdown_and_html_images(file_path)

if __name__ == "__main__":
    print(f"Début du traitement du répertoire : {directory}")
    process_directory(directory)
    print("Traitement terminé.")
