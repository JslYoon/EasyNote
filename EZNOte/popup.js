
function fn1(){
    var str = document.getElementById("YT_Url").value;
    var vOneLS = localStorage.getItem("vOneLocalStorage");
    var current_link = vOneLS
    alert("hi") 
    }

    document.getElementById('Extract').addEventListener('click', onclick
    , true)
    function onclick(){
        alert("hi")
    fn1()
}

document.getElementById('Keyword').addEventListener('click', onclick
    , false)
    function onclick(){
    
    alert("processing. Please wait")
    window.open("https://docs.google.com/document/d/1D-LnuhRr9MLR22CO7nFLRhKstuYhtlX-7zxkMxl-Ixk/edit");

    //saveStaticDataToFile()
    
   




}


function saveStaticDataToFile() {
    const keywords = []
    var key = document.getElementById("Keyword_input").value;
keywords.push(key)
saveAs(keywords, "static.txt");
}






