import csv
import os

# Definim maparea labelurilor la scoruri
label_mapping = {
    'foarte familiar': 1,
    'simplu': 2,
    'nici simplu nici complex': 3,
    'complex': 4,
    'nu cunosc': 5
}

# Folderul unde se află fișierele
folder_path = 'adnotari_complexitate'

# Funcție pentru a elimina spațiile din cheie
def create_key(propozitie, cuvant):
    return f"{propozitie.replace(' ', '')}_{cuvant.replace(' ', '')}"

# Dicționar pentru a stoca datele
data = {}

# Set pentru a colecta toți utilizatorii
all_users = set()

# Listăm toate fișierele din folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):  # Ne asigurăm că este un fișier CSV
        user = file_name.replace('.csv', '')  # Extragem numele utilizatorului din numele fișierului
        all_users.add(user)  # Adăugăm utilizatorul la set
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = create_key(row['text'], row['word'])
                if key not in data:
                    data[key] = {'propozitie': row['text'], 'cuvant': row['word']}
                data[key][user] = label_mapping.get(row['label'], 5)  # Default la 5 dacă labelul nu este găsit

# Scriem datele într-un nou fișier CSV
output_file = 'individual_scores.csv'
with open(output_file, mode='w', encoding='utf-8', newline='') as file:
    # Definim coloanele: propozitie, cuvant + toți utilizatorii
    fieldnames = ['propozitie', 'cuvant'] + list(all_users)
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for key, values in data.items():
        writer.writerow(values)

print(f"Fișierul {output_file} a fost creat cu succes.")