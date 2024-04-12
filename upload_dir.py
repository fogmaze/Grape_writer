import requests
import os


host = "150.116.202.108:49"

def getFile(filename) :
    r = requests.get("http://"+host+"/"+filename, stream=True)
    with open(filename, 'wb') as file:
        for chunk in r.iter_content(chunk_size=8192):
            file.write(chunk)

def postFile(filename, destname=None) :
    with open(filename, 'rb') as file:
        if destname is not None:
            r = requests.post("http://"+host+"/"+destname, data=file)
        else:
            r = requests.post("http://"+host+"/"+filename, data=file)
    print(r.text)


if __name__ == "__main__":
    # list all files and dirs in the directory
    postFile("data_np.pkl")
    postFile("highSchool.db")
    exit()
    files = []
    files += [os.path.join("web", n) for n in os.listdir("web/")]
    for file in files:
        if os.path.isdir(file):
            files += [os.path.join(file, n) for n in os.listdir(file)]
        else :
            # remove first dir of the filename
            postFile(file, file[4:])
            print(file)
