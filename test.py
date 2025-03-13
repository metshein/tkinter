import requests

url = 'https://metshein.com/kordamine/json/raamatud.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    kokku = 0
    pole = 0
    vanim = 3000
    parast = 0

    for raamat in data['raamatud']:
        aasta = raamat['väljaandmise_aasta']
        saadavus = raamat['saadavus']
        if aasta<2000:
            kokku+=1
        if aasta>2010:
            parast+=1
        if saadavus == False:
            pole+=1
        if aasta>vanim:
            vanim = aasta
        
    print(kokku)
    print(pole)
    print(vanim)
    print(parast)

else:
    print("Päring ebaõnnestus, staatuskood:", response.status_code)