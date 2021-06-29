const priceInput = document.querySelector('.input_price');
const pplInput = document.getElementById('input_ppl');
const maxPplInput = document.getElementById('input_max_ppl');
const btnMinus = document.querySelector('.btn_minus');
const btnPlus = document.querySelector('.btn_plus');
const pplDetail = document.querySelector('.detail_ppl');
const priceDetail = document.querySelector('.detail_price');

if (pplInput.value <= 1) {
  btnMinus.disabled = true;
  btnMinus.classList.add('disabled');
}

if (+maxPplInput.value <= +pplInput.value) {
  btnPlus.disabled = true;
  btnPlus.classList.add('disabled');
}

if (btnPlus) {
  btnPlus.addEventListener('click', () => {
    btnHandler('plus');
  });
}

if (btnMinus) {
  btnMinus.addEventListener('click', () => {
    btnHandler('minus');
  });
}

function btnHandler(type) {
  numOfPeople = +pplInput.value;
  price = +priceInput.value;

  if (type === 'plus') {
    newNumOfPeople = numOfPeople + 1;
  } else {
    newNumOfPeople = numOfPeople - 1;
  }

  pplInput.value = newNumOfPeople;
  pplDetail.textContent = newNumOfPeople;
  priceDetail.textContent = `$ ${price * newNumOfPeople}`;

  if (newNumOfPeople === +maxPplInput.value) {
    btnPlus.disabled = true;
    btnPlus.classList.add('disabled');
  } else {
    btnPlus.disabled = false;
    btnPlus.classList.remove('disabled');
  }

  if (newNumOfPeople > 1) {
    btnMinus.disabled = false;
    btnMinus.classList.remove('disabled');
  } else {
    btnMinus.disabled = true;
    btnMinus.classList.add('disabled');
  }
}
