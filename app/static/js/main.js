var addWalletButton = document.querySelector('.addWallet').querySelector('button');

addWalletButton.addEventListener('click', function (e) {
    e.preventDefault();
    var index = document.querySelector('.addWallet').querySelector('select').selectedIndex;
    var value = document.querySelector('.addWallet').querySelector('select').options[index].value;
    console.log(value);
    var json = JSON.stringify({
        value: value
    });

    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/api/create-wallet', true)
    xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');

    xhr.onreadystatechange = function () {
        if (this.readyState != 4) return;
        var clone = document.importNode(document.querySelector('#wallet').content, true);
        clone.querySelector('.wallet-name').innerHTML = this.responseText;
        document.querySelector('.wallets').querySelector('ul').appendChild(clone);
    }
    xhr.send(json);
});