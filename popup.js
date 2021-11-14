
function fn1(){
    var str = document.getElementById("YT_Url").value;
    var vOneLS = localStorage.getItem("vOneLocalStorage");
    var current_link = vOneLS
    }

    document.getElementById('Extract').addEventListener('click', onclick
    , true)
    function onclick(){
    fn1()

    
}
const keywords = []
document.getElementById('Keyword').addEventListener('click', onclick
    , true)
    function onclick(){
    var key = document.getElementById("Keyword_input").value;
    keywords.push(key)
}



var s = '<div id="YT_Url"></div>';
var htmlObject = document.createElement('div');
htmlObject.innerHTML = s;
htmlObject.getElementById("YT_Url").style.marginTop = something;





str = 'hello world'
function sendUserInfo() {
    let userInfo = {
        'string' : str
    }
    const request = new XMLHttpRequest()
    request.open('POST', '/processUserInfo/${JSON.stringify(userInfo)}')
    request.onload = () => {
        const flaskMessage = request.responseText
        console.log(flaskMessage)
        
    
    }
    request.send()
}
