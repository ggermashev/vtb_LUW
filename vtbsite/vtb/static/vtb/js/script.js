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