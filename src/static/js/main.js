/**
 * Main js file that contains all the functionality 
 * for the buttons not linked via flask.
 */

// VARIABLES
let signInForm = document.querySelector('.sign-in-form');
let loginBtns = document.querySelectorAll('.login-btns');
let formCloseBtn = document.getElementById('form-close-btn');



// Add event listeners for login buttons
loginBtns.forEach((x) => {
    x.addEventListener('click', () => {
        openSignInForm();
    });
});

// Add event listener for form close btn
formCloseBtn.addEventListener('click', () => {
    closeSignInform();
});

/** Opens the sign in form */
function openSignInForm() {
    signInForm.style.top = '50%';
    signInForm.style.opacity = '1';
    signInForm.style.width  = '280px';
    signInForm.style.height = '300px';
}

/** Closes the sign in form */
function closeSignInform() {
    signInForm.style.top = '0%';
    signInForm.style.opacity = '0';
    signInForm.style.width  = '0px';
    signInForm.style.height = '0px';
}