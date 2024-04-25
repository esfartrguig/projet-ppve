import csv
from pprint import pprint

# Cette fonction affiche les détails des véhicules à partir d'un fichier CSV
def fn_display_vehicule(csv_file_path):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        vehicule_reader = csv.DictReader(csvfile, delimiter=';')
        for item in vehicule_reader:
            print(f"Type : {item['type']}, Matricule : {item['matricule']}, Prénom : {item['prenom']}, Nom : {item['nom']}, Date de naissance : {item['naissance']}")

# Cette fonction affiche les détails des utilisateurs et des véhicules qu'ils utilisent en les comparant avec deux fichiers CSV
def fn_display_veh_and_user(csv_parc_auto_file_path, csv_list_ecole_file_path):
    vehicules = {}

    # Lecture du fichier CSV contenant les informations sur les véhicules
    with open(csv_parc_auto_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        vehicule_reader = csv.DictReader(csvfile, delimiter=';')
        for item in vehicule_reader:
            vehicules[item['immatriculation']] = item

    # Lecture du fichier CSV contenant les informations sur les utilisateurs
    with open(csv_list_ecole_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        utilisateur_reader = csv.DictReader(csvfile, delimiter=';')
        vu_liste = []
        for item in utilisateur_reader:
            user_immatriculation = item['immatriculation']
            if user_immatriculation in vehicules:
                vehicule_info = vehicules[user_immatriculation]
                # Création d'un dictionnaire contenant les détails de l'utilisateur et du véhicule utilisé
                vu_dict = {
                            "Nom utilisateur": item['nom'], 
                            "Prénom utilisateur": item['prenom'],
                            "Marque véhicule": vehicule_info['marque'],
                            "Modèle véhicule": vehicule_info['modele'],
                            "Plaque d'immatriculation": vehicule_info['immatriculation']
                           }
                vu_liste.append(vu_dict)
    return vu_liste

# Cette fonction trie la liste des personnes par nom puis par prénom
def tri_personnes(liste_personnes):
    liste_personnes_triee = sorted(liste_personnes, key=lambda x: (x['Nom utilisateur'], x['Prénom utilisateur']))
    return liste_personnes_triee

# Chemins des fichiers CSV contenant les données sur les utilisateurs et les véhicules
csv_list_ecole_file_path = "csv/liste_ecole_nv.csv"
csv_parc_auto_file_path = "csv/park_auto.csv"

# Appel de la fonction pour afficher les détails des véhicules (peut être commenté si non nécessaire)
# fn_display_vehicule(csv_parc_auto_file_path)

# Appel de la fonction pour afficher les détails des utilisateurs et des véhicules qu'ils utilisent
# (peut être commenté si non nécessaire)
# fn_display_veh_and_user(csv_parc_auto_file_path, csv_list_ecole_file_path)

# Appel de la fonction pour obtenir et trier les détails des utilisateurs et des véhicules qu'ils utilisent
resultat = fn_display_veh_and_user(csv_parc_auto_file_path, csv_list_ecole_file_path)
resultat_trie = tri_personnes(resultat)

# Affichage des résultats triés
pprint(resultat_trie)
