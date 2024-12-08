import requests

def view(site, links):

    print("-")
    print(site)
    print("-")

    print("0: Exit 1: Home 2: page2")
    #print(links)
    inputvar = int(input("Input: ")) - 1
    if inputvar < len(links) and inputvar > -1:
        return links[inputvar]
    else:
        return "exit"


serv = input("Input server address (leave blank to enter homepage): ")
if serv == "":
    serv = "https://gurra-h.neocities.org"
x = requests.get(serv + '/index.txt')
linkstxt = requests.get(serv + '/links.txt').text
links = linkstxt.split("\n")
inputresult = view(x.text, links)
while not inputresult == "exit":
    inputresult = view(requests.get(inputresult).text, links)

input("Press enter to exit... ")
