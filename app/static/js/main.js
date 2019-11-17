var addWalletButton = document.querySelector('.addWallet').querySelector('button');

addWalletButton.addEventListener('click', function(e) {
    e.preventDefault();
    var index = document.querySelector('.addWallet').querySelector('select').selectedIndex;
    var value = document.querySelector('.addWallet').querySelector('select').options[index].value;
    console.log(value);
    var json = {
        value: value
    }

    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/create-wallet', true)
    xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');

    xhr.onreadystatechange = function() {
    if (this.readyState != 4) return;
        alert( this.responseText );
    }
    xhr.send(json);
});