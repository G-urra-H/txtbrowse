import requests

def view(site):
    
    print("-")
    print(site)
    print("-")
    

serv = input("Input server address (leave blank to enter homepage): ")
if serv == "":
    serv = "https://gurra-h.neocities.org"
x = requests.get(serv + '/index.txtb')
view(x.text)


input("Press enter to exit... ")
