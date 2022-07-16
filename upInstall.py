# Script to Install/Update beta tester

import urllib.request
import zipfile

REPO = "https://github.com/codexfast/pixhos/archive/refs/heads/main.zip"
TARGET = "/temp"
FILE = "pixhos.zip"

def getPixhos() -> urllib:
    return urllib.request.urlretrieve(REPO, FILE)

def install(res: urllib): # Update/install
    with zipfile.ZipFile(FILE, "r") as z_ref:
        z_ref.extractall(TARGET)

if __name__ == "__main__":
    try:
        install(getPixhos())    
    except:
        pass