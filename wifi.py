import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp1252').split("\n")
profiles = [i.split(':')[1][1:-1] for i in data if 'Profil Tous les utilisateurs' in i]

for pr in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', pr, "key=clear"]).decode("cp1252").split("\n")
        for i in results:
            if "Contenu de la" in i:
                key = i.split(":")[1][1:-1]
                print("{:<50}|  {}".format(pr, key))
    except:
        print()
        print("Error with...",pr)
        print()

input("")