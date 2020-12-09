import csv
import folium
import webbrowser

# début -----------------------------------------------------
# création de la liste de dictionnaires villes
villes = []
with open('cities.csv', newline='',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for ligne in reader:
        villes.append(dict(ligne))

# affichage d'une ville pour voir la structure
print(villes[100])
print(len(villes))

# création de la liste de dictionnaires pays
pays = []
with open('countries.csv', newline='',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for ligne in reader:
        pays.append(dict(ligne))

# affichage d'un pays pour voir la structure
    print(pays[100])
    print(len(pays))

# création d'une carte avec la bibliothèque folium
lat=0
lon=0
zoom='3'
ma_carte=folium.Map(location=[lat,lon],zoom_start=zoom)

# recherche et affichage des données du pays France
for pa in pays:
    if pa['countryCode']=='FR':
        print(pa)

# recherche des villes Françaises de plus de 200 000 habitants
# ajout d'un marqueur sur la carte et d'un popup sur ces villes , à 'aide
# de leurs coordonnées
for ville in villes:
    if ville['country_code']=='FR' and int(ville['habitants'])>200000:
        print(ville['cityName'],ville['habitants'])
        folium.Marker([float(ville['latitude']),float(ville['longitude'])],
        popup=ville['cityName']+'<br/>'+'pop:'+ville['habitants']).add_to(ma_carte)

# enregistrement de la carte
# dans le même dossier que le script
ma_carte.save('maCarte.html')
# ouvre la carte dans un navigateur
webbrowser.open('maCarte.html')