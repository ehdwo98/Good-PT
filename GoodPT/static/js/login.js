let getScrollY = 0; 
let myString = '약관동의내용'; 
const signUpBtn = document.getElementById("signUp");
const signInBtn = document.getElementById("signIn");
const container = document.querySelector(".container-login");
const loginBtn = document.getElementById("login_button")


function toggleModal(id, show = true) {
    let modal = document.getElementById(id),
    isVisible = modal.classList.contains('show'),
    body = document.querySelector('body');

    if (!modal) return;

    if (show && !isVisible) {
        getScrollY = window.scrollY;
        body.style.top = `${-getScrollY}px`;

        modal.classList.add('show');

        updateModalContent();
    } else {
        modal.classList.remove('show');
        window.scrollTo(0, getScrollY);
    }
}


function updateModalContent() {
  
    var contentPlaceholder = document.getElementById('contentPlaceholder');
    if (contentPlaceholder) {
        contentPlaceholder.innerHTML = myString; 
    }
}


window.addEventListener('load', () => {
    getScrollY = 0;
});


document.addEventListener('click', (e) => {
    let modal = document.querySelector('.modal');
    if (e.target.id === modal.id) toggleModal(modal.id, false);
});

signUpBtn.addEventListener("click", () => {
  toggleModal('termsConditions');
});
signInBtn.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});

document.addEventListener('DOMContentLoaded', function () {
  var acceptButton = document.querySelector('.modal.agreement-popup .bottom button.btn-primary');
  console.log(acceptButton)
  if (acceptButton) {
      acceptButton.addEventListener('click', function () {
        var modalId = 'termsConditions';
        toggleModal(modalId, false);
      
          container.classList.add('right-panel-active');
      });
  }
});

