import csv

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
            print(f"Type : {item["type"]}, Matricule : {item["matricule"]}, Prénom : {item["prenom"]}, Nom : {item["nom"]}, Date de naissance : {item["naissance"]}")

def fn_display_veh_and_user(csv_vehicule_file_path, csv_utilisateur_file_path):
	vehicules = {}

	with open(csv_vehicule_file_path, newline='', encoding='utf-8') as csvfile:
    	vehicule_reader = csv.DictReader(csvfile, delimiter=',')
    	for item in vehicule_reader:
        	vehicules[item['id']] = item

	with open(csv_utilisateur_file_path, newline='', encoding='utf-8') as csvfile:
    	utilisateur_reader = csv.DictReader(csvfile, delimiter=',')
    	for item in utilisateur_reader:
        	vehicule_id = item['vehicule_id']
        	if vehicule_id in vehicules:
            	vehicule_info = vehicules[vehicule_id]
            	print(f"Véhicule - Marque : {vehicule_info['marque']}, Modèle : {vehicule_info['modele']}, Plaque d'immatriculation : {vehicule_info['immatriculation_id']}, Nom utilisateur : {item['nom']}, Prénom utilisateur : {item['prenom']}")   


csv_file_1 = "csv/liste_ecole_nv.csv"
csv_file_2 = "csv/park_auto.csv"

fn_display_vehicule(csv_file_1)