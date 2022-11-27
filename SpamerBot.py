import requests

while True:
    whom=input("whom: ")
    massage=input("massage: ")
    api_key=input("api_key: ")
    if "" in whom or massage=="":
        break

    resp=requests.post("https://textbelt.com/text",{


        'phone':'{}'.format(whom),
        'massage':"{}".format(massage),
        'api_key':"{}".format(api_key),
    })
    print("process: {} Your reamining right: {}.".format('successful' if resp.json()[SUCCESS]=='True' else 'unseccessful',resp.json()['qoutaremaning'])) 

    c=input("exit or enter:")

    if c=="exit":
        break
    else:
        pass