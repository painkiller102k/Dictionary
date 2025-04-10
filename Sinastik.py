import random

sonastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

def tolgi_est_rus(sona: str) -> str:
    """Tõlgib eesti keelest vene keelde.
    переводит с эстонского на русский язык
    """
    if sona in sonastik:
        return sonastik[sona]
    else:
        return "Sõna ei leitud sõnastikust."

def tolgi_rus_est(sona: str) -> str:
    """Tõlgib vene keelest eesti keelde.
    перевод с русского на эстонский язык
    """
    for est, rus in sonastik.items():
        if rus == sona:
            return est
    return "Sõna ei leitud sõnastikust."

def lisa_sona():
    """Lisab uue sõna sõnastikku.
    добавляет новое слово в словарь
    """
    est = input("Sisesta uus sõna eesti keeles: ")
    rus = input("Sisesta selle sõna vene tõlge: ")
    if est in sonastik:
        print("Sõna on juba sõnastikus.")
    else:
        sonastik[est] = rus
        print("Sõna lisatud!")

def paranda_sona():
    """Parandab sõna tõlget sõnastikus.
    исправляет определенное слово
    """
    est = input("Sisesta sõna, mida soovid parandada: ")
    if est in sonastik:
        uus_rus = input(f"Sisesta uus tõlge sõnale {est}: ")
        sonastik[est] = uus_rus
        print("Tõlge parandatud!")
    else:
        print("Sõna ei leitud sõnastikust.")

def testi_teadmisi():
    """Testib kasutaja teadmisi sõnastikust.
    тест
    """
    correct = 0
    total = len(sonastik)
    for est, rus in random.sample(list(sonastik.items()), total):
        vastus = input(f"Sisesta vene tõlge sõnale '{est}': ")
        if vastus == rus:
            print("Õige!")
            correct += 1
        else:
            print(f"Vale! Õige vastus on '{rus}'.")
    protsent = (correct / total) * 100
    print(f"Test lõppenud! Sinu tulemus: {protsent:.2f}%")

print("Tere tulemast eesti-vene sõnastikku!")

while True:
    print("Menu:")
    print("1 - Tõlgi eesti vene")
    print("2 - Tõlgi vene eesti")
    print("3 - Lisa uus sõna")
    print("4 - Paranda sõna")
    print("5 - Testi teadmisi")
    print("6 - Quit")

    try:
        choice = int(input("Tee oma valik: "))
        if choice == 1:
            sona = input("Sisesta sõna eesti keeles: ")
            print(f"Tõlge vene keelde: {tolgi_est_rus(sona)}")
        elif choice == 2:
            sona = input("Sisesta sõna vene keeles: ")
            print(f"Tõlge eesti keelde: {tolgi_rus_est(sona)}")
        elif choice == 3:
            lisa_sona()
        elif choice == 4:
            paranda_sona()
        elif choice == 5:
            testi_teadmisi()
        elif choice == 6:
            print("Quit")
            break
        else:
            print("Viga: Palun vali korrektne number.")
    except ValueError:
        print("Viga: Palun sisesta number.")