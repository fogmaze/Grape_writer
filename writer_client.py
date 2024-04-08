from time import sleep
import os
import writer
import requests
import scorer_py as scorer

host = "localhost"

def getFile(filename) :
    r = requests.get("http://"+host+":8000/"+filename, stream=True)
    with open(filename, 'wb') as file:
        for chunk in r.iter_content(chunk_size=8192):
            file.write(chunk)


def postFile(filename) :
    with open(filename, 'rb') as file:
        r = requests.post("http://"+host+":8000/"+filename, data=file)
    print(r.text)

if __name__ == "__main__":
    while os.path.isfile("highSchool.db"):
        print("Warn: database file already exists")
        sleep(1)
    getFile("highSchool.db")
    getFile("data.pkl")
    try:
        writer.operate()
        scores = scorer.Scores()
        scorer.startScoring(scores)
    finally:
        postFile("highSchool.db")
        postFile("data.pkl")
        print("posted")
        while True:
            try:
                os.remove('highSchool.db')
                os.remove('data.pkl')
            except:
                print('cannot remove db file')
                sleep(1)
            else:
                break