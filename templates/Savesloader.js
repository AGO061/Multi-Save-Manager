async function LoadSaves(GameID){
    document.getElementById("menu").innerHTML="";
    saves=await eel.GetSaves(GameID)();
    active=await eel.GetActiveSave(GameID)();
    conc="";
    for (const element of saves) {
        if (element==active){
            conc=" highlight";
        }
        else{
            conc="";
        }
        document.getElementById("menu").innerHTML+=`<div class="menu-element`+conc+`" onclick="LoadSave('`+element+`');">`+element+`</div>`;
    }
}

async function LoadSave(SaveID){
    GameID=sessionStorage.getItem('GameID');
    await eel.AddNameToFile(GameID,await eel.GetActiveSave(GameID)())();
    await eel.RemoveNameFromFile(GameID,SaveID)();
    await LoadSaves(GameID);
}

LoadSaves(sessionStorage.getItem('GameID'));