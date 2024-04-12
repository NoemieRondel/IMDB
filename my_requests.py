import requests

# URL de l'API ou du site que vous souhaitez interroger
url = 'http://20.19.235.140:5000/'

# Effectuer la requête GET
response = requests.get(url)

# Vérifier si la requête a réussi (statut HTTP 200)
if response.status_code == 200:
    # Afficher la réponse (sous forme de texte)
    print(response.text)
else:
    # Afficher un message d'erreur si la requête a échoué
    print(f"Erreur: La requête a retourné un statut {response.status_code}")
