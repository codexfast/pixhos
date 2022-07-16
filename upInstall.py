# Script to Install/Update beta tester

import urllib.request
import zipfile
import shutil

REPO = "https://github.com/codexfast/pixhos/archive/refs/heads/main.zip"
TARGET = "./temp"
FOLDER_INSTALL = "./src"
FILE = "pixhos.zip"

def getPixhos() -> urllib:
    return urllib.request.urlretrieve(REPO, FILE)

def install(res: urllib): # Update/install
    with zipfile.ZipFile(FILE, "r") as z_ref:
        z_ref.extractall(TARGET)

    shutil.rmtree(FOLDER_INSTALL)
    shutil.move(TARGET+'/pixhos-main/src', './src')
    shutil.rmtree(TARGET)
    

if __name__ == "__main__":
    try:
        install(getPixhos())    
    except:
        pass