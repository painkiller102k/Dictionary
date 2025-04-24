import json
import requests

andmed = {
    "name": "Anna",
    "age": 25,
    "abielus": "False"
}
json_string = json.dumps(andmed, indent=2, sort_keys=True)
print(json_string)

#lisame faili
with open("Json-txt.json", "w") as fail:
    json.dump(andmed, fail)

#loeme faili
with open("Json-txt.json", "r") as fail:
    andmed_failist = json.load(fail)
print(andmed_failist)


klass = {
"opetaja": "Tamm",
"opilased": [
{"nimi": "Mari", "hinne": 5},
{"nimi": "Jüri", "hinne": 4}
]
}
with open("klass.json", "w", encoding='utf-8-sig') as f:
    json.dump(klass, f, indent=2)

linn = input("Sisesta linna nimi: ")
api_voti = "1dd3fb621436f6352f0c550dcb441b7d" # asenda oma API võtmega
url = f"http://api.openweathermap.org/data/2.5/weather?q={linn}&appid={api_voti}&units=metric&lang=et"
vastus = requests.get(url)
andmed = vastus.json()
if andmed.get("cod") != "404" and "main" in andmed and "weather" in andmed:
 peamine = andmed["main"]
 temperatuur = peamine["temp"]
 niiskus = peamine["humidity"]
 kirjeldus = andmed["weather"][0]["description"]
 tuul = andmed["wind"]["speed"]
 print(f"\nIlm linnas {linn}:")
 print(f"Temperatuur: {temperatuur}°C")
 print(f"Kirjeldus: {kirjeldus.capitalize()}")
 print(f"Niiskus: {niiskus}%")
 print(f"Tuule kiirus: {tuul} m/s")
else:
 print("Linna ei leitud. Palun kontrolli nime õigekirja.")
with open("ilm.json", "w", encoding="utf-8") as f:
 json.dump(andmed, f, ensure_ascii=False, indent=4)


#keerulised andmed
with open ("andmed_keerulised.json", "r", encoding="utf-8") as f:
    andmed = json.load(f)
    
sisetatud_nimi = input("Sisesta nimi: ")

if andmed.get("nimi", "Voti ei ole") == sisetatud_nimi:
    print(f"Autod kasutajal {sisetatud_nimi}:")
    for auto in andmed.get("autod", []):
       print(f"- {auto['muudel']} {auto['varv']}, {auto['joud']} hj), number: {auto['number']}")
else:
    print(f"Kasutajat {sisetatud_nimi} ei leitud.")