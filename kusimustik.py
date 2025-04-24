import json
import random
import smtplib
from email.mime.text import MIMEText

# загрузка вопросов json
def loe_kusimused_failist(failinimi):
    try:
        with open(failinimi, 'r', encoding='utf-8') as f:
            return json.load(f) #в словарт
    except FileNotFoundError:
        print(f"Faili '{failinimi}' ei leitud. Alustame tühja küsimustikuga.")

# сохранение json
def salvesta_kusimused_faili(failinimi, kus_vas):
    with open(failinimi, 'w', encoding='utf-8') as f:
        json.dump(kus_vas, f, ensure_ascii=False, indent=4)

# Функция для проведения опроса
def kysimustik(kus_vas, kasutaja_nimi, kysimuste_arv):
    print(f"Tere, {kasutaja_nimi}! Alustame küsimustikku.")
    kysimused = random.sample(list(kus_vas.keys()), kysimuste_arv)
    oiged_vastused = 0

    for kysimus in kysimused:
        vastus = input(f"{kysimus} ")
        if vastus.lower() == kus_vas[kysimus].lower():
            oiged_vastused += 1

    return oiged_vastused

# Функция для добавления нового вопроса
def lisa_kusimus(failinimi, kus_vas):
    uus_kusimus = input("Sisesta uus küsimus: ")
    uus_vastus = input("Sisesta õige vastus: ")
    kus_vas[uus_kusimus] = uus_vastus
    salvesta_kusimused_faili(failinimi, kus_vas)
    print("Küsimus lisatud!")

# Функция отправки email
def saada_email(saaja, teema, sisu):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        saatja_email = "rossakovmartin@gmail.com"
        saatja_parool = "qhza flhd stuw jhpg"

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(saatja_email, saatja_parool)

        msg = MIMEText(sisu, _charset="utf-8")
        msg["Subject"] = teema
        msg["From"] = saatja_email
        msg["To"] = saaja


        server.sendmail(saatja_email, saaja, msg.as_string())
        server.quit()
        print(f"E-kiri saadetud: {saaja}")
    except Exception as e:
        print(f"Viga e-kirja saatmisel: {e}")

failinimi = "kusimused_vastused.json"
kus_vas = loe_kusimused_failist(failinimi)

while True:
    print("1. Alusta küsimustikku")
    print("2. Lisa uus küsimus")
    print("3. Välju")
    valik = input("Vali tegevus: ")

    if valik == "1":
        nimi = input("Sisesta oma nimi ja perekonnanimi: ")
        email = input("Sisesta oma e-posti aadress: ")
        
        if len(kus_vas) < 4:
            print("Küsimusi on liiga vähe, lisa rohkem küsimusi.")
            continue

        oiged = kysimustik(kus_vas, nimi, 4)

        with open("koik.txt", "a", encoding="utf-8") as f:
            f.write(f"{nimi}, {oiged}, {email}\n")


        if oiged >= 2:
            with open("oiged.txt", "a", encoding="utf-8") as f:
                f.write(f"{nimi} – {oiged} õigesti\n")
            print(f"Tulemused salvestatud faili 'oiged.txt'. Õigeid vastuseid: {oiged}")

            teema = "Küsitluse tulemused"
            sisu = (
                f"Tere, {nimi}!"
                f"Sa vastasid küsitlusele edukalt ja said {oiged} õigesti vastatud küsimust!"
                f"Palju õnne!"
            )
            saada_email(email, teema, sisu)

        else:
            with open("valed.txt", "a", encoding="utf-8") as f:
                f.write(f"{nimi} – {oiged} õigesti\n")
            print(f"Tulemused salvestatud faili 'valed.txt'. Õigeid vastuseid: {oiged}")

    elif valik == "2":
        lisa_kusimus(failinimi, kus_vas)
    elif valik == "3":
        print("Head aega!")
        break
    else:
        print("Vale valik, proovi uuesti.")
