import requests

def view(site, links, pages):

    print("-")
    print(site)
    print("-")

    print("0: Exit " + pages)
    #print(links)
    inputvar = int(input("Input: ")) - 1
    if inputvar < len(links) and inputvar > -1:
        return links[inputvar]
    else:
        return "exit"

serv = input("Input server address (leave blank to enter homepage): ")

#Redirect to txtbrowse homepage
if serv == "":
    serv = "https://gurra-h.neocities.org"

#Get site, links and pages
x = requests.get(serv + '/index.txt')
linkstxt = requests.get(serv + '/links.txt',).text
links = linkstxt.split("\n")
pages = requests.get(serv + '/pages.txt',).text
inputresult = view(x.text, links, pages)

#Switch between pages
while not inputresult == "exit":
    inputresult = view(requests.get(inputresult).text, links, pages)

input("Press enter to exit... ")
