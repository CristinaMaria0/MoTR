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

# Lista de useri (coloanele suplimentare)
users = ['iulia', 'petru', 'sergiu', 'stadio88', 'user', 'victor']

# Funcție pentru a elimina spațiile din cheie
def create_key(propozitie, cuvant):
    return f"{propozitie.replace(' ', '')}_{cuvant.replace(' ', '')}"

# Dicționar pentru a stoca datele
data = {}

# Citim fișierele CSV și populăm dicționarul
for user in users:
    file_name = f"adnotari_complexitate\/{user}.csv"

    if os.path.exists(file_name):
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = create_key(row['text'], row['word'])
                if key not in data:
                    data[key] = {'propozitie': row['text'], 'cuvant': row['word']}
                data[key][user] = label_mapping.get(row['label'], 0)  # Default la 0 dacă labelul nu este găsit

# Scriem datele într-un nou fișier CSV
output_file = 'individual_scores.csv'
with open(output_file, mode='w', encoding='utf-8', newline='') as file:
    fieldnames = ['propozitie', 'cuvant'] + users
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for key, values in data.items():
        writer.writerow(values)

print(f"Fișierul {output_file} a fost creat cu succes.")