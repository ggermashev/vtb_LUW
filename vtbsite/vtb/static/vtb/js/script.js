function ChangeFont(Class, Color)
{

document.getElementsByClassName(Class)[0].style.color = Color;
}

function create_wallet() {
    let req = new XMLHttpRequest();
    req.open('POST', "https://hackathon.lsp.team/hk/v1/wallets/new" )
    req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    req.send()
    alert(req.responseText)
}

function ChangeColor(ID, Class){
document.getElementById(ID).style.backgroundImage = 'linear-gradient(to left, #5f5f5f, 80%, #262626)';
document.getElementsByClassName(Class)[0].style.backgroundImage = 'clear';
}