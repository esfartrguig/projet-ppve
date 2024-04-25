import csv

def tri_personnes(liste_personnes):
    liste_personnes_triee = sorted(liste_personnes, key=lambda x: (x['nom'], x['prénom']))
    return liste_personnes_triee

def fn_display_old(csv_file_1, csv_file_2):
    with open(csv_file_1, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
             print(row)

    with open(csv_file_2, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)

def fn_display_vehicule(csv_file_path):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        vehicule_reader = csv.DictReader(csvfile, delimiter=';')
        for item in vehicule_reader:
            print(f"Type : {item['type']}, Matricule : {item['matricule']}, Prénom : {item['prenom']}, Nom : {item['nom']}, Date de naissance : {item['naissance']}")

def fn_display_veh_and_user(csv_parc_auto_file_path, csv_list_ecole_file_path):
    vehicules = {}

    with open(csv_parc_auto_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        vehicule_reader = csv.DictReader(csvfile, delimiter=';')
        for item in vehicule_reader:
            vehicules[item['immatriculation']] = item

    with open(csv_list_ecole_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        utilisateur_reader = csv.DictReader(csvfile, delimiter=';')
        vu_liste = []
        for item in utilisateur_reader:
            user_immatriculation = item['immatriculation']
            if user_immatriculation in vehicules:
                vehicule_info = vehicules[user_immatriculation]
                # print(f"Nom utilisateur : {item['nom']}, Prénom utilisateur : {item['prenom']}, Véhicule - Marque : {vehicule_info['marque']}, Modèle : {vehicule_info['modele']}, Plaque d'immatriculation : {vehicule_info['immatriculation']}")
                vu_dict = {
                            "Nom utilisateur ": item['nom'], 
                            "Prénom utilisateur": item['prenom'],
                            "Véhicule - Marque": vehicule_info['marque'],
                            "Modèle": vehicule_info['modele'],
                            "Plaque d'immatriculation": vehicule_info['immatriculation']
                           }
                vu_liste.append(vu_dict)
    return vu_liste   

csv_list_ecole_file_path = "csv/liste_ecole_nv.csv"
csv_parc_auto_file_path = "csv/park_auto.csv"

# fn_display_vehicule(csv_file_1)
# fn_display_veh_and_user(csv_parc_auto_file_path, csv_list_ecole_file_path)

vu_liste = fn_display_veh_and_user(csv_parc_auto_file_path,csv_list_ecole_file_path)
personnes_triees = tri_personnes(vu_liste)
for personne in personnes_triees:
    print(personne)