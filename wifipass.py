import subprocess
import sys

args = sys.argv[1:]
language = ["FR"]

if len(args) != 1 or args[0] not in language:
    print(f'Usage:')
    for i in language:
        print(f"        python wifi.py {i}")
    input()
    sys.exit()
else:
    if args[0] == "FR":
        check_profile = "Profil Tous les utilisateurs"
        check_key = "Contenu de la"
        check_open = "Authentification         : Ouvrir"


data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp1252').split("\n")
profiles = [i.split(':')[1][1:-1] for i in data if check_profile in i]

print()
print("*"*61)
print("{:<50}|  {}".format("Network", "Password"))
print("*"*61)
print()
for pr in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', pr, "key=clear"]).decode("cp1252").split("\n")
        for i in results:
            if check_key in i:
                key = i.split(":")[1][1:-1]
                print("{:<50}|  {}".format(pr, key))
            elif check_open in i:
                key = i.split(":")[1][1:-1]
                print("{:<50}|  NO KEY FOR THE NETWORK... !".format(pr))
    except:
        print()
        print("Error with...",pr)
        print()

input("")