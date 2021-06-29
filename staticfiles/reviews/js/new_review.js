const ratingList = document.querySelector('.radio_btn_list');
const ratingLabels = document.querySelectorAll('.radio_btn_label');
const ratingInputs = document.querySelectorAll('.radio_input');

if (ratingInputs) {
  ratingInputs.forEach(input => {
    if (input.checked) {
      const label = input
        .closest('.radio_btn_container')
        .querySelector('.radio_btn_label');

      label.classList.add('active');
    }
  });
}

if (ratingList) {
  ratingList.addEventListener('click', e => {
    const ratingLabel = e.target.closest('.radio_btn_label');

    if (!ratingLabel) return;

    ratingLabels.forEach(label => {
      label.classList.remove('active');
    });

    ratingLabel.classList.add('active');
  });
}
