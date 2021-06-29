const navBtnToggle = document.querySelector('.nav_btn_toggle');
const navList = document.querySelector('.nav_list');
const alertsList = document.querySelector('.alert_messages');

if (navBtnToggle) {
  navBtnToggle.addEventListener('click', () => {
    navList.classList.toggle('active');
		navBtnToggle.classList.toggle('active');
  });
}

if (alertsList) {
  alertsList.addEventListener('click', e => {
    e.target.closest('.alert_message').remove();
  })
}