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
                            "Véhicule - Marque": vehicule_info['marque'],
                            "Modèle": vehicule_info['modele'],
                            "Plaque d'immatriculation": vehicule_info['immatriculation']
                           }
                vu_liste.append(vu_dict)
    return vu_liste

# Cette fonction trie la liste des personnes par nom puis par prénom
def tri_personnes(liste_personnes):
    liste_personnes_triee = sorted(liste_personnes, key=lambda x: (x['Nom utilisateur'], x['Prénom utilisateur']))
    return liste_personnes_triee

def filtrer_par_marque(liste_dicts, marque):
    return [d for d in liste_dicts if d.get("Véhicule - Marque") == marque]

csv_list_ecole_file_path = "csv/liste_ecole_nv.csv"
csv_parc_auto_file_path = "csv/park_auto.csv"
resultat = fn_display_veh_and_user(csv_parc_auto_file_path, csv_list_ecole_file_path)
resultat_trie = tri_personnes(resultat)
marque_filtree = filtrer_par_marque(resultat_trie, "TOYOTA")
print(marque_filtree)
# Affichage des résultats triés
pprint(marque_filtree)
