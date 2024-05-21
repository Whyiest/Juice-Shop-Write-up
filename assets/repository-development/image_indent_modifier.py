import os
import re

# Chemin relatif vers le répertoire contenant les fichiers Markdown
directory = ''

# Expression régulière pour trouver les balises d'image HTML et Markdown
html_image_pattern = re.compile(r'<img\s+[^>]*src="([^"]+)"[^>]*>')
markdown_image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

def adjust_image_indentation(content):
    lines = content.split('\n')
    adjusted_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        # Vérifiez si la ligne actuelle contient une image HTML ou Markdown
        if html_image_pattern.search(line) or markdown_image_pattern.search(line):
            if i > 0:
                # Obtenez l'indentation de la ligne précédente non vide
                prev_line_index = i - 1
                while prev_line_index >= 0 and lines[prev_line_index].strip() == '':
                    prev_line_index -= 1
                
                if prev_line_index >= 0:
                    prev_line = lines[prev_line_index]
                    indentation = len(prev_line) - len(prev_line.lstrip())
                    # Ajustez l'indentation de la ligne actuelle
                    adjusted_line = ' ' * indentation + line.lstrip()
                    adjusted_lines.append(adjusted_line)
                    print(f"Image ré-indéntée : '{adjusted_line}'")
                else:
                    adjusted_lines.append(line)
                    print(f"Aucune ligne précédente non vide pour l'indentation de : '{line}'")
            else:
                adjusted_lines.append(line)
                print(f"Aucune ligne précédente pour l'indentation de : '{line}'")
        else:
            adjusted_lines.append(line)
        i += 1

    return '\n'.join(adjusted_lines)

def process_file(file_path):
    print(f"Traitement du fichier : {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Ajuster l'indentation des images
        new_content = adjust_image_indentation(content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Indentation des images corrigée dans le fichier : {file_path}")
        else:
            print(f"Aucune modification nécessaire pour le fichier : {file_path}")
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
                process_file(file_path)

if __name__ == "__main__":
    print(f"Début du traitement du répertoire : {directory}")
    process_directory(directory)
    print("Traitement terminé.")
