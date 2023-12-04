import time

def afficher_heure(heure_actuelle, mode_12h=False):
    # Formater l'heure au format 12 heures ou 24 heures
    if mode_12h:
        heure_format = time.strftime("%I:%M:%S %p", heure_actuelle)
    else:
        heure_format = time.strftime("%H:%M:%S", heure_actuelle)
    
    # Afficher l'heure formatée
    print(heure_format, end='\r')  # Le '\r' permet de revenir au début de la ligne dans la console

def regler_heure(heures, minutes, secondes):
    # Régler l'heure actuelle à celle spécifiée
    nouvelle_heure = time.localtime()
    nouvelle_heure = time.struct_time((nouvelle_heure.tm_year, nouvelle_heure.tm_mon, nouvelle_heure.tm_mday,
                                       heures, minutes, secondes, nouvelle_heure.tm_wday,
                                       nouvelle_heure.tm_yday, nouvelle_heure.tm_isdst))
    return nouvelle_heure

def regler_alarme(heures, minutes, secondes):
    # Régler l'heure de l'alarme
    alarme = time.struct_time((time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday,
                               heures, minutes, secondes, time.localtime().tm_wday,
                               time.localtime().tm_yday, time.localtime().tm_isdst))
    return alarme

def choisir_mode_affichage():
    # Demander à l'utilisateur de choisir le mode d'affichage
    while True:
        choix = input("Choisissez le mode d'affichage (12h ou 24h) : ").lower()
        if choix == '12h':
            return True
        elif choix == '24h':
            return False
        else:
            print("Choix invalide. Veuillez choisir 12h ou 24h.")

def choisir_am_pm():
    # Demander à l'utilisateur de choisir AM ou PM
    while True:
        choix = input("Choisissez AM ou PM : ").upper()
        if choix == 'AM' or choix == 'PM':
            return choix
        else:
            print("Choix invalide. Veuillez choisir AM ou PM.")

# Demander à l'utilisateur de choisir le mode d'affichage
mode_12h = choisir_mode_affichage()

# Demander à l'utilisateur de régler l'heure
heures = int(input("Entrez les heures : "))
minutes = int(input("Entrez les minutes : "))
secondes = int(input("Entrez les secondes :"))

# Régler l'heure initiale
heure_actuelle = regler_heure(heures, minutes, secondes)

# Régler l'alarme
heure_alarme = regler_alarme(14, 0, 0)  # Changer l'heure de l'alarme selon vos préférences

# Boucle infinie pour actualiser l'heure chaque seconde
try:
    while True:
        afficher_heure(heure_actuelle, mode_12h)
        time.sleep(1)  # Attendre une seconde

        # Vérifier si l'heure actuelle correspond à l'heure de l'alarme
        if heure_actuelle.tm_hour == heure_alarme.tm_hour and \
           heure_actuelle.tm_min == heure_alarme.tm_min and \
           heure_actuelle.tm_sec == heure_alarme.tm_sec:
            print("\nRéveil ! Il est temps de se lever.")
            break  # Sortir de la boucle après l'alarme
        heure_actuelle = time.localtime(time.mktime(heure_actuelle) + 1)  # Ajouter une seconde à l'heure actuelle

except KeyboardInterrupt:
    print("\nProgramme arrêté.")
