import eel
import os
import json
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


"""GameName:
    GamePath:Path,
    Type:File/Folder,
    SavesPath:Path,
    Saves:
        Savename1,
        Savename2,
        Savename3"""


separator=":"
DATAFOLDER="data/"
GAMESDATAFILE="gamesdata.json"
GAMESDATAPATH=DATAFOLDER+GAMESDATAFILE
try:
    gamesData=json.loads(open(GAMESDATAPATH,"r").read())
except json.JSONDecodeError:
    gamesData={}
# name of folder where the html, css, js, image files are located
eel.init('templates')

def UpdateJSON(data):
    open(GAMESDATAPATH,"w").write(json.dumps(gamesData))


@eel.expose
def ListGameNames():
    """Returns Game NAMES"""
    print(gamesData)
    if gamesData=={}:
        return -1
    a=[]
    for i in gamesData:
        a.append(i)
    return a


@eel.expose
def GetSaves(GameID):
    """Gets all the save NAMES of a specific Game"""
    a=[]
    for i in gamesData[GameID]["Saves"]:
        a.append(i)
    return a

@eel.expose
def GetActiveSave(GameID):
    """Returns the name of the active save"""
    for i in gamesData[GameID]["Saves"]:
        if gamesData[GameID]["Saves"][i]:
            return i
    return -1



@eel.expose
def AddNameToFile(GameID,SaveName):
    """Adding a .SAVENAME suffix to the active file"""

    path=gamesData[GameID]["SavesPath"]
    resultpath=path+"."+SaveName
    os.rename(path,resultpath)

    gamesData[GameID]["Saves"][SaveName]=False


@eel.expose
def RemoveNameFromFile(GameID,SaveName):
    """Removing the .SAVENAME suffix from the specified file"""

    path=gamesData[GameID]["SavesPath"]+"."+SaveName
    resultpath=path.replace("."+path.split(".")[-1],"")
    os.rename(path,resultpath)

    gamesData[GameID]["Saves"][SaveName]=True
    UpdateJSON(gamesData)

@eel.expose
def CreateSaveData(GameID,SaveName):
    """Creates a new folder and puts the old one as disabled"""
    active=GetActiveSave(GameID)
    gamesData[GameID]["Saves"][SaveName]=True
    gamesData[GameID]["Saves"][active]=False
    AddNameToFile(GameID,active)
    os.mkdir(path=gamesData[GameID]["SavesPath"])
    UpdateJSON(gamesData)


@eel.expose
def CreateGameData(GameID,SavePath):
    gamesData[GameID]={"SavesPath":SavePath,"Saves":{"Default":True}}
    UpdateJSON(gamesData)

@eel.expose
def AskDirectoryInput():
    return filedialog.askdirectory().replace("\\","/")
    

# 300 is width of window and 400 is the height
eel.start('index.html',size=(300, 400))
