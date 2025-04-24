import json
import random
import smtplib


# загрузка вопросов json
def loe_kusimused_failist(failinimi):
    try:
        with open(failinimi, 'r', encoding='utf-8') as f:
            return json.load(f) #в словарт
    except FileNotFoundError:
        print(f"Faili '{failinimi}' ei leitud.")

# сохранение json
def salvesta_kusimused_faili(failinimi, kusimusvastus):
    with open(failinimi, 'w', encoding='utf-8') as f:
        json.dump(kusimusvastus, f, ensure_ascii=False, indent=4)


def kysimustik(kusimusvastus, kasutaja_nimi, kysimuste_arv):
    print(f"Tere, {kasutaja_nimi}! Alustame küsimustikku.")
    kysimused = random.sample(list(kusimusvastus.keys()), kysimuste_arv)
    oiged_vastused = 0

    for kysimus in kysimused:
        vastus = input(f"{kysimus} ")
        if vastus.lower() == kusimusvastus[kysimus].lower():
            oiged_vastused += 1
            print("Õige vastus ! ")

    return oiged_vastused

def lisa_kusimus(failinimi, kusimusvastus):
    uus_kusimus = input("Sisesta uus küsimus: ")
    uus_vastus = input("Sisesta õige vastus: ")
    kusimusvastus[uus_kusimus] = uus_vastus
    salvesta_kusimused_faili(failinimi, kusimusvastus)
    print("Küsimus lisatud!")

# gmail send
def saada_email(saaja, teema, sisu):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        saatja_email = "rossakovmartin@gmail.com"
        saatja_parool = "qhza flhd stuw jhpg"

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(saatja_email, saatja_parool)

        
        email_message = (
            f"Subject: {teema}\n"
            f"From: {saatja_email}\n"
            f"To: {saaja}\n"
            f"Content-Type: text/plain; charset=utf-8\n\n"
            f"{sisu}" )

        server.sendmail(saatja_email, saaja, email_message.encode('utf-8'))
        server.quit()
        print(f"E-kiri saadetud: {saaja}")
    except Exception as e:
        print(f"Viga e-kirja saatmisel: {e}")

failinimi = "kusimused_vastused.json"
kusimusvastus = loe_kusimused_failist(failinimi)

while True:
    print("1. Alusta küsimustikku")
    print("2. Lisa uus küsimus")
    print("3. Välju")
    valik = input("Vali tegevus: ")

    if valik == "1":
        nimi = input("Sisesta nimi ja perekonanimi : ")
        email = input("Sisesta email aadress: ")
        
        if len(kusimusvastus) < 4:
            print("Küsimusi on liiga vähe, lisa rohkem küsimusi.")
            continue

        oiged = kysimustik(kusimusvastus, nimi, 4)

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
                f.write(f"{nimi} – {oiged} õigesti \n \n")
            print(f"Tulemused salvestatud faili 'valed.txt'. Õigeid vastuseid: {oiged}")

    elif valik == "2":
        lisa_kusimus(failinimi, kusimusvastus)
    elif valik == "3":
        print("Head aega ! ")
        break
    else:
        print("Vale valik ! ")
