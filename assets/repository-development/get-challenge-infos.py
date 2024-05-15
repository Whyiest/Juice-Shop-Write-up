import os
import re

# Chemin relatif vers le répertoire contenant les fichiers Markdown
directory = 'Documents/Juice-Shop-Write-Up'

# Expressions régulières pour trouver les informations du challenge
title_pattern = re.compile(r'# Juice-Shop Write-up: (.+)')
category_pattern = re.compile(r'\*\*Category:\*\* (.+)')
difficulty_pattern = re.compile(r'\*\*Difficulty:\*\* (.+)')

def extract_challenge_info(content):
    title_match = title_pattern.search(content)
    category_match = category_pattern.search(content)
    difficulty_match = difficulty_pattern.search(content)
    
    if title_match and category_match and difficulty_match:
        title = title_match.group(1).strip()
        category = category_match.group(1).strip()
        difficulty = difficulty_match.group(1).strip()
        return f"{title} - {category} - {difficulty}"
    return None

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Extraire les informations du challenge
        challenge_info = extract_challenge_info(content)
        
        return challenge_info
    except Exception as e:
        print(f"Erreur lors du traitement du fichier {file_path} : {e}")
        return None

def process_directory(directory):
    absolute_directory = os.path.abspath(directory)
    print(f"Chemin absolu du répertoire : {absolute_directory}")
    
    if not os.path.exists(absolute_directory):
        print(f"Le répertoire spécifié n'existe pas : {absolute_directory}")
        return
    
    challenges = []
    for root, dirs, files in os.walk(absolute_directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                challenge_info = process_file(file_path)
                if challenge_info:
                    challenges.append(challenge_info)
    
    return challenges

if __name__ == "__main__":
    print(f"Début du traitement du répertoire : {directory}")
    challenges = process_directory(directory)
    print("Traitement terminé.")
    
    # Afficher ou enregistrer les résultats
    if challenges:
        with open('challenges_info.txt', 'w', encoding='utf-8') as output_file:
            for challenge in challenges:
                output_file.write(challenge + '\n')
        print("Les informations des challenges ont été enregistrées dans 'challenges_info.txt'.")
    else:
        print("Aucun challenge trouvé.")
