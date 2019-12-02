var addWalletButton = document.querySelector('.addWallet').querySelector('button');

if(addWalletButton) {
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
        };
        xhr.send(json);
    });
}


var walletList = document.querySelector('.wallets').querySelectorAll('li');
var depositSection = document.querySelector('.updateBalance--deposit');
var withdrawSection = document.querySelector('.updateBalance--withdraw');


if(walletList) {
    depositSection.querySelector('.updateBalance__closeButton').addEventListener('click', function (e) {
        depositSection.style.display = 'none';
    });

    withdrawSection.querySelector('.updateBalance__closeButton').addEventListener('click', function (e) {
        withdrawSection.style.display = 'none';
    });

    walletList.forEach(function (el) {
        el.addEventListener('click', function (e) {
            if(e.target.dataset.action === 'withdraw') {
                withdrawSection.querySelector('.updateBalance__currency').text = e.currentTarget.querySelector('.wallet-name').text;
                withdrawSection.style.display = 'block';
            }
            if(e.target.dataset.action === 'deposit'){
                depositSection.querySelector('.updateBalance__currency').text = e.currentTarget.querySelector('.wallet-name').text;
                depositSection.style.display = 'block';
            }
        });
    });
}
