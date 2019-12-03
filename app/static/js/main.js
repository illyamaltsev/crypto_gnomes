var addwalletEl = document.querySelector('.addWallet');


if(addwalletEl) {
    var addWalletButton = addwalletEl.querySelector('button');
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


var walletEl = document.querySelector('.wallets');


if(walletEl) {
    var walletList = walletEl.querySelectorAll('li');
    var depositSection = document.querySelector('.updateBalance--deposit');
    var withdrawSection = document.querySelector('.updateBalance--withdraw');
    var postWithdraw = function() {

    }
    var postDeposit = function() {

    }

    depositSection.querySelector('.updateBalance__closeButton').addEventListener('click', function (e) {
        depositSection.querySelector('.deposit').removeEventListener('click', postDeposit);
        depositSection.style.display = 'none';
    });

    withdrawSection.querySelector('.updateBalance__closeButton').addEventListener('click', function (e) {
        withdrawSection.querySelector('.withdraw').removeEventListener('click', postWithdraw);
        withdrawSection.style.display = 'none';
    });

    walletList.forEach(function (el) {
        el.addEventListener('click', function (e) {
            if(e.target.dataset.action === 'withdraw') {
                postWithdraw = function() {
                    var formData = new FormData(document.forms.withdraw);
                    formData.append("user_coin_id", el.querySelector('.wallet-name').id);
                    var xhr = new XMLHttpRequest();
                    xhr.open("POST", "/api/do-withdraw/");

                    xhr.onreadystatechange = function() {
                      if (this.readyState != 4) return;
                      withdrawSection.querySelector('.updateBalance__closeButton').click();
                      el.querySelector('.wallet-amount').textContent = +el.querySelector('.wallet-amount').textContent - withdrawSection.querySelector('input').value;
                    }
                    xhr.send(formData);
                }
                withdrawSection.querySelector('.updateBalance__currency').text = e.currentTarget.querySelector('.wallet-name').text;
                withdrawSection.style.display = 'block';
                withdrawSection.querySelector('.withdraw').addEventListener('click', postWithdraw);
            }
            if(e.target.dataset.action === 'deposit') {
                postDeposit = function() {
                    var formData = new FormData(document.forms.deposit);
                    formData.append("user_coin_id", el.querySelector('.wallet-name').id);
                    var xhr = new XMLHttpRequest();
                    xhr.open("POST", "/api/do-deposit/");

                    xhr.onreadystatechange = function() {
                      if (this.readyState != 4) return;
                      depositSection.querySelector('.updateBalance__closeButton').click();
                      el.querySelector('.wallet-amount').textContent = +el.querySelector('.wallet-amount').textContent + +depositSection.querySelector('input').value;
                    }
                    xhr.send(formData);
                }
                depositSection.querySelector('.updateBalance__currency').text = e.currentTarget.querySelector('.wallet-name').text;
                depositSection.style.display = 'block';
                depositSection.querySelector('.deposit').addEventListener('click', postDeposit);
            }
        });
    });
}

var createOrderButton = document.querySelector('.create-order');

if(createOrderButton) {
    createOrderButton.addEventListener('click', function () {
        var formEl = document.forms.createOrder;
        var formData = new FormData(formEl);
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/api/stakan/create/");

        xhr.onreadystatechange = function() {
          if (this.readyState != 4) return;
          var clone = document.importNode(document.querySelector('#order').content, true);
          clone.querySelector('.order__from').innerHTML = formEl.querySelector('select[name=from]').options[formEl.querySelector('select[name=from]').selectedIndex].text;
          clone.querySelector('.order__to').innerHTML = formEl.querySelector('select[name=to]').options[formEl.querySelector('select[name=to]').selectedIndex].text;
          clone.querySelector('.order__price').innerHTML = formData.get('price');
          clone.querySelector('.order__count').innerHTML = formData.get('count');
          document.querySelector('.orders').querySelector('ul').appendChild(clone);
        }
        xhr.send(formData);
    });
}
