from mcstatus import JavaServer
import concurrent.futures
import json

#imput_file_name = "dockerformcstatus\dockerMyScript\pyscript\input.txt"
imput_file_name = "/pyscript/input.txt"

def savedata(serverdata):
    global serverJsonData
    serverJsonData.append(serverdata)

def scaner(data):
    #print("Processing data: ", data)
    #global serverJsonData
    global timeout
    server = JavaServer.lookup(data,5)
    #print(server)
    try:
        serverJson = server.status().raw
        return serverJson
    except:
       print("can't connect")

if __name__ == "__main__":

    serverJsonData = []
    timeout = 5

    data = None
    with open(imput_file_name,"r") as f:
        data = f.readlines()

    #print(data)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for result in executor.map(scaner,data):
            if not result == None:
                serverJsonData.append(result)

    #    for f in concurrent.futures.as_completed(res):
    #         print(f)

    #scaner("168.119.4.46:25619")

    with open("/pyscript/serverdata.json", "w") as f:
        f.write(json.dumps(serverJsonData))