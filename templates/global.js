function OpenSaves(gameid){
    sessionStorage.setItem("GameID", gameid);
    window.location.replace("saveselect.html");
}

function AddSave(){
    window.location.replace("savecreate.html");
}

function AddGame(){
    window.location.replace("gamecreate.html");
}


async function CreateSaveData(SaveName){
    if (SaveName!=""){
        GameID=sessionStorage.getItem("GameID");
        await eel.CreateSaveData(GameID,SaveName)();
    }
    window.location.replace("saveselect.html");
    
}

async function BrowseGamePath(){
    document.getElementById("gamepath").value=await eel.AskDirectoryInput()();
}

async function CreateGameData(GameName,SavePath){
    if (GameName!="" && SavePath!=""){
        await eel.CreateGameData(GameName,SavePath)
    }
    window.location.replace("index.html");
}