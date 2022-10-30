async function LoadGames(){
    nl=await eel.ListGameNames()();
    console.log(nl);
    if (await nl!=-1){
        for (const element of nl) {
            document.getElementById("menu").innerHTML+=`<div class="menu-element" onclick="OpenSaves('`+element+`');">`+element+`</div>`;
        }
    }
}

LoadGames();