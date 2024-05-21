from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route("/index", methods=['GET'])
def index():
    csv_list_ecole_file_path = "csv/liste_ecole_nv.csv"
    csv_parc_auto_file_path = "csv/park_auto.csv"
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
                            "nom": item['nom'], 
                            "prenom": item['prenom'],
                            "marque": vehicule_info['marque'],
                            "modele": vehicule_info['modele'],
                            "plaque": vehicule_info['immatriculation']
                           }
                vu_liste.append(vu_dict)
   
    return render_template('index.html', data=vu_liste)

if __name__ == '__main__':
    app.run(debug=True)