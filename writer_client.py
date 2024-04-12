from time import sleep
import os
import writer
import requests

host = "150.116.202.108:49"

def getFile(filename) :
    r = requests.get("http://"+host+"/"+filename, stream=True)
    with open(filename, 'wb') as file:
        for chunk in r.iter_content(chunk_size=8192):
            file.write(chunk)

def postFile(filename) :
    with open(filename, 'rb') as file:
        r = requests.post("http://"+host+"/"+filename, data=file)
    print(r.text)

if __name__ == "__main__":
    while os.path.isfile("highSchool.db"):
        print("Warn: database file already exists")
        sleep(1)
    getFile("highSchool.db")
    try:
        writer.operate()
    finally:
        postFile("highSchool.db")
        print("posted")
        while True:
            try:
                os.remove('highSchool.db')
            except:
                print('cannot remove db file')
                sleep(1)
            else:
                break