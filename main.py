models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = {}
#zmiana wartości NA na 0
sales2016 = [i.replace('NA', '0') for i in sales2016]
sales2017 = [i.replace('NA', '0') for i in sales2017]
#conwersja list z str do int
sales2016 = [int(i.replace(",", "")) for i in sales2016]
sales2017 = [int(i.replace(",", "")) for i in sales2017]
sales2018 = [int(i.replace(",", "")) for i in sales2018]
#Stworzenie pod-słownika
sales= {"2016":[sales2016],"2017":[sales2017],"2018":[sales2018]}

from collections import defaultdict
cars = defaultdict(list)

for a in models:
    b=a.split()
    cars[b[0]].append(b[2])
#print(cars)
cars={}
for a in models:
    b=a.split()
    cars[b[0]]={}
    cars[b[0]][b[2]]={}
#print(cars)
cars={}
for a, c, d, e in zip(models, sales2016, sales2017, sales2018):
    b=a.split()
    cars[b[0]]={}
    cars[b[0]][b[2]]={"2016":[c],"2017":[d],"2018":[e]}
#print(cars)

#podpięcie dat do modeli
cars={}
for a, c, d, e in zip(models, sales2016, sales2017, sales2018):
    b=a.split()
    cars[b[2]]= {"2016":[c],"2017":[d],"2018":[e]}
print(cars)



